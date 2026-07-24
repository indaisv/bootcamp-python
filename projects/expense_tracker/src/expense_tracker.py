"""
expense_tracker.py
Project 1: Personal Expense Tracker (Day 11 — regex validation + dates added).
Author: Viraj
Date: 2026-07-11
"""

import functools
import csv
import os
import logging
import re
from datetime import datetime
from money_utils import format_currency

logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def is_valid_amount(text: str) -> bool:
    """Return True if text is digits, optionally with 1-2 decimal places."""
    pattern = r"^\d+(\.\d{1,2})?$"
    return re.fullmatch(pattern, text) is not None


class Expense:
    def __init__(self, category: str, amount: float, date: str = None):
        self.category = category
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)} ({self.date})"

    def to_dict(self) -> dict:
        """Convert this Expense into a plain dict, ready for csv.DictWriter."""
        return {"type": "regular", "category": self.category, "amount": self.amount, "frequency": "", "date": self.date}


class RecurringExpense(Expense):
    def __init__(self, category: str, amount: float, frequency: str, date: str = None):
        super().__init__(category, amount, date)
        self.frequency = frequency

    def formatted(self):
        base = super().formatted()
        return f"{base} (repeats {self.frequency})"

    def to_dict(self) -> dict:
        """Same shape as Expense.to_dict(), but records type + frequency so load_expenses() can rebuild this exact class."""
        return {"type": "recurring", "category": self.category, "amount": self.amount, "frequency": self.frequency, "date": self.date}


DATA_FILE = "projects/expense_tracker/data/expenses.csv"

def log_call(func):
    """Decorator: logs the function's name every time it's called."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_call
def save_expenses(expenses: list, filepath: str = DATA_FILE) -> None:
    """Write all expenses to a CSV file, overwriting whatever was there."""
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["type", "category", "amount", "frequency", "date"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense.to_dict())
    

@log_call
def load_expenses(filepath: str = DATA_FILE) -> list:
    """Load expenses from a CSV file. Return an empty list if the file doesn't exist yet."""
    if not os.path.exists(filepath):
        return []

    expenses = []
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("type") == "recurring":
                expenses.append(RecurringExpense(row["category"], float(row["amount"]), row["frequency"], row["date"]))
            else:
                expenses.append(Expense(row["category"], float(row["amount"]), row["date"]))
    
    return expenses


def print_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. Exit")


def add_expense(expenses: list) -> None:
    category = input("Category (Food/Travel/Bills/Other): ").strip().title()
    amount_input = input("Amount (INR): ").strip()
    try:
        if not is_valid_amount(amount_input):
            raise ValueError(f"Invalid amount entered: '{amount_input}'")

        amount = float(amount_input)
        expense = Expense(category, amount)
        expenses.append(expense)
        logging.info(f"Added expense: {category} - {amount}")
        print(f" Added: {expense.formatted()}")
    except ValueError as e:
        logging.error(str(e))
        print("Invalid amount. Please enter a number like 450 or 450.50.")
        
def view_expenses(expenses: list) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense.formatted()}")


def total_by_category(expenses: list) -> dict:
    """Return {category: total_amount} instead of printing directly."""
    totals = {}
    for expense in expenses:
        category = expense.category
        amount = expense.amount
        totals[category] = totals.get(category, 0) + amount

    return totals


def main():
    """The menu loop — the heart of every CLI tool you'll ever build."""
    expenses = load_expenses()  # loads whatever was saved last time, if anything

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            totals = total_by_category(expenses)
            if not totals:
                print("No expenses recorded yet.")
            else:
                for category, total in totals.items():
                    print(f"{category}: {format_currency(total)}")
        elif choice == "4":
            save_expenses(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
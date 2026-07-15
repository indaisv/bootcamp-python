"""
expense_tracker.py
Project 1: Personal Expense Tracker (Day 10 — CSV persistence added).
Author: Viraj
Date: 2026-07-11
"""
import csv
import os
from money_utils import format_currency

class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)}"

    def to_dict(self) -> dict:
        """Convert this Expense into a plain dict, ready for csv.DictWriter."""
        return {"category": self.category, "amount": self.amount}


class RecurringExpense(Expense):
    def __init__(self, category: str, amount: int, frequency: str):
        super().__init__(category, amount)
        self.frequency = frequency

    def formatted(self):
        base = super().formatted()
        return f"{base} (repeats {self.frequency})"


DATA_FILE = "projects/expense_tracker/data/expenses.csv"


def save_expenses(expenses: list, filepath: str = DATA_FILE) -> None:
    """Write all expenses to a CSV file, overwriting whatever was there."""
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "amount"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense.to_dict())


def load_expenses(filepath: str = DATA_FILE) -> list:
    """Load expenses from a CSV file. Return an empty list if the file doesn't exist yet."""
    if not os.path.exists(filepath):
        return []

    expenses = []
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(Expense(row["category"], int(row["amount"])))
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

    if not amount_input.isdigit():
        print("Invalid amount. Please enter numbers only.")
        return

    amount = int(amount_input)
    expense = Expense(category, amount)
    expenses.append(expense)
    print(f" Added: {expense.formatted()}")


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
    expenses = load_expenses() # in-memory for now, becomes a CSV file once we hit File Handling

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
"""
expense_tracker.py
Project 1: Personal Expense Tracker (Day 6 — return instead of print for totals).
Author: Viraj
Date: 2026-07-11
"""
from money_utils import format_currency

class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)}"


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
    expenses = []  # in-memory for now, becomes a CSV file once we hit File Handling

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
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
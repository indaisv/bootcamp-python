"""
expense_tracker.py
Project 1: Personal Expense Tracker (Day 5 — in-memory version).
Author: Viraj
Date: 2026-07-10
"""


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
    """
    Ask the user for a category and amount, append it to expenses.
    expenses is a list of dicts: {"category": str, "amount": int}
    """
    category = input("Category (Food/Travel/Bills/Other): ").strip().title()
    amount_input = input("Amount (INR): ").strip()          # ← was "amount", now matches below

    if not amount_input.isdigit():
        print("Invalid amount. Please enter numbers only.")
        return

    amount = int(amount_input)
    expenses.append({"category": category, "amount": amount})
    print(f"Added: {category} - INR{amount}")


def view_expenses(expenses: list) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['category']}: INR{expense['amount']}")
    
    
def total_by_category(expenses: list) -> None:
    totals = {}                                    # step 1: init, empty dict this time
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        totals[category] = totals.get(category, 0) + amount   # step 2: update

    for category, total in totals.items():          # step 3: print after the loop
        print(f"{category}: INR{total}")


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
            total_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
            
if __name__ == "__main__":
    main()
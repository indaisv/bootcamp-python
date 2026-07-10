"""
day6_functions.py
Practicing return vs print, default arguments, and scope.
Author: Viraj
"""


def calculate_total(expenses: list) -> int:
    """Return the sum of all expense amounts. Do NOT print inside this function."""
    
    total = sum(e["amount"] for e in expenses)
    return total


def calculate_average(expenses: list) -> float:
    """Return the average expense amount. Handle the empty-list case (avoid ZeroDivisionError)."""
    if not expenses:
        return 0
    total = calculate_total(expenses)
    average = total/ len(expenses)
    return average

def add_item_safe(item, collection=None) -> list:
    """Demonstrate the mutable default argument fix. Append item, return the list."""
    # YOUR CODE — use the `if collection is None:` pattern from Lesson 1
    if collection is None:
        collection = []
    collection.append(item)
    return collection

def main():
    expenses = [
        {"category": "Food", "amount": 500},
        {"category": "Travel", "amount": 1200},
        {"category": "Bills", "amount": 300},
    ]

    total = calculate_total(expenses)
    average = calculate_average(expenses)
    print(f"Total: INR{total}")
    print(f"Average: INR{average:.2f}")

    cart = add_item_safe("apple")
    cart = add_item_safe("banana", cart)
    print(cart)


if __name__ == "__main__":
    main()
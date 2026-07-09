"""
day5_loops.py
Practicing for/while loops and control flow.
Author: Viraj
"""


def loop_practice():
    """Practice for loops, enumerate, zip, and control flow."""
    expenses = [500, 1200, 300, 4500, 150, 800]
    categories = ["Food", "Travel", "Bills", "Rent", "Food", "Entertainment"]

    # 1. Use enumerate() to print each expense with its position, starting at 1
    
    for i, amount in enumerate(expenses, start= 1):
        print(f"{i}. Rupees{amount}")
    #    e.g. "1. Rupees500"

    # 2. Use zip(expenses, categories) to print "Food: Rupees500" style pairs
    
    for category, amount in zip(categories, expenses):
        print(f"{category}: Rupees{amount}")

    # 3. Use a for loop + if to sum only expenses > 1000, print the total

    total_high = 0
    for amount in expenses:
        if amount > 1000:
            total_high = total_high + amount
    print(f"Total > Rupees1000: Rupees{total_high}")
    
    # 4. Use continue to skip any expense that equals exactly 300, print the rest
    
    for amount in expenses:
        if amount == 300:
            continue
        print(amount)
    

    # 5. Use a while True + break loop that keeps asking
    #    "Add another expense? (y/n): " until the user types "n"
    
    while True:
        answer = input("Add another expense? (y/n): ").strip().lower()
        if answer == "n":
            break
        else:
            print("Adding expense.....")

if __name__ == "__main__":
    loop_practice()
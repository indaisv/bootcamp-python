"""
day8_classes.py
Practicing class, __init__, self, and methods.
Author: Viraj
"""


class Expense:
    def __init__ (self, category: str, amount: int):
        # YOUR CODE: set self.category and self.amount
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        """Return a string like 'Food: INR500.00'."""
        # YOUR CODE: use an f-string with self.category and self.amount
        # (plain f-string is fine here, no need to import money_utils for this warm-up)
        return f"{self.category}: {self.amount}"


def main():
    e1 = Expense("Food", 500)
    e2 = Expense("Travel", 1200)

    print(e1.category)
    print(e1.amount)
    print(e1.formatted())
    print(e2.formatted())


if __name__ == "__main__":
    main()
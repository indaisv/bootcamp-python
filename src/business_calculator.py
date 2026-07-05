"""
business_calculator.py

Real business calculations using Python.
Author: Viraj
Date: 2026-07-01
"""

import math

def calculate_discount_price(original_price: float, discount_percent: float) -> float:
    """
    Calculate the final price after a discount.

    Args:
        original_price: The original price before discount.
        discount_percent: Discount percentage (e.g., 15 for 15%).

    Returns:
        The final price after discount.
    """
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price

def split_bill(total: float, people: int) -> float:
    """
    Split a bill evenly among people.

    Args:
        total: Total bill amount.
        people: Number of people.

    Returns:
        Amount each person pays (rounded to 2 decimal places).
    """
    per_person = total/people
    return round(per_person, 2)


def calculate_emi(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate monthly EMI for a loan.

    Formula: EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    Where:
        P = principal
        r = monthly interest rate = annual_rate / 12
        n = total months = years * 12

    Args:
        principal: Loan amount.
        annual_rate: Annual interest rate as decimal (e.g., 0.10 for 10%).
        years: Number of years.

    Returns:
        Monthly EMI amount (rounded to 2 decimal places).
    """
    r = annual_rate / 12
    n = years * 12
    numerator = principal * r * math.pow(1 + r, n)
    denominator = math.pow(1 + r, n) - 1
    EMI = numerator / denominator
    return round(EMI, 2)
def main() -> None:
    """Run all business calculations."""
    print("=" * 50)
    print("BUSINESS CALCULATOR")
    print("=" * 50)

    # Scenario 1: Discount
    original_price = 2500.00
    discount = 15
    final = calculate_discount_price(original_price, discount)
    print(f"Original Price: Rs.{original_price:,.2f}")
    print(f"Discount: {discount}%")
    print(f"Final Price: Rs.{final:,.2f}")
    print()

    # Scenario 2: Split Bill
    bill = 3470.00
    people = 4
    share = split_bill(bill, people)
    print(f"Total Bill: Rs.{bill:,.2f}")
    print(f"People: {people}")
    print(f"Each pays: Rs.{share:,.2f}")
    print()

    # Scenario 3: EMI
    loan = 500000
    rate = 0.10
    years = 5
    emi = calculate_emi(loan, rate, years)
    print(f"Loan Amount: Rs.{loan:,.2f}")
    print(f"Interest Rate: {rate:.1%}")
    print(f"Duration: {years} years")
    print(f"Monthly EMI: Rs.{emi:,.2f}")
    print()

    print("=" * 50)

if __name__ == "__main__":
    main()
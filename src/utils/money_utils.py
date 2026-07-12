"""
money_utils.py

Shared currency formatting used across the bootcamp project.
Author: Viraj
"""


def format_currency(amount: float) -> str:
    """
    Format a number as an INR currency string.

    Args:
        amount: The numeric amount.

    Returns:
        A string like "INR1,234.56".
    """
    return f"INR{amount:,.2f}"
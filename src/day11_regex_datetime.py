"""
day11_regex_datetime.py
Practicing regex validation and datetime formatting.
Author: Viraj
"""
import re
from datetime import datetime


def is_valid_amount(text: str) -> bool:
    """Return True if text is digits, optionally with 1-2 decimal places."""
    # TODO: write the regex pattern and use re.fullmatch()
    pattern = r"^\d+(\.\d{1,2})?$"
    return re.fullmatch(pattern, text) is not None

def is_valid_category(text: str) -> bool:
    """
    Return True if text is 2-20 letters only (no digits, no symbols, no spaces).
    Hint: character class for letters is [A-Za-z]
    """
    # TODO
    pattern = r"^[A-Za-z]{2,20}$"
    return re.fullmatch(pattern, text) is not None

def extract_numbers(text: str) -> list:
    r"""
    Given a messy string like "Spent 450 on food, 120 on travel",
    return all numbers found as a list of strings: ['450', '120']
    Hint: re.findall() with \d+
    """
    # TODO
    pattern = r"\d+"
    return re.findall(pattern, text)

def get_today_string() -> str:
    """Return today's date formatted as YYYY-MM-DD."""
    # TODO: use datetime.now() + strftime
    today = datetime.now()
    return today.strftime("%Y-%m-%d")


def days_between(date1_str: str, date2_str: str) -> int:
    """
    Given two date strings in YYYY-MM-DD format, return the number of days between them.
    Hint: strptime both, subtract the two datetime objects (gives a timedelta), use .days
    """
    # TODO
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    delta = date2 - date1
    return delta.days   

def test_all():
    """Test everything above."""
    print(is_valid_amount("450.50"))    # True
    print(is_valid_amount("abc"))       # False
    print(is_valid_category("Food"))    # True
    print(is_valid_category("Food123")) # False
    print(extract_numbers("Spent 450 on food, 120 on travel"))  # ['450', '120']
    print(get_today_string())           # e.g. "2026-07-18"
    print(days_between("2026-07-01", "2026-07-18"))  # 17


if __name__ == "__main__":
    test_all()
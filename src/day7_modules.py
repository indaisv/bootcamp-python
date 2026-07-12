"""
day7_modules.py
Practicing imports with a custom module.
Author: Viraj
"""

from utils.money_utils import format_currency


def main():
    print(format_currency(500))
    print(format_currency(1234.5))
    print(format_currency(99))


if __name__ == "__main__":
    main()
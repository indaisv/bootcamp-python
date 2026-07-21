"""
test_day11_regex_datetime.py
First pytest tests — validating Day 11's regex/datetime functions.
"""
import pytest
from day11_regex_datetime import is_valid_amount, is_valid_category, extract_numbers, days_between


def test_is_valid_amount_accepts_whole_number():
    # TODO: assert is_valid_amount("450") is True
    assert is_valid_amount("450") == True


def test_is_valid_amount_accepts_two_decimals():
    # TODO: assert is_valid_amount("450.50") is True
    assert is_valid_amount("450.50") == True


def test_is_valid_amount_rejects_letters():
    # TODO: assert is_valid_amount("abc") is False
    assert is_valid_amount("abc") == False


def test_is_valid_amount_rejects_three_decimals():
    # TODO: what should is_valid_amount("450.505") return? Assert it.
    assert is_valid_amount("450.505") == False


def test_is_valid_category_accepts_letters_only():
    # TODO: assert is_valid_category("Food") is True
    assert is_valid_category("Food") == True


def test_is_valid_category_rejects_numbers():
    # TODO: assert is_valid_category("Food123") is False
    assert is_valid_category("Food123") == False


def test_extract_numbers_finds_all_matches():
    # TODO: assert extract_numbers("Spent 450 on food, 120 on travel") == ["450", "120"]
    assert extract_numbers("Spent 450 on food, 120 on travel") == ["450", "120"]


def test_days_between_calculates_correctly():
    # TODO: assert days_between("2026-07-01", "2026-07-18") == 17
    assert days_between("2026-07-01", "2026-07-18") == 17
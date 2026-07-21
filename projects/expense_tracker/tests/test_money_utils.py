from money_utils import format_currency

def test_format_currency_basic():
    assert format_currency(500) == "INR500.00"

def test_format_currency_with_decimals():
    assert format_currency(1234.5) == "INR1,234.50"
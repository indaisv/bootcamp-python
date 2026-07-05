"""
invoice_formatter.py

Format a professional business invoice.
Author: Viraj
Date: 2026-07-01
"""

def format_invoice(customer: str, items: list, tax_rate: float = 0.18) -> None:
    """
    Print a formatted invoice.

    Args:
        customer: Customer name.
        items: List of tuples (item_name, quantity, unit_price).
        tax_rate: Tax rate as decimal (default 0.18 for 18% GST).
    """
    print("=" * 60)
    print(f"{'INVOICE':^60}")
    print(f"{'Customer: ' + customer:>60}")
    print("=" * 60)
    print(f"{'Item':<25} {'Qty':>8} {'Price':>12} {'Total':>12}")
    print("-" * 60)

    subtotal = 0.0

    for item_name, qty, price in items:
        line_total = qty * price
        subtotal += line_total
        print(f"{item_name:<25} {qty:>8} {price:>12.2f} {line_total:>12.2f}")

    print("-" * 60)

    tax_amount = subtotal * tax_rate
    grand_total = subtotal + tax_amount

    print(f"{'Subtotal:':>48} {subtotal:>10.2f}")
    print(f"{'Tax:':>48} {tax_amount:>10.2f}")
    print(f"{'Total:':>48} {grand_total:>10.2f}")

    print("=" * 60)
    print(f"{'Thank you for your business!':^60}")
    print("=" * 60)

if __name__ == "__main__":
    items = [
        ("Laptop Dell Inspiron", 2, 45000.00),
        ("Wireless Mouse", 5, 800.00),
        ("Mechanical Keyboard", 3, 1500.00),
    ]
    format_invoice("Viraj Enterprises", items)
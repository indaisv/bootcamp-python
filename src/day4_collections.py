"""
day4_collections.py
Working with lists, tuples, sets, and dictionaries.
Author: Viraj
Date: 2026-07-01
"""

def analyze_sales():
    """Analyze sales data using lists."""
    sales = [12000, 15000, 8000, 21000, 9500, 18000, 7500]

    total = sum(sales)
    average = total / len(sales)
    max_sale = max(sales)
    min_sale = min(sales)
    sales.sort(reverse=True)
    high_sales = [s for s in sales if s > 10000]

    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {max_sale}")
    print(f"Lowest: {min_sale}")
    print(f"Sorted: {sales}")
    print(f"High Sales (>10000): {high_sales}")
    print(f"Count: {len(high_sales)}")

def deduplicate_emails():
    """Remove duplicate emails using sets."""
    raw_emails = [
        "viraj@gmail.com",
        "alice@yahoo.com",
        "viraj@gmail.com",
        "bob@example.com",
        "alice@yahoo.com",
        "charlie@gmail.com",
    ]

    unique_emails = set(raw_emails)
    sorted_emails = sorted(unique_emails)
    print(f"Unique emails: {sorted_emails}")

def build_customer_database():
    """Build a customer database using dictionaries."""
    customers = [
        {"name": "Viraj", "email": "viraj@gmail.com", "city": "Mumbai", "orders": 5},
        {"name": "Alice", "email": "alice@yahoo.com", "city": "Delhi", "orders": 12},
        {"name": "Bob", "email": "bob@example.com", "city": "Mumbai", "orders": 3},
        {"name": "Charlie", "email": "charlie@gmail.com", "city": "Bangalore", "orders": 8},
    ]

    names = [c["name"] for c in customers]
    print(f"Names: {",".join(names)}")
    
     # 2. Find customer with most orders
    top_customer = customers[0]         # Start with first customer
    for c in customers:                 # Check every customer
        if c["orders"] > top_customer["orders"]:  # If this customer has more orders
            top_customer = c              # Update top_customer
    print(f"Top customer: {top_customer['name']} ({top_customer['orders']} orders)")

    
    mumbai_customers = [c["name"] for c in customers if c["city"] == "Mumbai"]
    print(f"Mumbai customers: {', '.join(mumbai_customers)}")
    
    total_orders = sum(c["orders"] for c in customers)
    print(f"Total orders: {total_orders}")
    
    
def main():
    """Run all exercises."""
    print("=" * 50)
    print("SALES ANALYSIS")
    print("=" * 50)
    analyze_sales()

    print("\n" + "=" * 50)
    print("EMAIL DEDUPLICATION")
    print("=" * 50)
    deduplicate_emails()

    print("\n" + "=" * 50)
    print("CUSTOMER DATABASE")
    print("=" * 50)
    build_customer_database()

if __name__ == "__main__":
    main()
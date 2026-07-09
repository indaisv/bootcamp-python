# Week 1, Day 4: Lists, Tuples, Sets, and Dictionaries

> **Learning Objectives:**
> 1. Understand the 4 core Python data structures and when to use each.
> 2. Master list operations: create, index, slice, append, insert, remove, sort, reverse.
> 3. Understand why tuples exist and when to use them over lists.
> 4. Use sets for deduplication and membership testing.
> 5. Use dictionaries for key-value data (the most common business data structure).
> 6. Avoid the mutable trap with nested lists and dictionaries.
> 7. Iterate over collections with `for` loops.
> 8. Build a customer database using dictionaries.

---

## Business Motivation

Every real-world application stores collections of data. As a data analyst and automation engineer, you will work with:

- **Lists:** Rows of sales data, product names, email addresses.
- **Tuples:** Fixed records like coordinates, RGB colors, database rows.
- **Sets:** Unique customer IDs, distinct product categories, deduplicated emails.
- **Dictionaries:** Customer profiles, JSON API responses, configuration settings.

**If you don't master these, you cannot build any real business application.**

---

## Lesson 1: Lists — Ordered, Mutable, Duplicates Allowed

### Creating and Accessing Lists

```python
# A list of sales amounts
sales = [12000, 15000, 8000, 21000, 9500]

# A list of product names
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

# Mixed types (not recommended but possible)
mixed = ["Viraj", 23, True, 50000.0]

# Access by index
print(products[0])   # "Laptop"
print(products[-1])  # "Monitor" — last item

# Length
print(len(sales))    # 5
```

### Modifying Lists

```python
products = ["Laptop", "Mouse", "Keyboard"]

# Append — add to the end
products.append("Monitor")
print(products)  # ["Laptop", "Mouse", "Keyboard", "Monitor"]

# Insert — add at a specific position
products.insert(1, "Tablet")  # Insert at index 1
print(products)  # ["Laptop", "Tablet", "Mouse", "Keyboard", "Monitor"]

# Remove — remove by value
products.remove("Mouse")  # Removes first occurrence of "Mouse"
print(products)  # ["Laptop", "Tablet", "Keyboard", "Monitor"]

# Pop — remove by index and return it
last_item = products.pop()      # Removes last item
first_item = products.pop(0)    # Removes item at index 0

# Sort — sorts in place
sales = [12000, 15000, 8000, 21000]
sales.sort()                    # [8000, 12000, 15000, 21000]
sales.sort(reverse=True)        # [21000, 15000, 12000, 8000]

# Reverse — reverses in place
products.reverse()
```

**Important:** `sort()` and `reverse()` modify the list in place. They return `None`.

```python
# Wrong — this does nothing useful
result = sales.sort()  # result is None!

# Right — sort first, then use the list
sales.sort()
print(sales)  # Now it's sorted
```

### List Slicing (Same as String Slicing)

```python
sales = [12000, 15000, 8000, 21000, 9500]

print(sales[0:3])   # [12000, 15000, 8000]
print(sales[:3])    # Same as above
print(sales[2:])    # [8000, 21000, 9500]
print(sales[-2:])   # [21000, 9500] — last 2
print(sales[::2])   # [12000, 8000, 9500] — every 2nd
print(sales[::-1])  # [9500, 21000, 8000, 15000, 12000] — reversed
```

### Checking Membership

```python
products = ["Laptop", "Mouse", "Keyboard"]

print("Mouse" in products)     # True
print("Tablet" in products)     # False
print("Phone" not in products)  # True
```

### List Comprehensions (Powerful One-Liners)

```python
prices = [100, 200, 300, 400]

# Double every price
doubled = [p * 2 for p in prices]        # [200, 400, 600, 800]

# Filter: only prices > 150
high_prices = [p for p in prices if p > 150]  # [200, 300, 400]

# Filter + transform
 taxed = [p * 1.18 for p in prices if p > 150]  # [236.0, 354.0, 472.0]
```

**Every Python developer uses list comprehensions.** They are faster and cleaner than loops.

---

## Lesson 2: Tuples — Immutable, Ordered, Faster

A tuple is like a list that **cannot be changed** after creation.

```python
# Creating tuples
coordinates = (19.0760, 72.8777)  # Mumbai latitude, longitude
color = (255, 0, 0)                  # RGB red

# Accessing — same as lists
print(coordinates[0])  # 19.0760
print(coordinates[-1]) # 72.8777

# Tuples are immutable — this will ERROR
coordinates[0] = 20.0  # TypeError!
```

### Why Use Tuples?

| Feature | List | Tuple |
|---------|------|-------|
| Mutable? | Yes | No |
| Speed | Slower | Faster |
| Memory | More | Less |
| Use as dictionary key? | No | Yes |
| Safe from accidental modification? | No | Yes |

**Use tuples when:**
- Data should never change (coordinates, dates, database records).
- You want to use it as a dictionary key.
- You need maximum performance.

**Unpacking tuples:**
```python
coordinates = (19.0760, 72.8777)
lat, lon = coordinates  # lat = 19.0760, lon = 72.8777
```

---

## Lesson 3: Sets — Unordered, No Duplicates, Fast Lookup

A set is a collection of **unique** items with **no order**.

```python
# Creating sets
emails = {"viraj@gmail.com", "alice@yahoo.com", "viraj@gmail.com"}
print(emails)  # {"viraj@gmail.com", "alice@yahoo.com"} — duplicates removed!

# From a list (deduplication)
raw_ids = [100, 200, 100, 300, 200, 400]
unique_ids = set(raw_ids)  # {100, 200, 300, 400}
```

### Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union — all items from both
print(a | b)  # {1, 2, 3, 4, 5, 6}

# Intersection — items in both
print(a & b)  # {3, 4}

# Difference — items in a but not in b
print(a - b)  # {1, 2}

# Symmetric difference — items in either but not both
print(a ^ b)  # {1, 2, 5, 6}
```

**Business use:**
- Deduplicate customer email lists.
- Find common customers between two stores.
- Check if a user ID exists in a whitelist.

```python
# Fast membership check (O(1) vs O(n) for lists)
whitelist = {100, 200, 300, 400}
print(250 in whitelist)  # False — instant check!
```

---

## Lesson 4: Dictionaries — Key-Value Pairs (The Most Important)

A dictionary stores data as **keys** and **values**. Think of it as a real dictionary: word (key) → definition (value).

```python
# Creating a dictionary
customer = {
    "name": "Viraj",
    "email": "viraj@example.com",
    "age": 23,
    "city": "Mumbai",
    "is_active": True,
}

# Accessing values
print(customer["name"])   # "Viraj"
print(customer["email"])  # "viraj@example.com"

# Using get() — safer (returns None if key doesn't exist)
print(customer.get("phone"))        # None — key doesn't exist, no error!
print(customer.get("phone", "N/A"))  # "N/A" — default value

# Modifying
customer["age"] = 24                    # Update existing key
customer["phone"] = "9876543210"        # Add new key

# Removing
del customer["is_active"]               # Remove a key
phone = customer.pop("phone", None)     # Remove and return value

# Checking membership (checks keys only)
print("email" in customer)      # True
print("viraj@example.com" in customer)  # False — checks KEYS, not values!
```

### Dictionary Methods

```python
customer = {"name": "Viraj", "age": 23, "city": "Mumbai"}

# Keys, values, items
print(customer.keys())    # dict_keys(['name', 'age', 'city'])
print(customer.values())  # dict_values(['Viraj', 23, 'Mumbai'])
print(customer.items())   # dict_items([('name', 'Viraj'), ...])

# Iterating
for key in customer:
    print(f"{key}: {customer[key]}")

# Better way — iterate over items
for key, value in customer.items():
    print(f"{key}: {value}")
```

### Nested Dictionaries (Real-World Data)

```python
customer = {
    "name": "Viraj",
    "address": {
        "street": "123 Main St",
        "city": "Mumbai",
        "pincode": "400001",
    },
    "orders": [
        {"id": "ORD001", "amount": 15000},
        {"id": "ORD002", "amount": 8000},
    ],
}

print(customer["address"]["city"])        # "Mumbai"
print(customer["orders"][0]["amount"])  # 15000
```

**This is exactly how JSON data from APIs looks.** You will parse this daily.

---

## Lesson 5: The Mutable Trap (Again, But Deeper)

You learned this with lists. Now see it with nested structures.

```python
# Shallow copy — only copies the outer layer
import copy

original = [
    {"name": "Viraj", "age": 23},
    {"name": "Alice", "age": 25},
]

# Dangerous — same reference
alias = original
alias[0]["age"] = 24
print(original[0]["age"])  # 24 — changed too!

# Shallow copy — still shares inner objects
shallow = original.copy()  # or list(original) or original[:]
shallow[0]["age"] = 25
print(original[0]["age"])  # 25 — still changed!

# Deep copy — completely independent
deep = copy.deepcopy(original)
deep[0]["age"] = 26
print(original[0]["age"])  # 25 — NOT changed! Safe!
```

**Rule:** For simple lists of primitives, `.copy()` is fine. For nested structures (lists of dicts, dicts of lists), always use `copy.deepcopy()`.

---

## Lesson 6: When to Use Which Data Structure

| Scenario | Use | Why |
|----------|-----|-----|
| List of sales amounts | **List** | Ordered, mutable, need indexing |
| Fixed coordinates | **Tuple** | Immutable, prevents accidental change |
| Remove duplicate emails | **Set** | Automatic deduplication, fast lookup |
| Customer profile (name, email, age) | **Dictionary** | Key-value pairs, fast lookup by name |
| JSON API response | **Dictionary** | JSON maps directly to Python dicts |
| Database row | **Tuple** | Immutable record, hashable |

---

## Common Beginner Mistakes (Day 4)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| `list.append()` returns `None` | `append()` modifies in place | `my_list.append(item)` then `print(my_list)` |
| `my_list = my_list.sort()` | `sort()` returns `None` | `my_list.sort()` then use `my_list` |
| `tuple[0] = 5` | Tuples are immutable | Use a list if you need to change it |
| `dict["key"]` when key doesn't exist | Raises `KeyError` | Use `dict.get("key", default)` |
| `set` preserves order | Sets are unordered | Use a list if order matters |
| `list = [[1,2], [3,4]]; copy = list.copy()` | Shallow copy shares inner lists | Use `copy.deepcopy()` for nested |

---

## Best Practices (Day 4)

1. **Use `get()` for dictionary access.** Never trust that a key exists.
2. **Use list comprehensions.** They are faster and more Pythonic.
3. **Use tuples for fixed data.** It signals to other engineers: "Do not modify this."
4. **Use sets for deduplication.** One line: `unique = set(my_list)`.
5. **Use `deepcopy()` for nested structures.** The shallow copy trap gets everyone.
6. **Use `in` for membership checks.** `if item in my_list:` is clean and readable.

---

## Exercises

### Exercise 4.1: Sales Data Analysis

Create `src/day4_collections.py`:

```python
"""
day4_collections.py
Working with lists, tuples, sets, and dictionaries.
Author: Viraj
Date: 2026-07-01
"""


def analyze_sales():
    """Analyze sales data using lists."""
    sales = [12000, 15000, 8000, 21000, 9500, 18000, 7500]

    # YOUR CODE:
    # 1. Calculate total sales (sum of all values)
    # 2. Calculate average sales (total / count)
    # 3. Find the highest and lowest sale
    # 4. Sort sales in descending order
    # 5. Print sales > 10000 using list comprehension
    # 6. Print how many sales were > 10000

    # Hints:
    # total = sum(sales)
    # average = total / len(sales)
    # max_sale = max(sales)
    # min_sale = min(sales)
    # sales.sort(reverse=True)
    # high_sales = [s for s in sales if s > 10000]

    pass


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

    # YOUR CODE:
    # 1. Convert to a set to remove duplicates
    # 2. Convert back to a sorted list
    # 3. Print the unique emails

    pass


def build_customer_database():
    """Build a customer database using dictionaries."""
    customers = [
        {"name": "Viraj", "email": "viraj@gmail.com", "city": "Mumbai", "orders": 5},
        {"name": "Alice", "email": "alice@yahoo.com", "city": "Delhi", "orders": 12},
        {"name": "Bob", "email": "bob@example.com", "city": "Mumbai", "orders": 3},
        {"name": "Charlie", "email": "charlie@gmail.com", "city": "Bangalore", "orders": 8},
    ]

    # YOUR CODE:
    # 1. Print all customer names
    # 2. Find the customer with the most orders
    # 3. Print all customers from Mumbai
    # 4. Print total orders across all customers

    pass


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
```

**Complete the three functions. Expected outputs:**

```
==================================================
SALES ANALYSIS
==================================================
Total: 81000
Average: 11571.43
Highest: 21000
Lowest: 7500
Sorted: [21000, 18000, 15000, 12000, 9500, 8000, 7500]
High Sales (>10000): [12000, 15000, 21000, 18000]
Count: 4

==================================================
EMAIL DEDUPLICATION
==================================================
Unique emails: ['alice@yahoo.com', 'bob@example.com', 'charlie@gmail.com', 'viraj@gmail.com']

==================================================
CUSTOMER DATABASE
==================================================
Names: Viraj, Alice, Bob, Charlie
Top customer: Alice (12 orders)
Mumbai customers: Viraj, Bob
Total orders: 28
```

---

## Interview Questions (Day 4 Level)

1. What is the difference between a list and a tuple? When would you use each?
2. What is a set? Why would you use it over a list?
3. What is a dictionary? How do you access a value safely?
4. What does `list comprehension` do? Why is it better than a `for` loop?
5. What happens if you do `my_list = my_list.sort()`?
6. How do you remove duplicates from a list?
7. What is the difference between a shallow copy and a deep copy?
8. How do you iterate over a dictionary's keys and values?

---

## Resume Relevance

**What you can put on your resume after Day 4:**

> "Built a sales analysis tool and customer database in Python using lists, dictionaries, and sets. Implemented data deduplication, filtering, and aggregation for real business datasets."

---

## Next Lesson Preview (Day 5)

**Topic:** Loops and Control Flow — The Professional Way

**What you will learn:**
- `for` loops with `range()`, `enumerate()`, `zip()`
- `while` loops with proper exit conditions
- `if/elif/else` chains for business logic
- `break`, `continue`, `pass`
- Building a menu-driven application

---

## ✅ Day 4 Checklist

- [ ] `day4_collections.py` created and runs without errors.
- [ ] `analyze_sales()` completed — all 6 tasks work.
- [ ] `deduplicate_emails()` completed — duplicates removed, sorted.
- [ ] `build_customer_database()` completed — names, top customer, Mumbai filter, total orders.
- [ ] Code committed to Git with descriptive message.
- [ ] Pushed to GitHub (`git push`).
- [ ] I can answer all 8 interview questions.

---

**When you are done, tell me: "Day 4 complete."**

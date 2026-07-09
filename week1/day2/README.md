# Week 1, Day 2: Variables, Data Types, and Operators — The Professional Way

> **Learning Objectives:**
> 1. Understand what a variable REALLY is in Python (not what you learned in college).
> 2. Master all 5 core data types: `int`, `float`, `str`, `bool`, `None`.
> 3. Learn the difference between `==` and `is` — a question that gets asked in **every** Python interview.
> 4. Understand mutable vs immutable types — the #1 source of bugs in Python.
> 5. Use the `math` module for real business calculations.
> 6. Format currency and percentages for business reports.
> 7. Type cast correctly and know when to use it.
> 8. Avoid the 5 most common beginner mistakes that get you rejected in interviews.

---

## Business Motivation

Every data analyst and automation engineer works with numbers, text, and decisions. You will:
- Calculate invoice totals (`float` arithmetic).
- Clean customer names (`str` methods).
- Decide if a transaction is valid (`bool` logic).
- Check if data is missing (`None` handling).
- Format currency for dashboards (`f-strings`).

If you don't understand how Python stores and manipulates data, you will write code that:
- Loses money due to floating-point rounding errors.
- Corrupts data by modifying shared lists.
- Fails silently because `==` and `is` behave differently.

**Companies will test you on these basics in technical interviews.** Even senior developers get tripped up by `==` vs `is`.

---

## Lesson 1: What Is a Variable? (The Truth)

### What You Learned in College (Wrong)
> "A variable is a box that stores data."

**This is a lie.** Python does not work this way.

### What Actually Happens in Python

A variable is a **label** (a name tag) attached to an **object** in memory.

**Analogy:** Imagine a balloon (the object) floating in the air. You tie a string to it with a name tag. The name tag is the variable. The balloon is the actual data.

```python
name = "Viraj"
```

What Python does:
1. Creates a string object `"Viraj"` somewhere in memory.
2. Creates a label `name` that points to that object.

**Critical:** The variable `name` does NOT contain the string. It **points to** the string.

### Why This Matters — The `id()` Function

Every object in Python has a unique memory address. You can see it with `id()`.

```python
a = 100
b = a

print(id(a))  # 140735893619024
print(id(b))  # 140735893619024  ← SAME address!
```

`a` and `b` are **two labels pointing to the same object.**

This is why this happens:
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  ← a changed too!
```

**Both `a` and `b` point to the SAME list.** Modify one, you modify the other.

This is the #1 source of bugs in Python. We will cover mutable vs immutable soon.

### Exercise 2.1

In your `src/` folder, create a new file: `day2_variables.py`

Type this and run it. Observe the output:

```python
"""
day2_variables.py

Understanding variables as labels, not boxes.
"""


def demonstrate_variables():
    """Show how Python variables work under the hood."""
    a = 100
    b = a

    print(f"a = {a}, b = {b}")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")
    print(f"Are they the same object? {a is b}")

    # Now change b
    b = 200
    print(f"\nAfter b = 200:")
    print(f"a = {a}, b = {b}")
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")
    print(f"Are they the same object? {a is b}")


if __name__ == "__main__":
    demonstrate_variables()
```

**Question:** Why does `a` stay `100` even after `b = 200`? Think about it. I will explain after you run it.

---

## Lesson 2: The 5 Core Data Types

### Type 1: `int` — Integers

Whole numbers. No decimals.

```python
age = 23
salary = 50000
employees = 150
```

**Key fact:** Python `int` has NO size limit. You can store numbers with millions of digits.

```python
huge_number = 10 ** 1000  # 1 followed by 1000 zeros
print(huge_number)  # Works fine!
```

**Business use:** Employee counts, transaction IDs, invoice numbers, years.

---

### Type 2: `float` — Floating-Point Numbers

Numbers with decimals.

```python
price = 49.99
tax_rate = 0.18
exchange_rate = 83.45
```

**⚠️ DANGER — The Float Trap:**

```python
print(0.1 + 0.2)  # 0.30000000000000004  ← NOT 0.3!
```

**Why?** Computers store floats in binary. `0.1` in decimal is an infinite repeating fraction in binary. Tiny rounding errors accumulate.

**Business impact:** If you calculate `0.1 + 0.2 == 0.3`, you get `False`. This breaks payment systems, tax calculations, and financial reports.

**The fix:** Use `round()` or the `decimal` module for money.

```python
# For simple cases, use round()
total = round(0.1 + 0.2, 2)  # 0.3

# For serious financial calculations, use Decimal (we'll cover this later)
```

**Business use:** Prices, tax rates, percentages, exchange rates, weights.

---

### Type 3: `str` — Strings

Text. Surrounded by single quotes, double quotes, or triple quotes.

```python
name = "Viraj"
email = 'viraj@example.com'
address = """123 Main Street
Mumbai, Maharashtra 400001"""
```

**Key rule:** Single and double quotes are the same in Python. Use whichever you prefer, but be consistent.

**Multi-line strings:** Use triple quotes for multi-line text (like docstrings, email templates, or addresses).

**Business use:** Customer names, emails, addresses, product descriptions, report titles, SQL queries.

---

### Type 4: `bool` — Booleans

Only two values: `True` and `False`.

```python
is_active = True
is_verified = False
has_discount = True
```

**Key rule:** In Python, these values are considered `False`:
- `False` (the boolean)
- `0` (integer zero)
- `0.0` (float zero)
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)
- `None`

Everything else is `True`.

```python
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))    # False
print(bool("hi"))   # True
print(bool([]))    # False
print(bool([1]))   # True
```

**Business use:** Is the customer active? Is the transaction valid? Is the report ready? Should we send the email?

---

### Type 5: `None` — The Absence of Value

`None` means "nothing." It is Python's version of "null" or "empty."

```python
result = None  # "I don't have a result yet."
```

**Common mistake:** Checking `None` with `==` instead of `is`.

```python
# Wrong (works but not recommended)
if result == None:
    pass

# Right (Python standard)
if result is None:
    pass
```

**Why `is`?** Because `None` is a singleton — there is only ONE `None` object in all of Python. `is` checks identity, which is faster and more correct.

**Business use:** Missing data, optional function arguments, default values, initialization before processing.

---

### How to Check Types

Use `type()` to see what type something is:

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
```

Use `isinstance()` to check if something IS a specific type (preferred in real code):

```python
age = 25
print(isinstance(age, int))      # True
print(isinstance(age, str))      # False
print(isinstance(age, (int, float)))  # True  — checks multiple types
```

**Why `isinstance()` is better than `type()`:**
- `type()` is rigid. It checks the EXACT type.
- `isinstance()` respects inheritance. If you have a custom number type that inherits from `int`, `isinstance(x, int)` will return `True`, but `type(x) == int` will return `False`.
- Every company uses `isinstance()` for type checking.

---

### Exercise 2.2: Type Detective

Add this to `day2_variables.py`:

```python
def type_detective():
    """Investigate data types and isinstance."""
    data = [
        42,
        3.14,
        "hello",
        True,
        None,
        [1, 2, 3],
        {"name": "Viraj"},
    ]

    for item in data:
        print(f"Value: {item!r:20} | type: {type(item).__name__:10} | isinstance(item, str): {isinstance(item, str)}")
```

Add `type_detective()` to your `if __name__ == "__main__":` block and run it.

**Question:** What is `{item!r}` doing? (Hint: `!r` means "use repr() for this.") What is the difference between `str()` and `repr()`? Think about it.

---

## Lesson 3: The `==` vs `is` Trap

This is asked in **every single Python interview.** Understand it now.

| Operator | What It Checks | Use Case |
|----------|---------------|----------|
| `==` | **Value equality** — Do two objects have the same value? | "Are these two numbers equal?" |
| `is` | **Identity** — Are two variables pointing to the SAME object in memory? | "Is this variable `None`?" |

### Example 1: Numbers

```python
a = 1000
b = 1000

print(a == b)   # True  — same value
print(a is b)   # False — different objects in memory!
```

**Why is `a is b` False?** Because Python created two separate integer objects. They happen to have the same value, but they live at different memory addresses.

### Example 2: Small Integers (Python Optimization)

```python
a = 5
b = 5

print(a == b)   # True
print(a is b)   # True  ← WAIT, WHY?
```

**Python caches small integers (-5 to 256).** It creates them once and reuses them. So `5` is a single object, and both `a` and `b` point to it.

**This is an implementation detail, not a guarantee.** Never rely on `is` for value comparison.

### Example 3: Strings

```python
a = "hello"
b = "hello"

print(a == b)   # True
print(a is b)   # True  — Python also caches short strings!

# But:
c = "hello world this is a very long string that python will not cache"
d = "hello world this is a very long string that python will not cache"
print(c == d)   # True
print(c is d)   # False!
```

### The Rule

> **Always use `==` for value comparison.**  
> **Only use `is` for checking `None` or singleton objects.**

**Interview question:** "What is the difference between `==` and `is` in Python?"

**Your answer:** "`==` checks if two objects have the same value. `is` checks if two variables point to the exact same object in memory. I use `==` for comparing values, and `is` only for checking `None` because `None` is a singleton."

---

### Exercise 2.3: Equality vs Identity

Add this to `day2_variables.py`:

```python
def equality_vs_identity():
    """Demonstrate the critical difference between == and is."""
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
    print()
    print(f"a == b: {a == b}")   # True — same values
    print(f"a is b: {a is b}")   # False — different objects
    print(f"a == c: {a == c}")   # True — same values
    print(f"a is c: {a is c}")   # True — SAME object!
    print()
    print(f"id(a) = {id(a)}")
    print(f"id(b) = {id(b)}")
    print(f"id(c) = {id(c)}")
```

Run it. Study the output until you can explain every line to yourself.

---

## Lesson 4: Mutable vs Immutable — The #1 Source of Bugs

### What Does "Mutable" Mean?

**Mutable** = Can be changed after creation.  
**Immutable** = Cannot be changed after creation.

| Type | Mutable? | Why It Matters |
|------|----------|----------------|
| `int` | ❌ Immutable | `x = 5; x += 1` creates a NEW object, doesn't modify `5` |
| `float` | ❌ Immutable | Same as int |
| `str` | ❌ Immutable | `name.upper()` returns a NEW string, doesn't modify the original |
| `bool` | ❌ Immutable | Only two objects: `True` and `False` |
| `None` | ❌ Immutable | Only one object: `None` |
| `list` | ✅ Mutable | `my_list.append(4)` modifies the list in place |
| `dict` | ✅ Mutable | `my_dict["key"] = "value"` modifies the dictionary |
| `tuple` | ❌ Immutable | Cannot add, remove, or change elements after creation |
| `set` | ✅ Mutable | `my_set.add(5)` modifies the set in place |

### The Bug That Gets You Fired

```python
def add_tax(items, tax_rate=0.18):
    """Add tax to each item price."""
    for i in range(len(items)):
        items[i] = items[i] * (1 + tax_rate)
    return items


prices = [100, 200, 300]
result = add_tax(prices)
print(result)    # [118.0, 236.0, 354.0] — correct
print(prices)    # [118.0, 236.0, 354.0] — WAIT, THE ORIGINAL CHANGED TOO!
```

**What happened?** `items` and `prices` point to the SAME list. When you modify `items`, you modify `prices`.

**The fix:** Never modify a mutable argument in place. Create a copy.

```python
def add_tax(items, tax_rate=0.18):
    """Add tax to each item price — safely."""
    return [price * (1 + tax_rate) for price in items]

# OR if you must modify in place:
def add_tax(items, tax_rate=0.18):
    items_copy = items.copy()  # Create a shallow copy
    for i in range(len(items_copy)):
        items_copy[i] = items_copy[i] * (1 + tax_rate)
    return items_copy
```

### String Immutability

```python
name = "viraj"
name.upper()        # Returns "VIRAJ" but does NOT modify 'name'
print(name)         # "viraj" — unchanged!

name = name.upper()  # You must reassign to change the variable
print(name)          # "VIRAJ"
```

**Why are strings immutable?** For performance and safety. Immutable objects can be shared freely without risk of modification. Python caches them aggressively.

---

### Exercise 2.4: Mutable vs Immutable Challenge

Add this to `day2_variables.py`:

```python
def mutable_trap():
    """Demonstrate the mutable trap and how to avoid it."""
    original = [1, 2, 3]

    # Dangerous: both point to the same list
    alias = original
    alias.append(4)
    print(f"After alias.append(4):")
    print(f"original = {original}")   # What do you expect?
    print(f"alias = {alias}")

    # Safe: create a copy
    original2 = [1, 2, 3]
    copy = original2.copy()  # or list(original2) or original2[:]
    copy.append(4)
    print(f"\nAfter copy.append(4):")
    print(f"original2 = {original2}")  # What do you expect?
    print(f"copy = {copy}")


def string_immutable():
    """Show that strings are immutable."""
    greeting = "hello"
    print(f"Original: {greeting}")
    print(f"greeting.upper() returns: {greeting.upper()}")
    print(f"After upper(): {greeting}")  # Still "hello"!

    greeting = greeting.upper()  # Reassign to update
    print(f"After reassignment: {greeting}")
```

Run these functions and verify your understanding.

---

## Lesson 5: Operators — The Complete Set

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `5 / 3` | `1.666...` |
| `//` | Floor Division | `5 // 3` | `1` |
| `%` | Modulo (remainder) | `5 % 3` | `2` |
| `**` | Exponentiation | `2 ** 3` | `8` |

**Key differences:**

```python
print(5 / 2)    # 2.5  — always returns float
print(5 // 2)   # 2    — returns int, rounds DOWN
print(5 % 2)    # 1    — remainder after division
print(10 % 3)   # 1    — 10 = 3*3 + 1
```

**Business use of modulo:**
- Is a number even? `num % 2 == 0`
- Distribute items into groups: `items_per_group = total // groups`
- Find remaining items: `remaining = total % groups`

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `5 == 5` → `True` |
| `!=` | Not equal to | `5 != 3` → `True` |
| `<` | Less than | `5 < 3` → `False` |
| `>` | Greater than | `5 > 3` → `True` |
| `<=` | Less than or equal | `5 <= 5` → `True` |
| `>=` | Greater than or equal | `5 >= 3` → `True` |

**Chain comparisons (Python feature):**
```python
x = 15
print(10 < x < 20)  # True — Python reads this as (10 < x) and (x < 20)
```

### Logical Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `and` | Both must be True | `True and False` → `False` |
| `or` | At least one must be True | `True or False` → `True` |
| `not` | Invert the boolean | `not True` → `False` |

**Short-circuit evaluation:**
```python
# In 'and', if the first is False, Python stops immediately
print(False and expensive_function())  # expensive_function() is NEVER called!

# In 'or', if the first is True, Python stops immediately
print(True or expensive_function())    # expensive_function() is NEVER called!
```

**Business use:**
```python
# Approve a loan only if BOTH conditions are met
if credit_score >= 700 and income >= 50000:
    approve_loan()

# Send a discount if EITHER condition is met
if is_first_time_customer or total_spent > 10000:
    apply_discount()
```

### Assignment Operators

```python
x = 10       # Basic assignment
x += 5       # x = x + 5  → 15
x -= 3       # x = x - 3  → 12
x *= 2       # x = x * 2  → 24
x /= 4       # x = x / 4  → 6.0
x //= 2      # x = x // 2 → 3.0
x %= 2       # x = x % 2  → 1.0
x **= 3      # x = x ** 3 → 1.0
```

---

## Lesson 6: Type Casting — Converting Between Types

You already did this with `int(birth_year_input)`. This is called **type casting** (or type conversion).

| Function | Converts to | Example | Result |
|----------|-------------|---------|--------|
| `int()` | Integer | `int("42")` | `42` |
| `float()` | Float | `float("3.14")` | `3.14` |
| `str()` | String | `str(42)` | `"42"` |
| `bool()` | Boolean | `bool(1)` | `True` |
| `list()` | List | `list("abc")` | `['a', 'b', 'c']` |

**Common errors:**

```python
int("3.14")    # ERROR! Cannot convert a string with decimal directly to int
int(3.14)      # OK → 3 (truncates decimal)
float("3.14")  # OK → 3.14
int("hello")   # ERROR! Cannot convert text to int
```

**The safe way to convert user input:**

```python
def get_positive_number(prompt: str) -> float:
    """Safely get a positive number from the user."""
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


price = get_positive_number("Enter the price: ")
```

**Why this is professional:**
- It handles bad input gracefully (no crashes).
- It validates the number is positive (business logic).
- It loops until the user provides valid input.
- It has a clear docstring and type hints.

---

## Lesson 7: The `math` Module — Business Calculations

Python's `math` module has functions for real-world calculations.

```python
import math

# Rounding
print(math.ceil(4.2))    # 5  — round UP to nearest integer
print(math.floor(4.8))   # 4  — round DOWN to nearest integer
print(round(4.5))        # 4  — banker's rounding (to nearest even)
print(round(4.5001))     # 5

# Finance
print(math.pow(2, 3))    # 8.0  — 2 raised to power 3
print(math.sqrt(16))     # 4.0  — square root

# Statistics (we'll use numpy later, but math has basics)
numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
print(f"Mean: {mean}")   # 30.0

# Constants
print(math.pi)           # 3.141592653589793
print(math.e)            # 2.718281828459045
```

**Business example: Compound Interest**

```python
import math


def compound_interest(principal: float, rate: float, years: int) -> float:
    """
    Calculate compound interest: A = P * (1 + r)^t

    Args:
        principal: Initial investment amount.
        rate: Annual interest rate as a decimal (e.g., 0.08 for 8%).
        years: Number of years.

    Returns:
        Final amount after compound interest.
    """
    return principal * math.pow(1 + rate, years)


# Example: Invest ₹10,000 at 8% for 5 years
final_amount = compound_interest(10000, 0.08, 5)
print(f"Final amount: ₹{final_amount:.2f}")
# ₹14693.28
```

---

### Exercise 2.5: Business Calculator

Add this to `day2_variables.py`:

```python
import math


def business_calculator():
    """Practice with math operators for real business scenarios."""
    # Scenario 1: Calculate discount price
    original_price = 2500.00
    discount_percent = 15
    # YOUR CODE: Calculate final price after discount

    # Scenario 2: Split a bill among people
    total_bill = 3470.00
    people = 4
    # YOUR CODE: Calculate each person's share (rounded to 2 decimal places)

    # Scenario 3: Calculate monthly EMI
    # EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    # P = principal, r = monthly rate, n = number of months
    loan_amount = 500000
    annual_rate = 0.10
    years = 5
    # YOUR CODE: Calculate and print the monthly EMI

    # Print all results with 2 decimal places and ₹ symbol
```

**Complete the three scenarios.** Use `math.pow()`, division, and rounding. Format the output with `:.2f`.

---

## Lesson 8: String Formatting for Business Reports

### f-Strings (The Modern Way)

```python
name = "Viraj"
sales = 125000.50
percentage = 0.235

print(f"Salesperson: {name}")
print(f"Total Sales: ₹{sales:,.2f}")       # ₹125,000.50
print(f"Growth Rate: {percentage:.1%}")   # 23.5%
print(f"ID: {123:06d}")                    # 000123
```

**Formatting codes:**
| Code | Meaning | Example |
|------|---------|---------|
| `:.2f` | 2 decimal places | `3.14159` → `3.14` |
| `:,` | Thousands separator | `1000000` → `1,000,000` |
| `:.1%` | Percentage | `0.235` → `23.5%` |
| `:>10` | Right-align, 10 chars | `"hi"` → `"        hi"` |
| `:<10` | Left-align, 10 chars | `"hi"` → `"hi        "` |
| `:^10` | Center, 10 chars | `"hi"` → `"    hi    "` |
| `:06d` | Pad with zeros, 6 digits | `123` → `000123` |

**Business report example:**

```python
def print_sales_report(salesperson: str, revenue: float, target: float) -> None:
    """Print a formatted sales report line."""
    achievement = revenue / target
    status = "MET TARGET" if revenue >= target else "BELOW TARGET"

    print(f"{'Salesperson:':<15} {salesperson:>20}")
    print(f"{'Revenue:':<15} ₹{revenue:>18,.2f}")
    print(f"{'Target:':<15} ₹{target:>18,.2f}")
    print(f"{'Achievement:':<15} {achievement:>18.1%}")
    print(f"{'Status:':<15} {status:>20}")


print_sales_report("Viraj", 1250000.50, 1000000.00)
```

Output:
```
Salesperson:                  Viraj
Revenue:           ₹1,250,000.50
Target:            ₹1,000,000.00
Achievement:                 125.0%
Status:                 MET TARGET
```

---

### Exercise 2.6: Invoice Formatter

Create a new file: `src/invoice_formatter.py`

```python
"""
invoice_formatter.py

Format a professional invoice using f-strings.
"""


def format_invoice(customer: str, items: list, tax_rate: float = 0.18) -> None:
    """
    Print a formatted invoice.

    Args:
        customer: Customer name.
        items: List of tuples (item_name, quantity, unit_price).
        tax_rate: Tax rate as a decimal (default 0.18 for 18% GST).
    """
    # YOUR CODE:
    # 1. Print a header with the customer name
    # 2. Print each item with quantity, unit price, and line total
    # 3. Calculate subtotal, tax amount, and grand total
    # 4. Print all amounts aligned to the right with ₹ symbol and 2 decimal places
    # 5. Use at least 3 different formatting codes
    pass


if __name__ == "__main__":
    items = [
        ("Laptop", 2, 45000.00),
        ("Mouse", 5, 800.00),
        ("Keyboard", 3, 1500.00),
    ]
    format_invoice("Viraj Enterprises", items)
```

**Complete the function.** The output should look professional — like a real invoice you would see in a business.

---

## Common Beginner Mistakes (Day 2)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| `0.1 + 0.2 == 0.3` returns `False` | Float precision | Use `round()` or `Decimal` |
| `a = b` for lists, then `b.append()` modifies `a` | Mutable alias | Use `.copy()` or create new list |
| `x = x + 1` on a string | Strings are immutable | `x += "1"` works, but understand it's creating a new string |
| `if x == None` | Using `==` for `None` | Always use `if x is None` |
| `input()` without `int()` conversion | Forgetting type casting | `age = int(input("Age: "))` |
| `int("3.14")` crashes | Converting float string to int directly | `int(float("3.14"))` or `int(3.14)` |
| `True + True` equals `2` | Booleans are subclass of int | Don't use booleans in arithmetic |
| `="*" * 50` forgetting it's a string | Confusing string repetition | `"=" * 50` creates a string of 50 equals signs |

---

## Best Practices (Day 2)

1. **Use `isinstance()` for type checking, not `type()`.**
2. **Use `is None`, not `== None`.**
3. **Use `==` for value comparison, `is` for identity.**
4. **Never modify mutable arguments in place.** Create copies.
5. **Use `round()` for float display, but `Decimal` for financial calculations.**
6. **Use f-strings with formatting codes for business output.**
7. **Validate and cast user input immediately.** Never trust what the user types.
8. **Use descriptive variable names.** `price` is better than `p`. `total_revenue` is better than `tr`.

---

## Mini Exercise Summary (Complete Before Day 3)

| Exercise | File | What to Do |
|----------|------|------------|
| 2.1 | `day2_variables.py` | Run `demonstrate_variables()` and explain why `a` stays `100` |
| 2.2 | `day2_variables.py` | Run `type_detective()` and understand `isinstance()` |
| 2.3 | `day2_variables.py` | Run `equality_vs_identity()` and explain every output |
| 2.4 | `day2_variables.py` | Run `mutable_trap()` and `string_immutable()` |
| 2.5 | `day2_variables.py` | Complete the business calculator scenarios |
| 2.6 | `invoice_formatter.py` | Create a professional invoice formatter |

---

## Challenge Question (Think About It)

**What will this print? Why?**

```python
a = [1, 2, 3]
b = a[:]
c = list(a)
d = a.copy()

print(a is b, a is c, a is d)
print(a == b, a == c, a == d)

b.append(4)
print(a)  # What is a now?
```

**Answer this BEFORE moving to Day 3.**

---

## Interview Questions (Day 2 Level)

1. What is the difference between `==` and `is`? When do you use each?
2. What are mutable and immutable types in Python? Give examples.
3. Why does `0.1 + 0.2 != 0.3`? How do you fix it?
4. What happens when you do `a = [1, 2, 3]` and `b = a`? What is `b`?
5. Why do we use `is None` instead of `== None`?
6. What is the output of `bool(0)`, `bool(1)`, `bool("")`, `bool("hello")`?
7. How do you safely convert a string to an integer?
8. What is the difference between `type()` and `isinstance()`?

---

## Resume Relevance

**What you can put on your resume after Day 2:**

> "Demonstrated deep understanding of Python memory model, mutable vs immutable data types, and the `==` vs `is` distinction. Built business calculation tools with the `math` module and professional string formatting for invoice generation."

---

## Next Lesson Preview (Day 3)

**Topic:** Strings — The Professional Way

**What you will learn:**
- String methods (`strip()`, `split()`, `join()`, `replace()`, `find()`)
- String slicing (the most powerful Python feature)
- Regex basics (matching patterns in text)
- Reading and cleaning real business data (customer names, emails, phone numbers)
- Building a data cleaning utility

---

## ✅ Day 2 Checklist

Before you tell me "Day 2 complete," confirm EACH of these:

- [ ] `day2_variables.py` created and runs without errors.
- [ ] Exercise 2.1 completed and I can explain why `a` stays `100`.
- [ ] Exercise 2.2 completed — I understand `type()` and `isinstance()`.
- [ ] Exercise 2.3 completed — I can explain `==` vs `is` with examples.
- [ ] Exercise 2.4 completed — I understand mutable vs immutable.
- [ ] Exercise 2.5 completed — Business calculator works correctly.
- [ ] Exercise 2.6 completed — Invoice formatter looks professional.
- [ ] Challenge question answered correctly.
- [ ] Code committed to Git with descriptive message.
- [ ] I can answer all 8 interview questions.

---

**When you are done, tell me: "Day 2 complete." I will review your code and quiz you before moving to Day 3.**

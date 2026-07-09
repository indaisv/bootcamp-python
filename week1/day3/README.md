# Week 1, Day 3: Strings — The Professional Way

> **Learning Objectives:**
> 1. Master string methods: `strip()`, `split()`, `join()`, `replace()`, `find()`, `upper()`, `lower()`, `title()`, `startswith()`, `endswith()`.
> 2. Understand string slicing — the most powerful Python feature for text.
> 3. Clean real business data: messy customer names, emails, phone numbers.
> 4. Use `len()`, indexing, and negative indexing.
> 5. Build a data cleaning utility for a real-world dataset.
> 6. Explain why strings are immutable and what that means in practice.

---

## Business Motivation

Every data analyst and automation engineer spends **40% of their time cleaning text data.** Real business data is messy:

- Customer names: `"  viraj  INDais  "` → needs to become `"Viraj Indais"`
- Emails: `"Viraj.Indais@GMAIL.COM"` → needs to become `"viraj.indais@gmail.com"`
- Phone numbers: `"+91-98765-43210"` → needs to become `"9876543210"`
- Addresses: `"123, Main Street, Mumbai, 400001"` → needs to split into parts
- Product codes: `"PRD-12345-XYZ"` → needs to extract `12345`

**Today you will build a data cleaning utility.** This is a real tool that every data team uses.

---

## Lesson 1: String Basics (Quick Review)

### Creating Strings

```python
name = "Viraj"              # Double quotes
email = 'viraj@example.com' # Single quotes — same thing
template = """              # Triple quotes — for multi-line
Dear {name},
Your order has been shipped.
"""
```

**Rule:** Single and double quotes are identical in Python. Use whichever is easier for your text. If your text contains `'`, use `"`. If it contains `"`, use `'`.

### Escape Characters

```python
quote = "He said, \"Hello!\""  # \" puts a double quote inside double quotes
path = "C:\\Users\\Viraj"       # \\ puts a backslash
newline = "Line 1\nLine 2"      # \n creates a new line
```

**Raw strings** (ignore escapes): `r"C:\Users\Viraj"` → useful for file paths and regex.

### String Length and Indexing

```python
name = "Viraj"
print(len(name))     # 5 — number of characters
print(name[0])       # V — first character
print(name[1])       # i — second character
print(name[-1])      # j — last character (negative index)
print(name[-2])      # a — second to last
```

**Index positions:**
```
V  i  r  a  j
0  1  2  3  4
-5 -4 -3 -2 -1
```

---

## Lesson 2: String Slicing — The Most Powerful Python Feature

**Slicing** means extracting a part of a string using `[start:end:step]`.

| Syntax | Meaning | Example |
|--------|---------|---------|
| `[0:3]` | Characters from index 0 UP TO (not including) 3 | `"Viraj"[0:3]` → `"Vir"` |
| `[:3]` | Same as `[0:3]` — start from beginning | `"Viraj"[:3]` → `"Vir"` |
| `[2:]` | From index 2 to the end | `"Viraj"[2:]` → `"raj"` |
| `[-3:]` | Last 3 characters | `"Viraj"[-3:]` → `"raj"` |
| `[::2]` | Every 2nd character | `"Viraj"[::2]` → `"Vrj"` |
| `[::-1]` | Reverse the string | `"Viraj"[::-1]` → `"jariV"` |

**The most important rule:** `start` is INCLUDED. `end` is EXCLUDED.

```python
text = "abcdef"
print(text[0:3])   # "abc" — index 0, 1, 2 (3 is NOT included)
print(text[2:5])   # "cde" — index 2, 3, 4 (5 is NOT included)
```

### Business Examples

```python
# Extract date parts from "2026-07-01"
date = "2026-07-01"
year = date[:4]      # "2026"
month = date[5:7]    # "07"
day = date[8:]       # "01"

# Extract product code from "PRD-12345-XYZ"
code = "PRD-12345-XYZ"
product_id = code[4:9]  # "12345"

# Extract domain from email
email = "viraj@example.com"
at_index = email.find("@")
domain = email[at_index + 1:]  # "example.com"

# Reverse a transaction ID
txn = "TXN12345"
reversed_txn = txn[::-1]  # "54321NXT"
```

---

### Exercise 3.1: Slicing Practice

Create `src/day3_strings.py` and add this:

```python
"""
day3_strings.py
Mastering string slicing and methods.
Author: Viraj
Date: 2026-07-01
"""


def slicing_practice():
    """Practice string slicing with real data."""
    # Extract year, month, day from this date string
    date_str = "2026-07-15"
    # YOUR CODE: year = ?, month = ?, day = ?

    # Extract the phone number without country code
    phone = "+91-98765-43210"
    # YOUR CODE: phone_without_code = ?

    # Extract first name from "Viraj_Indais_123"
    username = "Viraj_Indais_123"
    # YOUR CODE: first_name = ?

    # Reverse this transaction ID
    txn_id = "TXN-2026-78432"
    # YOUR CODE: reversed_txn = ?

    # Print all results
    print(f"Year: {year}")
    print(f"Month: {month}")
    print(f"Day: {day}")
    print(f"Phone without code: {phone_without_code}")
    print(f"First name: {first_name}")
    print(f"Reversed TXN: {reversed_txn}")


if __name__ == "__main__":
    slicing_practice()
```

**Fill in the YOUR CODE sections. Run it. Expected output:**
```
Year: 2026
Month: 07
Day: 15
Phone without code: 98765-43210
First name: Viraj
Reversed TXN: 23487-6202-NXT
```

---

## Lesson 3: String Methods — The Toolkit

### Cleaning Methods

```python
text = "  Viraj  INDais  "
print(text.strip())       # "Viraj  INDais" — removes leading/trailing spaces
print(text.lstrip())      # "Viraj  INDais  " — removes leading spaces only
print(text.rstrip())      # "  Viraj  INDais" — removes trailing spaces only
```

### Case Methods

```python
name = "viraj indais"
print(name.upper())       # "VIRAJ INDAIS"
print(name.lower())       # "viraj indais"
print(name.title())       # "Viraj Indais" — Capitalizes Each Word
print(name.capitalize())  # "Viraj indais" — Only first letter capitalized
```

**Business use:** `title()` is perfect for customer names. `lower()` is perfect for email comparison.

### Finding and Replacing

```python
email = "viraj.indais@example.com"
print(email.find("@"))       # 14 — index of @ sign, or -1 if not found
print(email.find("z"))       # -1 — not found
print(email.replace("@", " AT "))  # "viraj.indais AT example.com"
print(email.replace(".", "_"))     # "viraj_indais@example_com"
```

**`find()` returns `-1` if the substring is NOT found.** Always check for `-1` before using the index.

### Splitting and Joining

```python
# Split a string into parts
csv_line = "Viraj,Indais,viraj@example.com,Mumbai"
parts = csv_line.split(",")
print(parts)  # ['Viraj', 'Indais', 'viraj@example.com', 'Mumbai']

# Split with max splits
info = "Name: Viraj | Age: 23 | City: Mumbai"
pairs = info.split(" | ")
print(pairs)  # ['Name: Viraj', 'Age: 23', 'City: Mumbai']

# Join parts back together
words = ["Hello", "World", "Python"]
sentence = " ".join(words)  # "Hello World Python"
print(sentence)

# Join with custom separator
ids = ["100", "200", "300"]
csv = ",".join(ids)  # "100,200,300"
print(csv)
```

**Business use:** `split(",")` is how you read CSV files. `split(" | ")` is how you parse log files. `" ".join(words)` is how you build sentences from lists.

### Checking Methods

```python
email = "viraj@example.com"
print(email.startswith("viraj"))   # True
print(email.endswith(".com"))       # True
print(email.islower())              # True
print(email.isdigit())              # False
print("12345".isdigit())            # True
```

**Business use:** `isdigit()` validates phone numbers. `endswith(".com")` checks email domains. `startswith("TXN")` validates transaction IDs.

---

### Exercise 3.2: Data Cleaning Utility

Add this to `day3_strings.py`:

```python
def clean_customer_data(raw_name: str, raw_email: str, raw_phone: str) -> dict:
    """
    Clean messy customer data.

    Args:
        raw_name: Name with extra spaces and wrong case.
        raw_email: Email with possible uppercase and spaces.
        raw_phone: Phone with country code and dashes.

    Returns:
        Dictionary with cleaned name, email, phone.
    """
    # Clean name: strip spaces, title case
    # Example: "  viraj  INDais  " -> "Viraj Indais"
    cleaned_name = raw_name.strip().title()

    # Clean email: strip spaces, lowercase
    cleaned_email = raw_email.strip().lower()

    # Clean phone: remove country code and dashes
    # Example: "+91-98765-43210" -> "9876543210"
    # Hint: use .replace() twice or .split("-")
    cleaned_phone = raw_phone.replace("+91-", "").replace("-", "")

    return {
        "name": cleaned_name,
        "email": cleaned_email,
        "phone": cleaned_phone,
    }


def test_data_cleaning():
    """Test the data cleaning utility."""
    raw_data = [
        ("  viraj  INDais  ", "Viraj.Indais@GMAIL.COM", "+91-98765-43210"),
        ("ALICE  smith", " alice@Yahoo.com ", "+91-87654-32109"),
        ("  BOB JONES  ", "BOB@EXAMPLE.COM", "+91-76543-21098"),
    ]

    for raw_name, raw_email, raw_phone in raw_data:
        cleaned = clean_customer_data(raw_name, raw_email, raw_phone)
        print(f"Raw:    {raw_name!r} | {raw_email!r} | {raw_phone!r}")
        print(f"Clean:  {cleaned['name']!r} | {cleaned['email']!r} | {cleaned['phone']!r}")
        print()
```

Update `if __name__` to call `test_data_cleaning()` after `slicing_practice()`. Run it. Expected output should show clean, professional data.

---

## Lesson 4: String Immutability — Why You Must Reassign

Strings are **immutable** — they cannot be changed after creation. Every "modification" creates a new string.

```python
name = "viraj"
name.upper()        # Returns "VIRAJ" but does NOT modify 'name'!
print(name)         # "viraj" — still the same!

name = name.upper()  # You MUST reassign to update the variable
print(name)          # "VIRAJ" — now updated
```

**The mistake:**
```python
# Wrong — this does nothing!
email.strip()  # Returns a new string but throws it away!

# Right — capture the result!
email = email.strip()
```

**Business impact:** Every data cleaning function must return the cleaned result. The caller must capture it.

```python
# WRONG — data stays dirty
clean_customer_data(raw_name, raw_email, raw_phone)

# RIGHT — capture the cleaned result
cleaned = clean_customer_data(raw_name, raw_email, raw_phone)
```

---

## Lesson 5: f-Strings with Expressions (Advanced, Briefly)

You already know f-strings. Here are the advanced features:

```python
price = 2500.50
discount = 15

# Math inside f-string
print(f"Discount: {price * discount / 100:,.2f}")  # "375.08"

# Method calls inside f-string
email = "Viraj@Example.COM"
print(f"Email: {email.lower()}")  # "viraj@example.com"

# Conditional inside f-string
age = 23
print(f"Status: {'Adult' if age >= 18 else 'Minor'}")  # "Adult"
```

**Business use:** Build dynamic email templates, format reports, create log messages.

---

## Common Beginner Mistakes (Day 3)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| `text.upper()` without reassignment | Forgetting strings are immutable | `text = text.upper()` |
| `text.find("@")` returns `-1` | Not checking if substring exists | `if "@" in text:` |
| `text.split()` with no separator | Default splits on whitespace, not commas | `text.split(",")` for CSV |
| `text[5]` on a 5-character string | Index 5 does not exist (indices 0-4) | Check `len(text)` first |
| `text[0:5]` thinking it includes index 5 | End index is EXCLUDED | Remember: start INCLUDED, end EXCLUDED |
| `"hello" + 5` | Cannot add string and number | `"hello" + str(5)` |

---

## Best Practices (Day 3)

1. **Always `strip()` user input.** Users type extra spaces accidentally.
2. **Always `lower()` emails before comparison.** `Gmail.com` and `gmail.com` are the same.
3. **Use `title()` for names.** `"viraj indais"` → `"Viraj Indais"` looks professional.
4. **Use `find()` + check for `-1`.** Never assume a substring exists.
5. **Use `split()` and `join()` for CSV-style data.** It's faster and cleaner than manual parsing.
6. **Reassign after every string method.** `name = name.strip().title()`

---

## Mini Exercise Summary

| Exercise | File | What to Do |
|----------|------|------------|
| 3.1 | `day3_strings.py` | Fill in slicing operations for date, phone, username, reverse |
| 3.2 | `day3_strings.py` | Complete `clean_customer_data()` and test with 3 customers |
| 3.3 (bonus) | `day3_strings.py` | Add a function to validate email format (must contain `@` and `.`) |

---

## Challenge Question

What does this print? Why?

```python
text = "abcdef"
print(text[::2])      # ?
print(text[1::2])     # ?
print(text[::-1])     # ?
print(text[::-2])     # ?
```

---

## Interview Questions (Day 3 Level)

1. What is the difference between `strip()`, `lstrip()`, and `rstrip()`?
2. How do you extract a substring from index 3 to 7? What is included/excluded?
3. What is the output of `"hello"[::-1]`? What does `[::-1]` do?
4. Why must you reassign after `name.upper()`?
5. What does `split(",")` return? What does `" ".join(words)` return?
6. How do you check if a string contains a specific substring?
7. What is the difference between `find()` and `index()`?
8. How do you remove all spaces from a string?

---

## Resume Relevance

**What you can put on your resume after Day 3:**

> "Built a data cleaning utility in Python that standardizes customer names, emails, and phone numbers using string methods, slicing, and validation checks."

---

## Next Lesson Preview (Day 4)

**Topic:** Lists, Tuples, Sets, and Dictionaries

**What you will learn:**
- How to store collections of data
- When to use each data structure
- The mutable trap (again, but deeper)
- Real business data structures: product catalogs, customer databases, order lists

---

## ✅ Day 3 Checklist

- [ ] `day3_strings.py` created and runs without errors.
- [ ] Exercise 3.1 completed — slicing works correctly.
- [ ] Exercise 3.2 completed — data cleaning utility works.
- [ ] (Optional) Exercise 3.3 completed — email validation added.
- [ ] Challenge question answered correctly.
- [ ] Code committed to Git.
- [ ] I can answer all 8 interview questions.

---

**When you are done, tell me: "Day 3 complete."**

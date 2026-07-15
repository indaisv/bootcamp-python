# Week 1, Day 10: File Handling — Reading & Writing Data

> **Learning Objectives:**
> 1. Understand the `with open(...) as f:` pattern and why it matters.
> 2. Read and write plain text files.
> 3. Read and write CSV files using the `csv` module.
> 4. Give the Expense Tracker real persistence — expenses survive after the program closes.

---

## Business Motivation

Every time you've run the Expense Tracker so far, `expenses = []` starts fresh at the top of `main()` — meaning the moment you type option `4` and exit, everything you added is gone. That's fine for practicing loops and functions, but it means the tool isn't actually usable for real life yet.

**Today fixes that permanently.** Expenses get saved to a real file on disk, and loaded back automatically the next time you run the program. This is the single biggest jump in "does this feel like a real app" you'll experience this week.

---

## Lesson 1: `with open(...) as f:` — The Pattern You'll Use Forever

```python
with open("notes.txt", "w") as f:
    f.write("Hello, bootcamp!\n")
```

- **`open(path, mode)`** — opens a file. `mode` tells Python what you intend to do:
  - `"w"` — write (creates the file if it doesn't exist, **overwrites** it completely if it does)
  - `"r"` — read (file must already exist, or this errors)
  - `"a"` — append (adds to the end, doesn't erase existing content)
- **`with ... as f:`** — this is the important part. It guarantees the file gets properly **closed** automatically once you're done with it — even if something goes wrong halfway through. Forgetting to close a file can corrupt data or leave it locked. `with` removes the risk entirely; you never have to remember to call `.close()` yourself.

**Reading it back:**
```python
with open("notes.txt", "r") as f:
    content = f.read()          # whole file as one string

with open("notes.txt", "r") as f:
    for line in f:                 # loop line by line — very common pattern
        print(line.strip())         # .strip() removes the trailing newline
```

---

## Lesson 2: The `csv` Module

You could split lines on commas yourself, but real data gets messy fast — a category name containing a comma would silently break manual parsing. The built-in `csv` module handles this correctly, so use it instead of hand-rolled string splitting.

```python
import csv

# Writing rows
rows = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1200},
]

with open("expenses.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "amount"])
    writer.writeheader()          # writes the column names as the first row
    for row in rows:
        writer.writerow(row)

# Reading rows back
with open("expenses.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)                 # each row comes back as a dict: {"category": "Food", "amount": "500"}
```

**⚠️ Two real gotchas, not optional details:**
1. **`newline=""` in `open()` is required on Windows for CSV files.** Without it, you'll get blank lines between every row. Always include it for CSV — both reading and writing.
2. **Everything read from a CSV comes back as a string**, even the numbers. `row["amount"]` is `"500"` (text), not `500` (int). You must explicitly convert it back: `int(row["amount"])`.

---

## Lesson 3: Wiring This Into the Real Project

**Step 1 — give `Expense` a way to convert itself to a plain dict** (CSV writing needs simple dicts, not objects):

```python
class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)}"

    def to_dict(self) -> dict:
        """Convert this Expense into a plain dict, ready for csv.DictWriter."""
        return {"category": self.category, "amount": self.amount}
```

**Step 2 — a `save_expenses()` function** that writes every expense in the list out to a CSV file:

```python
import csv
import os

DATA_FILE = "projects/expense_tracker/data/expenses.csv"


def save_expenses(expenses: list, filepath: str = DATA_FILE) -> None:
    """Write all expenses to a CSV file, overwriting whatever was there."""
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "amount"])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense.to_dict())
```

**Step 3 — a `load_expenses()` function** that rebuilds `Expense` objects from the CSV, if the file exists:

```python
def load_expenses(filepath: str = DATA_FILE) -> list:
    """Load expenses from a CSV file. Return an empty list if the file doesn't exist yet."""
    if not os.path.exists(filepath):
        return []

    expenses = []
    with open(filepath, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(Expense(row["category"], int(row["amount"])))
    return expenses
```

**Why the `os.path.exists()` check matters:** the very first time you ever run the program, `expenses.csv` won't exist yet — trying to `open()` it in read mode would crash. Checking first and returning an empty list handles that "brand new user, no data yet" case gracefully.

**Step 4 — wire both functions into `main()`:**

```python
def main():
    expenses = load_expenses()        # was: expenses = []

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            totals = total_by_category(expenses)
            if not totals:
                print("No expenses recorded yet.")
            else:
                for category, total in totals.items():
                    print(f"{category}: {format_currency(total)}")
        elif choice == "4":
            save_expenses(expenses)     # NEW — save before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
```

**One small housekeeping note:** your `.gitignore` from Day 1 already excludes `*.csv` files — so `expenses.csv` will never get committed to Git, which is actually correct behavior. Personal financial data shouldn't live in a public repo; only your code should.

---

## Exercise 10.1: Warm-up

Create `src/day10_files.py`:

```python
"""
day10_files.py
Practicing file I/O: plain text and CSV.
Author: Viraj
"""

import csv


def text_file_practice():
    """Write a few lines to a text file, then read them back."""
    lines = ["Line one", "Line two", "Line three"]

    # YOUR CODE: open "practice.txt" in write mode.
    # Loop through `lines` and write each one, adding "\n" after it.

    # YOUR CODE: open "practice.txt" in read mode.
    # Read and print the whole contents.
    pass


def csv_practice():
    """Write a small CSV of expenses, then read it back."""
    rows = [
        {"category": "Food", "amount": 500},
        {"category": "Travel", "amount": 1200},
    ]

    # YOUR CODE: open "practice.csv" in write mode (remember newline="").
    # Use csv.DictWriter with fieldnames=["category", "amount"].
    # Call writeheader(), then write each row.

    # YOUR CODE: open "practice.csv" in read mode (remember newline="").
    # Use csv.DictReader, loop through it, and print each row.
    pass


if __name__ == "__main__":
    text_file_practice()
    print()
    csv_practice()
```

**Expected output:**
```
Line one
Line two
Line three

{'category': 'Food', 'amount': '500'}
{'category': 'Travel', 'amount': '1200'}
```

(Notice `'500'` and `'1200'` print with quotes — proof they came back as strings, exactly the gotcha from Lesson 2.)

---

## Exercise 10.2: Real Persistence for the Expense Tracker

Apply Steps 1-4 from Lesson 3 to your actual `expense_tracker.py`:

1. Add `to_dict()` to the `Expense` class.
2. Add `import csv` and `import os` near the top of the file.
3. Add the `DATA_FILE` constant, `save_expenses()`, and `load_expenses()` functions.
4. Update `main()` — `load_expenses()` at the start, `save_expenses(expenses)` right before the goodbye message on exit.

**Test it properly — this is important, don't skip steps:**
1. Run the program, add 2-3 expenses, then choose option 4 to exit.
2. Check that `projects/expense_tracker/data/expenses.csv` now exists and has your data in it (open it in VS Code to look).
3. **Run the program again.** Immediately choose option 2 (View all expenses) *without adding anything new*. You should see your expenses from last time — proof persistence actually worked.

---

## Common Beginner Mistakes (Day 10)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Blank lines between every row in the CSV | Forgot `newline=""` in `open()` on Windows | Always include `newline=""` when opening a file for `csv` reading/writing |
| `amount` comparisons or math failing after loading from CSV | Forgetting everything from CSV is text | Always `int(row["amount"])` (or `float()`) when reading numeric data back |
| `FileNotFoundError` on first run | Trying to `open()` a file in read mode before it's ever been created | Check `os.path.exists(filepath)` first, return an empty list if it's missing |
| Data doesn't persist between runs | `save_expenses()` never actually gets called | Confirm the save call is inside the `choice == "4"` branch, not somewhere it never executes |
| Overwriting real data with test data while experimenting | `"w"` mode erases the whole file every time | Be deliberate about when you call `save_expenses()` — it's a full overwrite, not an append |

---

## Best Practices (Day 10)

1. **Always use `with open(...) as f:`.** Never call `open()` without it — you risk leaving files unclosed.
2. **Use the `csv` module for CSV data, never manual `.split(",")`.** It correctly handles edge cases manual parsing gets wrong.
3. **Convert types explicitly after reading from a file.** Nothing coming out of a text-based file is ever automatically an `int` or `float`.
4. **Check for file existence before reading**, so a first-time run doesn't crash.

---

## Interview Questions (Day 10 Level)

1. What does the `with` keyword actually guarantee when working with files?
2. What's the difference between `"w"`, `"r"`, and `"a"` file modes?
3. Why is `newline=""` required when opening files for CSV on Windows?
4. Why does `int(row["amount"])` need to happen after reading from a CSV, when the CSV clearly contains numbers?
5. What would happen if `load_expenses()` didn't check `os.path.exists()` first?

---

## Resume Relevance

**What you can put on your resume after Day 10:**

> "Implemented CSV-based data persistence for a Python CLI application, enabling data to reliably survive across program sessions using the `csv` module and safe file-handling patterns."

---

## Next Lesson Preview (Day 11)

**Topic:** Regex & Datetime

**What you will learn:**
- Pattern matching with the `re` module — validating emails, phone numbers, extracting structured data from messy text
- The `datetime` module — timestamping expenses with real dates, not just category/amount

---

## ✅ Day 10 Checklist

- [ ] `day10_files.py` created — Exercise 10.1 complete (text + CSV practice).
- [ ] `Expense.to_dict()` added.
- [ ] `save_expenses()` and `load_expenses()` added to `expense_tracker.py`.
- [ ] `main()` updated — loads on start, saves on exit.
- [ ] Tested properly: added data, exited, re-ran, confirmed data was still there.
- [ ] Code committed to Git (note: `expenses.csv` itself won't be committed — that's correct, thanks to `.gitignore`).
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 10 complete."**

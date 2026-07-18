# Day 10: File Handling — Notes

## 1. Revision Notes

**Core idea:** RAM is temporary (wiped when the program exits), disk is permanent. Any data that must survive between runs (expenses, users, settings) has to be written to a file.

**File modes:**
- `"r"` (read) — file must already exist, or `FileNotFoundError`.
- `"w"` (write) — wipes the file completely the instant it's opened, then writes fresh. Creates the file if missing.
- `"a"` (append) — keeps existing content, adds new content to the end. Creates the file if missing.

**Why `"w"` doesn't lose data in a tracker app:** the program never saves *only* the new item. The pattern is:
1. `load_expenses()` at startup → reads CSV into a Python list in RAM.
2. Every add/edit happens on that in-RAM list only.
3. `save_expenses()` opens in `"w"` mode and rewrites the *entire* list, old + new, from scratch.

So `"w"` wiping the file first is safe — because right before the wipe, the full data set already exists in RAM, ready to be written back whole.

**The `csv` module vs plain `open()`/`write()`:** CSV files are just text with commas, but the `csv` module handles quoting, escaping commas inside values, and reading rows back as dictionaries (`csv.DictReader`/`csv.DictWriter`) instead of manually splitting strings — less error-prone for tabular data.

**OOP + File Handling (the Day 9 wrinkle):** CSV only stores plain text — it has no concept of a Python class. To save `Expense` and `RecurringExpense` objects and load them back as the *correct* class, you need an extra column (e.g. `"type"`) recording which class each row came from, then branch on it during load to reconstruct the right object.

**Data read from a file is always a string.** Even a column that looks like a number (`"450.0"`) comes back as `str` — must be explicitly cast (`float(...)`, `int(...)`) before doing math on it.

---

## 2. Cheat Sheet

```python
import csv
import os

# Writing (overwrites file each time — call with the FULL current list)
with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["category", "amount"])
    writer.writeheader()
    writer.writerows(list_of_dicts)      # or loop + writer.writerow(...)

# Reading
if os.path.exists("data.csv"):
    with open("data.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row["amount"])   # cast! everything is str by default
```

| Mode | Behavior | Missing file |
|------|----------|---------------|
| `"r"` | Read only | Error |
| `"w"` | Wipe + write | Creates it |
| `"a"` | Keep + add to end | Creates it |

- `with open(...) as f:` → auto-closes file even on crash. Always prefer this over manual `f.close()`.
- `newline=""` in `open()` → required on Windows to avoid blank rows in CSV.
- `os.path.exists(path)` → check before reading, avoids `FileNotFoundError` on first run.
- Polymorphic save/load → add a `"type"` column, branch on it when reconstructing objects.

---

## 3. Active Recall Questions

1. What's the difference between what happens to a file's existing content in `"w"` mode vs `"a"` mode?
2. Why is it safe for `save_expenses()` to use `"w"` mode without losing previously saved expenses?
3. What error do you get opening a non-existent file in `"r"` mode, and how do you guard against it?
4. Why does every value read from a CSV file come back as a string, even if it looks like a number?
5. What extra piece of information do you need to store in the CSV so that `load_expenses()` can correctly rebuild a `RecurringExpense` instead of a plain `Expense`?
6. What does `newline=""` in `open()` prevent, and on which OS does it matter?
7. Why is `with open(...) as f:` preferred over manually calling `f.close()`?
8. If you called `open("data.csv", "w")` inside a `for` loop (once per row) instead of once outside the loop, what would go wrong?

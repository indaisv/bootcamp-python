# Week 1, Day 5: Loops & Control Flow — Building Your First Real App

> **Learning Objectives:**
> 1. Master `for` loops: `range()`, `enumerate()`, `zip()`.
> 2. Master `while` loops — especially the `while True` + `break` menu pattern.
> 3. Build clean `if/elif/else` decision chains.
> 4. Use `break`, `continue`, `pass` correctly.
> 5. Build the menu system for **Project 1: Personal Expense Tracker** — in the `expense_tracker` folder you already created.

---

## Business Motivation

Almost every automation script is loops + conditionals wearing a business suit: "for each row, check a condition, do something, otherwise skip it." Today that stops being theory — you build the actual menu loop for your Expense Tracker.

---

## Lesson 1: `for` Loops

### Basic `for`

```python
categories = ["Food", "Travel", "Bills", "Rent"]

for category in categories:
    print(category)
```

### `range()` — looping a fixed number of times

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 — step of 2
    print(i)
```

### `enumerate()` — index + value together

```python
expenses = [500, 1200, 300, 4500]

# Bad — the beginner way
for i in range(len(expenses)):
    print(i, expenses[i])

# Good — the professional way
for i, amount in enumerate(expenses, start=1):
    print(f"{i}. ₹{amount}")
```

**Rule:** if you ever write `range(len(something))`, stop — use `enumerate()`.

### `zip()` — looping two lists together

```python
categories = ["Food", "Travel", "Bills"]
amounts = [500, 1200, 300]

for category, amount in zip(categories, amounts):
    print(f"{category}: ₹{amount}")
```

**Business use:** `enumerate()` numbers rows for display. `zip()` pairs up parallel columns of data (e.g. a CSV where category and amount came from separate lists).

---

## Lesson 2: `while` Loops — The Menu Pattern

### Basic `while` with a counter

```python
count = 0
while count < 5:
    print(count)
    count += 1   # forget this line = infinite loop
```

### The pattern you'll use constantly: `while True` + `break`

```python
while True:
    answer = input("Add another expense? (y/n): ").strip().lower()
    if answer == "n":
        break
    print("Adding expense...")
```

This is how **every menu-driven CLI app** is built — including today's project. You loop forever, and the only way out is an explicit `break` when the user chooses to exit.

**Why not a flag variable instead?**

```python
# Works, but clunkier
running = True
while running:
    choice = input(...)
    if choice == "4":
        running = False
```

Both work. `while True` + `break` is the more common professional pattern because the exit condition lives right where it happens, not split across two places.

---

## Lesson 3: `if/elif/else`, `break`, `continue`, `pass`

### Chains for business logic

```python
amount = 4500

if amount > 5000:
    print("High expense — needs approval")
elif amount > 1000:
    print("Medium expense")
else:
    print("Low expense")
```

### `break` — exit the loop immediately

```python
for expense in [500, 1200, 99999, 300]:
    if expense > 10000:
        print("Suspicious amount found, stopping.")
        break
    print(expense)
```

### `continue` — skip this iteration, keep looping

```python
for expense in [500, 0, 300, -50, 1200]:
    if expense <= 0:
        continue   # skip invalid entries, don't stop the loop
    print(expense)
```

### `pass` — a placeholder that does nothing

```python
def add_expense(expenses):
    pass  # not implemented yet — lets the file run without errors
```

**Difference in one line:** `break` = leave the loop. `continue` = skip to the next round of the *same* loop. `pass` = do nothing, used as a placeholder.

---

## Lesson 4: Project 1 — Expense Tracker Skeleton

You already made the folders:
```
projects/expense_tracker/src/
projects/expense_tracker/data/
projects/expense_tracker/tests/
```

Today's version stores expenses **in memory only** (a list of dicts). We don't have File Handling yet (that's a few days out on the roadmap) — once we cover it, you'll upgrade this exact file to save/load from `data/expenses.csv`. For now the goal is the menu loop itself.

Create `projects/expense_tracker/src/expense_tracker.py`:

```python
"""
expense_tracker.py
Project 1: Personal Expense Tracker (Day 5 — in-memory version).
Author: Viraj
Date: 2026-07-08
"""


def print_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. Exit")


def add_expense(expenses: list) -> None:
    """
    Ask the user for a category and amount, append it to expenses.
    expenses is a list of dicts: {"category": str, "amount": int}
    """
    # YOUR CODE:
    # 1. input() for category -> .strip().title()   (Day 3 skill)
    # 2. input() for amount -> check .isdigit() BEFORE converting to int
    # 3. If not a valid number: print an error message and return (don't crash!)
    # 4. Append {"category": category, "amount": amount} to expenses
    pass


def view_expenses(expenses: list) -> None:
    """Print every expense with a running number, e.g. '1. Food: ₹500'."""
    # YOUR CODE:
    # - Use enumerate(expenses, start=1)
    # - Handle the empty-list case: print "No expenses recorded yet."
    pass


def total_by_category(expenses: list) -> None:
    """Print the total amount spent per category."""
    # YOUR CODE:
    # 1. Build a dict: {category: running_total}
    # 2. Use totals.get(category, 0) + amount   (Day 4 skill)
    # 3. Print each category with its total
    pass


def main():
    """The menu loop — the heart of every CLI tool you'll ever build."""
    expenses = []  # in-memory for now, becomes a CSV file once we hit File Handling

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ").strip()

        # YOUR CODE: if/elif chain
        # "1" -> add_expense(expenses)
        # "2" -> view_expenses(expenses)
        # "3" -> total_by_category(expenses)
        # "4" -> print a goodbye message, then break
        # anything else -> print "Invalid option. Try again."
        pass


if __name__ == "__main__":
    main()
```

**Expected interaction once complete:**
```
========================================
PERSONAL EXPENSE TRACKER
========================================
1. Add expense
2. View all expenses
3. View total by category
4. Exit
Choose an option (1-4): 1
Category (Food/Travel/Bills/Other): food
Amount (INR): 500
Added: Food - ₹500
Choose an option (1-4): 3
Food: ₹500
Choose an option (1-4): 4
Goodbye!
```

---

## Exercise 5.1: Loop Practice (Warm-up)

Create `src/day5_loops.py`:

```python
"""
day5_loops.py
Practicing for/while loops and control flow.
Author: Viraj
"""


def loop_practice():
    """Practice for loops, enumerate, zip, and control flow."""
    expenses = [500, 1200, 300, 4500, 150, 800]
    categories = ["Food", "Travel", "Bills", "Rent", "Food", "Entertainment"]

    # YOUR CODE:
    # 1. Use enumerate() to print each expense with its position, starting at 1
    # 2. Use zip(expenses, categories) to print "Food: ₹500" style pairs
    # 3. Use a for loop + if to sum only expenses > 1000
    # 4. Use continue to skip any expense that equals exactly 300, print the rest
    # 5. Use a while True + break loop that keeps asking
    #    "Add another expense? (y/n): " until the user types "n"
    pass


if __name__ == "__main__":
    loop_practice()
```

Do this one first — it's the syntax rehearsal before you touch the real project.

---

## Common Beginner Mistakes (Day 5)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Forgetting to increment inside `while` | Loop never reaches exit condition | Always update the counter/state before looping again |
| `range(len(list))` | Habit from other languages | Use `enumerate(list)` instead |
| Confusing `break` and `continue` | Both feel like "skip" | `break` exits the loop entirely; `continue` only skips this round |
| Infinite `while True` with no `break` path | Exit condition typo'd or missed | Test the exit path first, before adding features |
| Modifying a list while looping over it | Looks fine, silently skips items | Loop over a copy: `for x in list[:]:` |
| Deep `if/elif` nesting | Copy-pasting conditions | Flatten with early `return`/`continue` where possible |

---

## Best Practices (Day 5)

1. **Use `enumerate()`, never `range(len(...))`.**
2. **`while True` + `break` for menus** — the exit condition sits where the exit happens.
3. **Validate input before converting types** (`isdigit()` before `int()`) — never trust `input()`.
4. **Keep `if/elif` chains flat.** If you're nesting 3+ levels deep, extract a function.
5. **One `break` per intended exit.** Multiple scattered breaks make loops hard to follow.

---

## Challenge Question

What does this print, and why doesn't it skip printing anything for `i == 2`?

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## Interview Questions (Day 5 Level)

1. What's the difference between `for` and `while`? When would you choose each?
2. What does `enumerate()` do, and why is it preferred over `range(len(x))`?
3. What's the difference between `break`, `continue`, and `pass`?
4. How do you avoid an infinite `while` loop?
5. What does `zip()` do when the two lists are different lengths?
6. Why is `while True` + `break` a common pattern for CLI menus?

---

## Resume Relevance

**What you can put on your resume after Day 5:**

> "Built a menu-driven CLI expense tracker in Python using loop control structures and dictionary aggregation for category-wise spend analysis."

---

## Next Lesson Preview (Day 6)

**Topic:** Functions & Scope

**What you will learn:**
- Parameters, default arguments, `*args`/`**kwargs`
- Return values (and why `print()` inside a function isn't the same as `return`)
- Local vs global scope — the mutable default argument trap
- Refactoring today's Expense Tracker functions to be properly testable

---

## ✅ Day 5 Checklist

- [ ] `day5_loops.py` created — Exercise 5.1 complete.
- [ ] `expense_tracker.py` created in `projects/expense_tracker/src/`.
- [ ] Menu loop runs without crashing on invalid input.
- [ ] Add / View / Total by category all work correctly.
- [ ] Challenge question answered correctly.
- [ ] Code committed to Git.
- [ ] I can answer all 6 interview questions.

---

**When you are done, tell me: "Day 5 complete."**

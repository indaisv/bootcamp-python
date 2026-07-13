# Week 1, Day 8: Object-Oriented Programming — Classes & Objects

> **Learning Objectives:**
> 1. Understand why a plain dictionary eventually hits a ceiling for representing real-world things.
> 2. Master `class`, `__init__`, and `self` — the three pieces every class needs.
> 3. Understand the difference between attributes (data) and methods (behavior).
> 4. Refactor the Expense Tracker's `{"category": ..., "amount": ...}` dicts into a real `Expense` class.

---

## Business Motivation

Right now, an expense is a dictionary: `{"category": "Food", "amount": 500}`. That's worked fine so far — but it has real, silent risks that only show up as your project grows:

- **Typos are invisible.** If you write `expense["categroy"]` somewhere by accident, Python doesn't complain — it just creates a *new*, different key. No error, just quietly wrong data.
- **No enforcement.** Nothing stops you from creating `{"category": "Food", "amount": -500}` or `{"amount": 500}` with no category at all. The dict doesn't know what a "valid" expense looks like.
- **Behavior lives far from the data.** The logic for "how do I display this expense nicely" (`format_currency(expense["amount"])`) is scattered wherever it's needed, instead of traveling with the data itself.

**A class fixes all three.** It bundles the data *and* the rules/behavior for that data into one definition, in one place. This is the actual shift from "writing scripts" to "designing software" — the next real level up.

---

## Lesson 1: `class`, `__init__`, and `self` — The Three Pieces

```python
class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount
```

**Breaking this down, piece by piece:**

- **`class Expense:`** — declares a new *blueprint* called `Expense`. Nothing is created yet — this is a template, not an actual expense.
- **`__init__`** — a special method that runs **automatically** every time you create a new `Expense`. Short for "initialize." This is where you set up whatever data the object needs to start with.
- **`self`** — refers to *this specific instance* being created. When you later write `expense1 = Expense("Food", 500)`, `self` inside `__init__` refers to `expense1` specifically. Every method inside a class automatically receives `self` as its first parameter — Python passes it in for you.
- **`self.category = category`** — this is the part that actually "sticks" the data onto the object. Without this line, `category` would just be a local variable that vanishes when `__init__` finishes. `self.category` is what makes it a permanent, retrievable *attribute* of the object.

**Creating (instantiating) objects:**

```python
expense1 = Expense("Food", 500)
expense2 = Expense("Travel", 1200)

print(expense1.category)   # "Food"
print(expense1.amount)     # 500
print(expense2.category)   # "Travel"
```

Each call to `Expense(...)` builds a completely separate object. `expense1` and `expense2` don't share data — changing one doesn't touch the other (same idea as two separate lists, not two labels on the same list, from Day 2).

**Compare directly to the dict version:**
```python
# Dict version — typo-prone, no structure enforced
expense = {"category": "Food", "amount": 500}
expense["categroy"]     # KeyError — but only if you're LUCKY. Otherwise silent bug.

# Class version — Python catches the typo immediately
expense = Expense("Food", 500)
expense.categroy         # AttributeError — Python tells you immediately, this doesn't exist
```

---

## Lesson 2: Methods — Behavior That Travels With the Data

A **method** is just a function defined inside a class. Like `__init__`, it automatically receives `self` — giving it access to that specific object's data.

```python
from money_utils import format_currency


class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        """Return a display-ready string for this expense."""
        return f"{self.category}: {format_currency(self.amount)}"
```

```python
expense1 = Expense("Food", 500)
print(expense1.formatted())   # "Food: INR500.00"
```

**Notice what happened here:** the "how do I display this expense" logic used to live in `view_expenses()`, written out by hand with dictionary lookups. Now it lives *inside* the `Expense` class itself, right next to the data it describes. Any code that has an `Expense` object automatically knows how to display it correctly — no copy-pasted formatting logic scattered around.

---

## Exercise 8.1: Warm-up

Create `src/day8_classes.py`:

```python
"""
day8_classes.py
Practicing class, __init__, self, and methods.
Author: Viraj
"""


class Expense:
    def __init__(self, category: str, amount: int):
        # YOUR CODE: set self.category and self.amount
        pass

    def formatted(self) -> str:
        """Return a string like 'Food: INR500.00'."""
        # YOUR CODE: use an f-string with self.category and self.amount
        # (plain f-string is fine here, no need to import money_utils for this warm-up)
        pass


def main():
    e1 = Expense("Food", 500)
    e2 = Expense("Travel", 1200)

    print(e1.category)
    print(e1.amount)
    print(e1.formatted())
    print(e2.formatted())


if __name__ == "__main__":
    main()
```

**Expected output:**
```
Food
500
Food: INR500.00
Travel: INR1200.00
```

---

## Exercise 8.2: Refactor the Expense Tracker

This is the real one — go into `expense_tracker.py` and switch the whole app from dicts to `Expense` objects.

**Step 1 — add the class** (put this near the top of the file, after the imports):

```python
class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)}"
```

**Step 2 — update `add_expense()`.** Instead of building a dict and appending it, build an `Expense` object and append *that*:

```python
def add_expense(expenses: list) -> None:
    category = input("Category (Food/Travel/Bills/Other): ").strip().title()
    amount_input = input("Amount (INR): ").strip()

    if not amount_input.isdigit():
        print("Invalid amount. Please enter numbers only.")
        return

    amount = int(amount_input)
    expense = Expense(category, amount)      # was: {"category": category, "amount": amount}
    expenses.append(expense)                   # was: expenses.append({...})
    print(f"Added: {expense.formatted()}")
```

**Step 3 — update `view_expenses()`.** Every `expense["category"]` / `expense["amount"]` dictionary lookup becomes `expense.category` / `expense.amount` (dot instead of brackets). Even better — use the `.formatted()` method you just built instead of re-writing the format by hand:

```python
def view_expenses(expenses: list) -> None:
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {______}")    # YOUR CODE: what method call goes here?
```

**Step 4 — update `total_by_category()`.** Same idea — swap dictionary-style access for dot access:

```python
def total_by_category(expenses: list) -> dict:
    totals = {}
    for expense in expenses:
        category = expense.______      # YOUR CODE
        amount = expense.______        # YOUR CODE
        totals[category] = totals.get(category, 0) + amount
    return totals
```

Fill in the two blanks yourself — you already know the attribute names from Step 1.

---

## Common Beginner Mistakes (Day 8)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Forgetting `self` as the first parameter in a method | Feels redundant — "why do I need to pass this?" | Python passes it automatically when you call `obj.method()`, but you must still *declare* it in `def method(self):` |
| Writing `def __init__(self, category, amount): category = category` (forgetting `self.`) | Muscle memory from regular variables | Without `self.`, the value never attaches to the object — it vanishes when `__init__` ends. Always `self.category = category` |
| Calling `Expense.formatted()` without an instance | Confusing the class (blueprint) with an object (built from it) | You need an actual object first: `e = Expense(...)`, then `e.formatted()` |
| Mixing up `expense.category` (object) and `expense["category"]` (dict) mid-refactor | Old habit from before today | After refactoring, an `Expense` is never a dict again — always dot notation |
| `AttributeError: 'Expense' object has no attribute 'categroy'` | Same typo risk as before, just a different error type | This is actually the *fix* working as intended — Python is now telling you immediately instead of staying silent |

---

## Best Practices (Day 8)

1. **A class should represent one clear "thing."** `Expense` represents one expense — it shouldn't also handle menu printing or file saving.
2. **Keep `__init__` simple** — just assign incoming data to `self.attribute`. Complex logic belongs in separate methods.
3. **Methods that describe "how to display this object" belong on the object itself**, not scattered across the functions that use it.
4. **Attribute names should match exactly what you'll type everywhere** — a typo in `self.category` inside `__init__` means every single usage elsewhere breaks too.

---

## Interview Questions (Day 8 Level)

1. What is `self`, and why does every method need it as the first parameter?
2. What's the difference between a class and an object (instance)?
3. What does `__init__` actually do, and when does it run?
4. Give a concrete reason a class is safer than a dictionary for representing structured data.
5. What's the difference between an attribute and a method?

---

## Resume Relevance

**What you can put on your resume after Day 8:**

> "Refactored a Python CLI application from dictionary-based data structures to a proper class-based object model, improving data integrity and encapsulating display logic within the domain object."

---

## Next Lesson Preview (Day 9)

**Topic:** Inheritance & Polymorphism

**What you will learn:**
- Why you'd want one class to "extend" another (e.g. a `RecurringExpense` that's mostly like `Expense`, but with extra behavior)
- `class Child(Parent):` and `super()`
- How polymorphism lets different objects respond to the same method call in their own way

---

## ✅ Day 8 Checklist

- [ ] `day8_classes.py` created — Exercise 8.1 complete.
- [ ] `Expense` class added to `expense_tracker.py`.
- [ ] `add_expense()`, `view_expenses()`, and `total_by_category()` all refactored to use `Expense` objects instead of dicts.
- [ ] Program runs identically to before (same behavior, cleaner internals).
- [ ] Code committed to Git.
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 8 complete."**

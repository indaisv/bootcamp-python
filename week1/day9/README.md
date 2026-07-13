# Week 1, Day 9: Inheritance & Polymorphism

> **Learning Objectives:**
> 1. Understand why you'd want one class to "extend" another instead of copy-pasting it.
> 2. Master `class Child(Parent):` and `super()`.
> 3. Understand method overriding — a child class providing its own version of a parent's method.
> 4. Understand polymorphism — different objects responding to the same method call, each in their own way.
> 5. Add a `RecurringExpense` class that builds on top of `Expense`.

---

## Business Motivation

Your `Expense` class works great for one-time purchases — a coffee, a taxi ride. But real spending includes **recurring** costs too: rent, a Netflix subscription, a gym membership. These need everything `Expense` already has (a category, an amount) *plus* something extra (how often it repeats).

**The tempting-but-wrong move:** copy-paste the whole `Expense` class, rename it `RecurringExpense`, and add the new field. That works today — but now you have the *same* `category`/`amount` logic living in two places. Fix a bug in one, you have to remember to fix it in the other too. That's the exact DRY violation from Day 7, just at the class level instead of the function level.

**Inheritance is the fix:** `RecurringExpense` reuses everything `Expense` already does, and only adds what's genuinely different.

---

## Lesson 1: `class Child(Parent):` and `super()`

```python
class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)}"


class RecurringExpense(Expense):
    def __init__(self, category: str, amount: int, frequency: str):
        super().__init__(category, amount)   # reuse Expense's __init__ — don't rewrite it
        self.frequency = frequency
```

**Breaking this down:**

- **`class RecurringExpense(Expense):`** — the `(Expense)` part is the whole idea of inheritance. It says "`RecurringExpense` *is a kind of* `Expense`, starting with everything `Expense` already has."
- **`super().__init__(category, amount)`** — calls the **parent's** `__init__` directly, so you don't have to retype `self.category = category` / `self.amount = amount` all over again. `super()` means "go ask my parent class to do this part."
- **`self.frequency = frequency`** — the *new* thing this child class adds, on top of everything inherited.

```python
rent = RecurringExpense("Rent", 15000, "monthly")
print(rent.category)     # "Rent"      — inherited from Expense
print(rent.amount)        # 15000       — inherited from Expense
print(rent.frequency)      # "monthly"  — new, only on RecurringExpense
```

Notice `rent.category` and `rent.amount` work even though `RecurringExpense` never wrote that logic itself — it inherited it from `Expense` via `super().__init__()`.

---

## Lesson 2: Method Overriding

The parent's `formatted()` doesn't mention frequency at all — it just shows category and amount. `RecurringExpense` needs its *own* version that includes the frequency too. This is called **overriding**: the child class defines a method with the *same name* as the parent's, and Python uses the child's version instead when called on a child object.

```python
class RecurringExpense(Expense):
    def __init__(self, category: str, amount: int, frequency: str):
        super().__init__(category, amount)
        self.frequency = frequency

    def formatted(self) -> str:
        base = super().formatted()          # reuse the parent's formatting first
        return f"{base} (repeats {self.frequency})"
```

```python
rent = RecurringExpense("Rent", 15000, "monthly")
print(rent.formatted())
# "Rent: INR15,000.00 (repeats monthly)"
```

`super().formatted()` here works the same idea as `super().__init__()` did — "run the parent's version of this method first," then build on top of the result, instead of retyping the whole formatting logic from scratch.

---

## Lesson 3: Polymorphism — The Actual Payoff

Here's where this all pays for itself. Because `RecurringExpense` **is a kind of** `Expense`, you can put both types in the *same list*, and any code that calls `.formatted()` automatically gets the *correct* version for each object — no `if` statements checking types required.

```python
expenses = [
    Expense("Food", 500),
    RecurringExpense("Rent", 15000, "monthly"),
    Expense("Travel", 1200),
]

for e in expenses:
    print(e.formatted())
```

```
Food: INR500.00
Rent: INR15,000.00 (repeats monthly)
Travel: INR1,200.00
```

**Notice what *didn't* have to change:** `view_expenses()` in your real project already just does `expense.formatted()` in a loop. It has **zero idea** whether each `expense` is a plain `Expense` or a `RecurringExpense` — and it doesn't need to. Each object knows how to format *itself* correctly. That automatic "the right behavior happens for each object's actual type" is what **polymorphism** means.

---

## Exercise 9.1: Warm-up

Create `src/day9_inheritance.py`:

```python
"""
day9_inheritance.py
Practicing inheritance, super(), overriding, and polymorphism.
Author: Viraj
"""


class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} earns INR{self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: int, team_size: int):
        # YOUR CODE: call super().__init__() to reuse Employee's setup
        # YOUR CODE: set self.team_size
        pass

    def describe(self) -> str:
        # YOUR CODE: call super().describe(), then add team size info
        # e.g. "Viraj earns INR80000, managing a team of 5"
        pass


def main():
    people = [
        Employee("Alice", 50000),
        Manager("Viraj", 80000, 5),
        Employee("Bob", 45000),
    ]

    for person in people:
        print(person.describe())


if __name__ == "__main__":
    main()
```

**Expected output:**
```
Alice earns INR50000
Viraj earns INR80000, managing a team of 5
Bob earns INR45000
```

---

## Exercise 9.2: Add `RecurringExpense` to the Real Project

Add the `RecurringExpense` class to `expense_tracker.py`, right after the existing `Expense` class:

```python
class RecurringExpense(Expense):
    def __init__(self, category: str, amount: int, frequency: str):
        super().__init__(category, amount)
        self.frequency = frequency

    def formatted(self) -> str:
        base = super().formatted()
        return f"{base} (repeats {self.frequency})"
```

**To prove polymorphism works without touching the menu yet**, temporarily test it inside `main()` — add this at the very top of `main()`, before the `while True:` loop, just to see it work:

```python
def main():
    expenses = []
    expenses.append(Expense("Food", 500))
    expenses.append(RecurringExpense("Rent", 15000, "monthly"))
    # (leave the rest of main() exactly as it was — while True loop etc.)
```

Run the program and choose option 2 (View all expenses). You should see **both** the plain expense and the recurring one, correctly formatted, **without having changed `view_expenses()` at all.** That's the proof — the same function already handles both types correctly, because of polymorphism.

**Once you've confirmed that, remove the two test `.append()` lines** — they were only there to prove the concept works, not a real feature yet. A proper "Add recurring expense" menu option is a natural next step, but that's for another day, not today's scope.

---

## Common Beginner Mistakes (Day 9)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Forgetting `super().__init__()` entirely | Assuming inheritance means everything is automatic | You still have to explicitly call it — otherwise `self.category`/`self.amount` never get set on the child |
| Writing `Expense.__init__(self, ...)` instead of `super().__init__(...)` | Both technically work, but `super()` is the correct professional convention | Use `super()` — it's more maintainable if the class hierarchy changes later |
| Overriding a method but forgetting to call `super().method()` when you actually wanted to reuse the parent's logic | Rewriting from scratch out of habit | Ask: "does the child's version need everything the parent's version does, plus something extra?" If yes, call `super()` first |
| Checking `if isinstance(e, RecurringExpense):` everywhere instead of trusting polymorphism | Not yet trusting that `.formatted()` "just works" per object | If every subclass correctly overrides the method it needs, you never need to check types — that's the whole point |

---

## Best Practices (Day 9)

1. **Only inherit when there's a genuine "is-a" relationship.** A `RecurringExpense` *is* an `Expense` — that's a legitimate inheritance. Don't force inheritance where it doesn't naturally fit.
2. **Call `super()` to reuse parent logic rather than duplicating it**, in both `__init__` and any overridden method.
3. **Favor polymorphism over type-checking.** If you find yourself writing `if isinstance(x, Y):`, ask whether an overridden method would let the object handle it itself instead.

---

## Interview Questions (Day 9 Level)

1. What does `class RecurringExpense(Expense):` actually mean/do?
2. What does `super().__init__()` accomplish, and what would break if you left it out?
3. What is method overriding?
4. What is polymorphism, in your own words, using the `Expense`/`RecurringExpense` example?
5. Why didn't `view_expenses()` need any changes to support `RecurringExpense`?

---

## Resume Relevance

**What you can put on your resume after Day 9:**

> "Applied inheritance and polymorphism in Python to extend a base `Expense` class into a `RecurringExpense` subclass, enabling type-specific behavior without modifying existing display logic."

---

## Next Lesson Preview (Day 10)

**Topic:** File Handling — Reading & Writing Data

**What you will learn:**
- Reading and writing `.txt`, `.csv`, and `.json` files
- Finally giving the Expense Tracker real persistence — expenses survive after the program closes
- The `with open(...) as f:` pattern and why it matters

---

## ✅ Day 9 Checklist

- [ ] `day9_inheritance.py` created — Exercise 9.1 complete (`Manager` class working).
- [ ] `RecurringExpense` class added to `expense_tracker.py`.
- [ ] Polymorphism confirmed working via temporary test in `main()` (both types display correctly through unchanged `view_expenses()`).
- [ ] Temporary test lines removed after confirming.
- [ ] Code committed to Git.
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 9 complete."**

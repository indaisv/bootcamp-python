# Day 9 — Inheritance & Polymorphism

## Revision Notes

**Why inheritance instead of copy-paste:** copy-pasting `Expense` into a new `RecurringExpense` class would duplicate `category`/`amount` logic in two places — fix a bug in one, you'd have to remember the other. Inheritance lets `RecurringExpense` *reuse* `Expense`'s logic instead of repeating it.

**`class RecurringExpense(Expense):`** — the `(Expense)` in parentheses is the entire mechanism. It declares "this class inherits from `Expense`," meaning `RecurringExpense` automatically has access to everything `Expense` defines, before a single line is written inside `RecurringExpense` itself.

**`super().__init__(...)`** — calls the *parent's* constructor directly, so the child doesn't have to retype the parent's setup logic. **Leaving it out is a real, specific bug**, not just "bad practice": any attributes the parent normally sets (e.g. `self.category`, `self.amount`) simply never get created on the child object, and using them later raises `AttributeError: object has no attribute 'category'`.

**Method overriding** — when a child class defines a method with the **same name** as one in the parent, and Python uses the child's version for objects of that child's type. Both `Expense` and `RecurringExpense` have a `formatted()` method — `RecurringExpense`'s version *overrides* the parent's. The override can still call `super().method()` to reuse the parent's version as a starting point, then add to it, or it can ignore the parent's version entirely and do something completely different.

**Polymorphism ("many forms")** — the same method call (`expense.formatted()`) behaves differently depending on the *actual type* of the object it's called on, decided automatically at runtime. The concrete proof from today: `view_expenses()` was never edited, yet it correctly displayed both a plain `Expense` and a `RecurringExpense` with their own distinct formats — because it trusts `.formatted()` to know what to do, rather than checking `if isinstance(...)` and branching manually.

**The whole point, stated plainly:** code that works with a *parent* type (`Expense`) automatically works correctly with any *child* type (`RecurringExpense`) too, without modification — as long as the child properly overrides whatever methods need different behavior.

---

## Cheat Sheet

```python
# Base class
class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def formatted(self):
        return f"{self.category}: {format_currency(self.amount)}"

# Child class — inherits from Expense
class RecurringExpense(Expense):
    def __init__(self, category, amount, frequency):
        super().__init__(category, amount)   # reuse parent setup
        self.frequency = frequency             # add new attribute

    def formatted(self):                        # OVERRIDE parent's method
        base = super().formatted()               # reuse parent's version first
        return f"{base} (repeats {self.frequency})"

# Polymorphism — same call, different behavior per object
items = [Expense("Food", 500), RecurringExpense("Rent", 15000, "monthly")]
for item in items:
    print(item.formatted())     # correct output for EACH type, automatically
```

---

## Active Recall — Day 9

1. What does the `(Expense)` in `class RecurringExpense(Expense):` actually do?
2. What specifically breaks if you forget `super().__init__()` in a child class — name the exact error and why it happens.
3. What is method overriding, and where in your own project did you see two classes define the same method name?
4. Explain polymorphism using your own `Food`/`Rent` output as the example.
5. Why didn't `view_expenses()` need to change at all to support `RecurringExpense`?
6. What's the difference between calling `super().formatted()` inside an override versus not calling it at all?

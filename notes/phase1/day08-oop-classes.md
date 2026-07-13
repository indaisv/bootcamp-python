# Day 8 — OOP: Classes & Objects

## Revision Notes

**Why move from dict to class at all:** a dict like `{"category": "Food", "amount": 500}` has no built-in protection. A typo'd key (`expense["categroy"]`) silently creates a new, wrong key instead of erroring — the mistake hides. A class catches the same typo immediately: `expense.categroy` raises `AttributeError` the moment it happens, because that attribute was never defined. The class also lets behavior (like formatting for display) travel with the data itself, instead of being rewritten wherever the data is used.

**The three required pieces of a basic class:**
```python
class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount
```
- `class Expense:` — declares the blueprint. No object exists yet.
- `__init__` — **exact, reserved name** (not a name you invent or paraphrase — "initialize" is what it *stands for*, not a valid alternative spelling). Runs automatically the instant an object is created.
- `self` — refers to *this specific object*. Every method automatically receives it as the first parameter; Python passes it in for you when you call `obj.method()`.

**`self.category = category` is what makes data stick.** Without the `self.` prefix, `category` is just a local variable inside `__init__` that disappears the moment `__init__` finishes — it never attaches to the object.

**Creating objects (instantiating):** `e1 = Expense("Food", 500)` builds one independent object. `e2 = Expense("Travel", 1200)` builds a completely separate one — they don't share data, same as two separate lists (not two labels on the same list).

**Methods** are functions defined inside the class, also automatically receiving `self`, giving them access to that object's own data:
```python
def formatted(self) -> str:
    return f"{self.category}: {format_currency(self.amount)}"
```
Called via `e1.formatted()` — not called on the class itself (`Expense.formatted()` with no object makes no sense; there's no `self` to work with).

**Two unrelated things that share the name `__init__` — a real source of confusion, worth keeping permanently separate:**
| | `__init__.py` (Day 7) | `__init__` (Day 8) |
|---|---|---|
| What it is | A file | A method inside a class |
| Job | Marks a folder as an importable package | Runs automatically when an object is created |

Same double-underscore ("dunder") naming convention, completely different mechanism and context.

---

## Cheat Sheet

```python
class Expense:
    def __init__(self, category: str, amount: int):
        self.category = category
        self.amount = amount

    def formatted(self) -> str:
        return f"{self.category}: {format_currency(self.amount)}"


# Creating objects
e1 = Expense("Food", 500)
e2 = Expense("Travel", 1200)

# Accessing attributes — dot notation, not brackets
e1.category      # "Food"
e1.amount         # 500

# Calling methods
e1.formatted()     # "Food: INR500.00"

# Dict access (old way) vs class access (new way)
expense["category"]     # dict — bracket notation
expense.category          # object — dot notation
```

**Debugging checklist for class errors:**
- `TypeError: X() takes no arguments` → check your constructor is spelled exactly `__init__`, not a paraphrase.
- `AttributeError: 'X' object has no attribute 'y'` → typo in the attribute name, or it was never set in `__init__`.
- Forgot `self.` in front of an assignment inside `__init__` → the value never attaches to the object.

---

## Active Recall — Day 8

1. What is `self`, and why does every method need it as the first parameter?
2. What's the difference between a class and an object (instance)?
3. What does `__init__` actually do, and when does it run?
4. Give a concrete reason a class is safer than a dictionary for representing structured data.
5. What's the difference between an attribute and a method?
6. Why doesn't `initialize` work as a substitute name for `__init__`, even though it means the same thing conceptually?
7. What are the two completely unrelated things both called `__init__` across Day 7 and Day 8?

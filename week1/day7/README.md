# Week 1, Day 7: Modules & Packages

> **Learning Objectives:**
> 1. Understand what a module actually is (hint: you've already been writing them).
> 2. Master the different `import` forms and when to use each.
> 3. Build your own reusable module and import it into other files.
> 4. Understand `__init__.py` and what turns a folder into a package.
> 5. Refactor duplicated formatting logic across your project into one shared module (DRY principle).

---

## Business Motivation

Look across your own code right now: `business_calculator.py`, `invoice_formatter.py`, and `expense_tracker.py` all format money with roughly the same idea — `f"INR{amount}"` or `f"₹{amount:.2f}"` — written out separately, by hand, in three different places. If the currency symbol changes, or you decide to add thousands separators, you'd have to hunt down and fix it in every file. That's not a hypothetical — it's the exact repeated code sitting in your project right now.

**Modules solve this.** Write the formatting logic once, in one file, then `import` it wherever it's needed. Fix a bug once, it's fixed everywhere. This is the actual foundation every Python project of any real size is built on — nobody writes 10,000 lines in a single file.

---

## Lesson 1: What Is a Module? (You Already Know This)

**A module is just a `.py` file.** That's the whole definition. Every file you've written this week — `day2_variables.py`, `expense_tracker.py` — is already a module. You've been *using* other modules since Day 2 without necessarily calling them that:

```python
import math                    # math is a module — someone else's .py file (built into Python)
print(math.sqrt(16))
```

`math.sqrt()` works because `math` is a module, and `sqrt` is a function defined inside it. `import math` gives you access to everything inside that file, accessed through the module's name.

**The only new idea today: you can do this with your *own* files, not just built-in ones.**

---

## Lesson 2: The Import Forms

```python
import math                          # bring in the whole module, access via math.sqrt()
from math import sqrt                # bring in ONE thing directly, access via sqrt() (no prefix)
from math import sqrt, pow           # bring in multiple specific things
import math as m                     # rename on import, access via m.sqrt()
from math import sqrt as square_root # rename a specific import
```

**Which one to use?**
- `import module_name` — safest default. Keeps things namespaced (`math.sqrt` is unambiguous about where `sqrt` came from), which matters more as a project grows.
- `from module import specific_thing` — fine when you're using that one thing constantly and the module name would just be noise. You've technically already seen this pattern's cousin in `from expense_tracker import add_expense` style imports.
- `as` aliasing — mostly for long/awkward names, or an industry-standard convention (you'll meet `import pandas as pd` and `import numpy as np` in Phase 2 — everyone does this, it's not optional style).

---

## Lesson 3: Building Your Own Module

Create `src/money_utils.py`:

```python
"""
money_utils.py

Shared currency formatting used across the bootcamp project.
Author: Viraj
"""


def format_currency(amount: float) -> str:
    """
    Format a number as an INR currency string.

    Args:
        amount: The numeric amount.

    Returns:
        A string like "INR1,234.56".
    """
    return f"INR{amount:,.2f}"
```

Now, in a **different** file — create `src/day7_modules.py`:

```python
"""
day7_modules.py
Practicing imports with a custom module.
Author: Viraj
"""

from money_utils import format_currency


def main():
    print(format_currency(500))
    print(format_currency(1234.5))
    print(format_currency(99))


if __name__ == "__main__":
    main()
```

**Run it from the `src/` folder context the same way you've run every other file.** If Python complains it can't find `money_utils`, it's almost always because the two files aren't in the same folder — Python looks in the *same directory as the file you're running* first, by default.

**Expected output:**
```
INR500.00
INR1,234.50
INR99.00
```

Notice `format_currency` was written once, and both here and in a moment inside `expense_tracker.py`, you'll get identical formatting for free — no copy-pasting the `f"INR{amount:,.2f}"` pattern again.

---

## Lesson 4: Packages — Folders That Act Like Modules (Brief, You'll Use This More Later)

A **package** is a folder containing a special file called `__init__.py`, which tells Python "treat this folder as an importable package, not just a folder of unrelated files."

```
src/
├── utils/
│   ├── __init__.py         ← can be empty — its presence is what matters
│   └── money_utils.py
```

With that structure, you'd import as:
```python
from utils.money_utils import format_currency
```

**You don't need to restructure your project into packages today** — for a project this size, flat files in `src/` are still totally reasonable. This is here so the term isn't a mystery when your project grows and packages become the right call (you'll do this for real once the project gets bigger in later phases).

---

## Lesson 5: The Real Refactor — DRY Your Formatting

Now the payoff. Go into `expense_tracker.py` and replace every hand-written `f"INR{amount}"` with a call to your new shared function.

```python
from money_utils import format_currency

# Before:
print(f"Added: {category} - INR{amount}")

# After:
print(f"Added: {category} - {format_currency(amount)}")
```

Do this in **all three places** `INR{...}` currently appears in `expense_tracker.py`: `add_expense()`, `view_expenses()`, and the totals-printing block in `main()`.

**Why this is worth doing, concretely:** if you later decide amounts should show 2 decimal places consistently (right now `INR40` and `INR2,000.00` would look inconsistent — one has decimals, one doesn't), you fix it in **one place** (`money_utils.py`), and it's correct everywhere at once. That's the entire value proposition of a module.

---

## Common Beginner Mistakes (Day 7)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| `ModuleNotFoundError: No module named 'money_utils'` | The importing file and `money_utils.py` aren't in the same folder | Keep custom modules in the same directory as the files that import them, for now |
| `from money_utils import *` | Seems like a shortcut to "get everything" | Avoid this — it pollutes your namespace and hides *where* a function actually came from. Import specific names. |
| Circular imports (`a.py` imports `b.py`, `b.py` imports `a.py`) | Splitting code without thinking about dependency direction | Keep shared/reusable code (like `money_utils.py`) as a one-way dependency — other files import it, it doesn't import them |
| Naming your file the same as a real Python module (e.g. `math.py`) | Innocent naming collision | Never name your own files after standard library modules — Python will import yours instead of the real one, breaking everything |
| Running `money_utils.py` directly expecting output | Forgetting it's a *library* file, not a script | It has no `if __name__ == "__main__":` block with real logic — it's meant to be imported, not run directly. That's fine and intentional. |

---

## Best Practices (Day 7)

1. **One module, one clear purpose.** `money_utils.py` formats money — it shouldn't also handle dates or file I/O.
2. **Prefer `import module` or `from module import specific_thing` over `from module import *`.** Explicit imports make it obvious where a function came from when you're reading code later.
3. **Shared/reusable code should have no dependency on the files that use it.** `money_utils.py` should never need to `import` anything from `expense_tracker.py`.
4. **A module doesn't need an `if __name__ == "__main__":` block unless it's also meant to be run directly.** `money_utils.py` doesn't need one — it's purely a library.

---

## Interview Questions (Day 7 Level)

1. What's the actual definition of a "module" in Python?
2. What's the difference between `import math` and `from math import sqrt`?
3. What does `__init__.py` do, and what does its presence signal to Python?
4. Why is `from module import *` generally discouraged?
5. What's a circular import, and why does it cause problems?

---

## Resume Relevance

**What you can put on your resume after Day 7:**

> "Refactored duplicated formatting logic across multiple Python modules into a single reusable utility module, applying the DRY (Don't Repeat Yourself) principle."

---

## Next Lesson Preview (Day 8)

**Topic:** Object-Oriented Programming — Classes & Objects

**What you will learn:**
- Why functions + dictionaries eventually hit a ceiling, and what a class gives you instead
- `class`, `__init__`, `self`, attributes, and methods
- Refactoring the Expense Tracker's `{"category": ..., "amount": ...}` dicts into a proper `Expense` class

---

## ✅ Day 7 Checklist

- [ ] `money_utils.py` created with `format_currency()`.
- [ ] `day7_modules.py` created and imports/runs correctly.
- [ ] `expense_tracker.py` refactored — all 3 `INR{...}` spots now use `format_currency()`.
- [ ] Program still runs identically to before (same behavior, cleaner internals).
- [ ] Code committed to Git.
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 7 complete."**

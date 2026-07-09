# Day 2 — Variables, Data Types, Operators

## Revision Notes

**Variables are labels, not boxes.** `name = "Viraj"` doesn't put `"Viraj"` *inside* `name` — it creates a string object somewhere in memory, and `name` points to it. Two variables can point to the *same* object (`a = b`); reassigning one doesn't move the label off the other.

**The 5 core types**
| Type | Mutable? | Notes |
|---|---|---|
| `int` | No | No fixed size limit in Python |
| `float` | No | Binary rounding errors — `0.1 + 0.2 != 0.3` |
| `str` | No | `.upper()` etc. return a *new* string, don't modify in place |
| `bool` | No | `True`/`False` — falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `None` |
| `None` | No | Singleton — always compare with `is`, not `==` |

**`==` vs `is`** — the #1 interview question of the week.
- `==` compares **value**. Use this almost always.
- `is` compares **identity** (same object in memory). Use this *only* for `None` checks, because `None` is a singleton — there's exactly one `None` object in the whole program.

**Mutable vs immutable — the bug that gets you fired**
- Lists/dicts/sets are mutable: modifying a parameter inside a function can silently modify the caller's original data, if you didn't mean to.
- Fix: don't mutate in place unless that's the explicit intent — build and return a new object, or `.copy()` first.
- Strings are immutable: `name.upper()` returns a new string; you must reassign (`name = name.upper()`) or the change is lost.

**Type casting** — always validate before converting user input:
```python
if user_input.isdigit():
    value = int(user_input)
```
Blind `int(user_input)` crashes on bad input. This is the exact pattern you used in the Expense Tracker's `add_expense`.

**`math` module** — `math.pow()`, `math.sqrt()`, `math.ceil()`/`floor()`, constants `math.pi`/`math.e`. Used for real formulas like EMI and compound interest (see `business_calculator.py`).

**f-string formatting codes** — `:.2f` (2 decimals), `:,` (thousands separator), `:.1%` (percentage), `:>N`/`:<N`/`:^N` (align in N-char field), `:0Nd` (zero-pad).

---

## Cheat Sheet

```python
# == vs is
a == b     # value equality — use for almost everything
x is None  # identity — use ONLY for None checks

# Type checking
isinstance(x, int)              # preferred over type(x) == int
isinstance(x, (int, float))     # multiple types at once

# Safe mutation avoidance
def add_tax(items, rate=0.18):
    return [p * (1 + rate) for p in items]   # new list, original untouched

# Safe type casting
if user_input.isdigit():
    value = int(user_input)
else:
    print("Invalid input.")

# math module
import math
math.pow(2, 3)     # 8.0
math.sqrt(16)       # 4.0
math.ceil(4.2)      # 5
math.floor(4.8)     # 4

# f-string formatting
f"{price:,.2f}"     # 1,234.56
f"{rate:.1%}"        # 23.5%
f"{name:>20}"        # right-align in 20 chars
f"{id:06d}"          # 000123
```

---

## Active Recall — Day 2

1. What's actually happening in memory when you write `a = b`?
2. When should you use `is` instead of `==`? Why only then?
3. Why does `0.1 + 0.2 != 0.3` in Python? How do you work around it?
4. What's the bug in modifying a mutable function argument in place — walk through a concrete example.
5. Why must you reassign after `name.upper()`?
6. What's the risk of calling `int(user_input)` without checking `.isdigit()` first?
7. What's the difference between `type()` and `isinstance()`, and why does it matter for inheritance?

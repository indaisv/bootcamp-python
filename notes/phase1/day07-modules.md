# Day 7 — Modules & Packages

## Revision Notes

**A module is just a `.py` file.** You've been writing modules since Day 1 without the label — `import math` works because `math` is a `.py` file (built into Python), and `math.sqrt` is a function defined inside it. Today's only new idea: you can `import` your *own* files the same way.

**Import forms**
- `import module_name` — brings in the whole module; access everything via `module_name.thing`. Safest default — keeps origin obvious.
- `from module import thing` — brings in one specific thing directly, no prefix needed.
- `import module as alias` / `from module import thing as alias` — renaming, mostly for long names or industry convention (`import pandas as pd`, later in the roadmap).
- `from module import *` — avoid. Pulls in everything with no prefix, which means you can no longer tell *where* a given name came from just by reading the code — and if two modules define the same name, one silently overwrites the other.

**Where Python looks for your own modules:** by default, the same folder as the file you're running. This is why `money_utils.py` had to be duplicated into `projects/expense_tracker/src/` — a module sitting in the top-level `src/` isn't visible to a script running from a different folder. (This limitation is exactly what packages solve properly — not needed yet at this project's size.)

**Packages** = a folder containing `__init__.py`, which signals to Python "treat this folder as importable," not a real folder-of-loose-files. Not needed for this project yet — flat files in `src/` are fine at this scale.

**Circular imports** — `a.py` imports `b.py`, and `b.py` imports `a.py`. When Python starts loading `a.py` and hits `import b`, it pauses `a.py` mid-load to go load `b.py`. But `b.py` immediately tries to import `a.py` back — except `a.py` isn't finished loading yet, so `b.py` gets an incomplete version of it, missing anything defined after the pause point. Avoid by keeping shared/reusable modules (like `money_utils.py`) as one-way dependencies — things import it, it doesn't import them back.

**Today's real refactor:** duplicated `f"INR{amount}"` formatting across three files got extracted into one function (`format_currency()`) in one module (`money_utils.py`), then imported wherever needed. Fix a formatting bug once, it's fixed everywhere — the actual point of DRY (Don't Repeat Yourself).

---

## Cheat Sheet

```python
# Import forms
import math                       # math.sqrt(16)
from math import sqrt              # sqrt(16) — no prefix
from math import sqrt, pow         # multiple specific names
import math as m                    # m.sqrt(16)
from math import sqrt as square_root

# Your own module — money_utils.py
"""
money_utils.py
Shared currency formatting.
"""
def format_currency(amount: float) -> str:
    return f"INR{amount:,.2f}"

# Using it from another file IN THE SAME FOLDER
from money_utils import format_currency
print(format_currency(1234.5))   # INR1,234.50
```

**Debugging `ModuleNotFoundError` on your own module — check in this order:**
1. Is the module file in the *same folder* as the file importing it?
2. Did you accidentally name your file the same as a real Python module (e.g. `math.py`)? Rename it.
3. Are you trying to use a dotted package path (`folder.subfolder.module`) without actual package setup? Use the plain `from module import thing` form instead, unless you've deliberately built package structure.

---

## Active Recall — Day 7

1. What's the actual definition of a "module" in Python?
2. What's the difference between `import math` and `from math import sqrt`?
3. Why does Python fail to find a module you wrote yourself, even though the file clearly exists somewhere in your project?
4. What does `__init__.py` signal to Python?
5. Why is `from module import *` discouraged, specifically?
6. Walk through, step by step, why a circular import breaks — not just that it does.
7. What was the actual business value of extracting `format_currency()` into `money_utils.py`, beyond "it's cleaner"?

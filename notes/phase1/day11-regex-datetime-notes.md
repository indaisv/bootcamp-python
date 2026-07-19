# Day 11: Regex & Datetime — Notes

## 1. Revision Notes

**Regex validates shape, not just type.** `isdigit()` can only ask "is this all digits" — it can't express "digits, optionally with a decimal point and up to 2 decimal places." Regex patterns describe the exact structure text must have.

**Core syntax:**
- `\d` digit, `\w` word char, `\s` whitespace, `.` any char
- `*` zero-or-more, `+` one-or-more, `?` optional, `{n,m}` between n and m
- `^` start of string, `$` end of string, `()` groups part of the pattern

**The 3 `re` functions:**
- `re.search(pattern, text)` — pattern anywhere in the string
- `re.fullmatch(pattern, text)` — entire string must match, start to end
- `re.findall(pattern, text)` — list of every match

**Always write regex patterns as raw strings** (`r"\d+"`). Without the `r`, Python tries to interpret `\d` as an escape sequence before regex ever sees it — usually harmless (like `\d`, which just produces a warning), but fragile and inconsistent.

**`datetime`:**
- `strftime()` — object → string ("from time")
- `strptime()` — string → object ("parse time")
- Store dates as `"%Y-%m-%d"` (ISO format) — sorts correctly as plain text and is unambiguous across locales, unlike `"18/7/26"`.

**The default-value trap:** `self.date = date if date else None` looks reasonable but is wrong whenever the field should never truly be empty. If no date is given, the correct default is *today's actual date* (`datetime.now().strftime(...)`), not `None` — otherwise the field silently stays empty forever, even across save/reload cycles, because an empty CSV field reloads as `""` (falsy) and collapses back to `None` every time.

**Debugging insight from today:** a `KeyError` after adding a new field to a CSV-backed class almost always means old data on disk predates the schema change. Two valid fixes exist — `.get()` to gracefully handle the missing key, or deleting/migrating the old file — and the right choice depends on whether the old rows' missing data would actually be *useful* once defaulted, or just a crash traded for silently-wrong data.

---

## 2. Cheat Sheet

```python
import re
from datetime import datetime

# --- Regex ---
re.fullmatch(r"^\d+(\.\d{1,2})?$", text)   # whole-string amount validation
re.search(r"\d+", text)                     # find digits anywhere
re.findall(r"\d+", text)                    # list of all digit runs

# common patterns
r"^\d+$"            # digits only
r"^\d+(\.\d{1,2})?$"  # digits, optional 1-2 decimal places
r"^[A-Za-z]{2,20}$"   # letters only, 2-20 chars

# --- Datetime ---
datetime.now()                              # current datetime object
datetime.now().strftime("%Y-%m-%d")         # object -> "2026-07-18"
datetime.strptime("2026-07-18", "%Y-%m-%d") # string -> object

# date math
delta = date2 - date1     # timedelta object
delta.days                 # number of days between them

# --- Safe default pattern (avoid the None trap) ---
def __init__(self, value, date: str = None):
    self.date = date if date else datetime.now().strftime("%Y-%m-%d")
    # NOT: date if date else None  <- silently stays empty forever
```

---

## 3. Active Recall Questions

1. What's the difference between `re.search()` and `re.fullmatch()`? Give an example input where they'd disagree.
2. Why should regex patterns always be written as raw strings?
3. What does the pattern `r"^\d+(\.\d{1,2})?$"` actually require — walk through each piece.
4. What's the difference between `strftime()` and `strptime()`, and which direction does each go?
5. Why is `"%Y-%m-%d"` a better format to store dates in than `"18/7/2026"`?
6. Why was `self.date = date if date else None` a bug, specifically in the context of saving to and loading from CSV?
7. If you add a new column to a CSV-backed class and get a `KeyError` on old data, what are the two valid fixes, and how do you decide which one to use?
8. What does `re.findall(r"\d+", text)` return — and what type are the items inside it?

# Week 1, Day 11: Regex & Datetime

> **Learning Objectives:**
> 1. Use `re` to validate text against a *pattern*, not just a type (`isdigit()` → proper amount validation).
> 2. Read core regex syntax: `\d`, `\w`, `\s`, `.`, `*`, `+`, `?`, `{n,m}`, `^`, `$`.
> 3. Use `re.fullmatch()`, `re.search()`, and `re.findall()` correctly — know when each applies.
> 4. Use `datetime.now()` + `strftime()` to generate timestamps; `strptime()` to parse strings back.
> 5. Add a `date` field to `Expense`/`RecurringExpense` and wire real validation into the live project.

---

## Business Motivation

Two real gaps existed in the Expense Tracker before today:
- **No dates.** Every expense existed with no record of *when* it happened — no way to ever answer "how much did I spend this month."
- **Weak validation.** `amount_input.isdigit()` only accepts whole numbers — `450.50` was rejected outright, even though decimal amounts are completely normal for money.

Regex fixes the second by checking *shape* ("digits, optionally with up to 2 decimal places") instead of a blunt yes/no type check. `datetime` fixes the first by giving every expense a real, sortable timestamp.

---

## Lesson 1: Regex — Pattern Matching

Regex describes the *shape* of text, not just its type.

| Symbol | Meaning |
|--------|---------|
| `\d` | one digit |
| `\w` | one word character (letter/digit/underscore) |
| `\s` | one whitespace character |
| `.` | any character |
| `*` | zero or more of the previous thing |
| `+` | one or more of the previous thing |
| `?` | optional (zero or one) |
| `{n,m}` | between n and m of the previous thing |
| `^` / `$` | start / end of string |
| `()` | group part of the pattern |

**The three `re` functions that cover most use cases:**
```python
re.search(pattern, text)     # pattern anywhere in text → Match or None
re.fullmatch(pattern, text)  # ENTIRE text must match → Match or None
re.findall(pattern, text)    # list of ALL matches
```

**Always use raw strings for patterns** (`r"\d+"`, not `"\d+"`) — regex leans on `\` constantly, and without `r`, Python tries to interpret those as escape sequences first.

**Validating a money amount:**
```python
def is_valid_amount(text: str) -> bool:
    pattern = r"^\d+(\.\d{1,2})?$"
    return re.fullmatch(pattern, text) is not None
```
`^\d+` = starts with digits. `(\.\d{1,2})?` = an *optional* group: a literal dot + 1-2 digits. `$` = nothing else allowed after.

---

## Lesson 2: `datetime` — Timestamps

```python
from datetime import datetime

now = datetime.now()
today_str = now.strftime("%Y-%m-%d")            # object → string

parsed = datetime.strptime("2026-07-18", "%Y-%m-%d")  # string → object
```

**Memory trick:** `strftime` = string **F**rom time. `strptime` = string **P**arsed to time.

**Why `"%Y-%m-%d"` (ISO format) specifically:** it sorts correctly as plain text — `"2026-01-05" < "2026-07-18"` alphabetically matches chronologically — and it's unambiguous across locales, unlike `"18/7/26"`.

---

## Exercise 11.1 — `day11_regex_datetime.py`

Built and tested: `is_valid_amount()`, `is_valid_category()`, `extract_numbers()`, `get_today_string()`, `days_between()`. All 6 test cases in `test_all()` passed on the first real attempt.

---

## Project Integration — Expense Tracker

Real changes made to `expense_tracker.py` today:

1. **`is_valid_amount()`** moved into the tracker itself, replacing `amount_input.isdigit()` in `add_expense()` — amounts like `450.50` are now accepted.
2. **`Expense.__init__`** gained a `date: str = None` parameter — defaults to `datetime.now().strftime("%Y-%m-%d")` when no date is given, so every expense is timestamped automatically.
3. **`RecurringExpense.__init__`** passes `date` through to `super().__init__()`.
4. **Both `to_dict()` methods** now include `"date"` in the returned dict.
5. **`save_expenses()`** — `"date"` added to `fieldnames`.
6. **`load_expenses()`** — both branches now pass `row["date"]` when reconstructing `Expense`/`RecurringExpense` objects.
7. **`amount` is now `float`, not `int`**, throughout — matches decimal-friendly validation.

### Bugs hit and fixed today (real debugging log — good interview material)
- `from datetime import datetime, re` — `re` isn't part of `datetime`; needs its own `import re` line.
- `self.date = date if date else None` — meant every un-dated expense stayed `None` forever, even after save/reload, since an empty CSV field reloads as `""` (falsy) → `None` again. Fixed by defaulting to `datetime.now().strftime(...)` instead of `None`.
- `format_currency(self.amount) ({self.date})` inside an f-string — a misplaced `}` meant Python read this as "call `format_currency(...)`, then call *its return value* as a function with `self.date`" → `TypeError: 'str' object is not callable`. Fixed by closing the f-string expression right after `format_currency(self.amount)`.
- `int(row["amount"], row["date"])` — misplaced parenthesis caused `row["date"]` to be passed as `int()`'s base argument instead of as `Expense`'s third constructor argument.
- `KeyError: 'date'` on load — old `expenses.csv` predated the `date` column (same root cause as the earlier `type`-column bug). Fixed by deleting the outdated CSV rather than patching around it with `.get()`, since defensive `.get()` here would've just produced `None` dates for every old row — a crash avoided but not useful data.

---

## Common Mistakes (Day 11)

| Mistake | Fix |
|---------|-----|
| Forgetting `r` prefix on regex patterns | Always `r"\d+"` |
| `re.search()` when you meant `re.fullmatch()` | `search` matches *part* of a string; `fullmatch` requires the whole thing to match |
| Mixing up `strftime`/`strptime` | *f*rom object → string; *p*arse string → object |
| Storing dates as inconsistent/raw strings | Always `"%Y-%m-%d"` |
| Two-value default trap: `x if x else None` | If the field should never truly be empty, default to a *real* value, not `None` |

---

## Interview Questions (Day 11 Level)

1. What's the difference between `re.search()`, `re.fullmatch()`, and `re.findall()`?
2. Why should regex patterns be written as raw strings?
3. What does `{1,2}` mean in a regex pattern?
4. What's the difference between `strftime()` and `strptime()`?
5. Why is `"%Y-%m-%d"` a better date format to store than `"18/7/2026"`?
6. Walk through why `date if date else None` was a bug in this project, and what the correct default should have been.

---

## Resume Relevance

> "Added regex-based input validation and datetime timestamping to a Python CLI expense tracker, including debugging real production-style bugs in data persistence and object reconstruction from CSV."

---

## Next Lesson Preview (Day 12)

**Topic:** Exception Handling & Logging — replacing manual `if not valid:` checks with proper `try/except`, and adding a real logging system instead of `print()` debugging.

---

## ✅ Day 11 Checklist

- [x] `day11_regex_datetime.py` created — all functions implemented and tested.
- [x] `is_valid_amount()` wired into `add_expense()`, replacing `isdigit()`.
- [x] `date` field added to `Expense` and `RecurringExpense`, with correct default.
- [x] `save_expenses()`/`load_expenses()` updated for the new `date` column.
- [x] Old `expenses.csv` (outdated schema) deleted; verified fresh file works end-to-end.
- [ ] Code committed to Git and pushed.
- [ ] I can answer all 6 interview questions.

---

**When you are done, tell me: "Day 11 complete."**

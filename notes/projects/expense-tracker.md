# Project 1 — Personal Expense Tracker (v1, in-memory)

**Status:** Menu loop working (Day 5). Data lives in memory only — no persistence yet.
**Location:** `projects/expense_tracker/src/expense_tracker.py`
**Upgrade planned:** once File Handling is covered, this becomes CSV-backed (`data/expenses.csv`).

## Architecture (v1)
- `expenses` = list of dicts: `{"category": str, "amount": int}`, created fresh each run in `main()`.
- `print_menu()` — pure display, no logic.
- `add_expense(expenses)` — validates input, mutates the list in place via `.append()`.
- `view_expenses(expenses)` — read-only, numbered display, handles empty state.
- `total_by_category(expenses)` — aggregates via the dict-accumulator pattern.
- `main()` — the `while True` + `break` menu loop, dispatches to the above via `if/elif`.

## Key decisions / why
- Amount stored as `int`, not `str` — validated once at input time (`isdigit()` → `int()`), so every downstream function can trust the type.
- Functions take `expenses` as a parameter rather than using a global — keeps them testable in isolation later (relevant once Pytest shows up).
- `add_expense` returns early (`return`) on bad input rather than crashing or silently continuing with garbage data.

## Known limitation (by design, for now)
- No persistence — closing the program loses all data. This is intentional; File Handling hasn't been taught yet.

## Resume bullet (draft)
> Built a menu-driven CLI expense tracker in Python using loop control structures and dictionary aggregation for category-wise spend analysis.

## Interview questions to be ready for
1. Why pass `expenses` into each function instead of making it global?
2. Walk through what happens end-to-end when a user picks option 1 and enters bad input.
3. How would you extend this to persist data across runs?
4. Why validate with `isdigit()` before `int()` instead of just wrapping `int()` in a try/except?

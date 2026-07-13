# Project 1 — Personal Expense Tracker (v2, class-based)

**Status:** Menu loop working, now backed by a real `Expense` class (Day 8). Data still in memory only — no persistence yet.
**Location:** `projects/expense_tracker/src/expense_tracker.py`
**Upgrade planned:** File Handling → CSV persistence. Day 9 → `RecurringExpense` subclass via inheritance.

## Architecture (v2)
- `Expense` class — `__init__(self, category, amount)` sets `self.category`/`self.amount`; `formatted()` method returns a display-ready string using `money_utils.format_currency()`.
- `expenses` = list of `Expense` **objects** (changed from Day 5's list of dicts).
- `print_menu()` — unchanged, pure display.
- `add_expense(expenses)` — validates input, builds an `Expense` object, appends it.
- `view_expenses(expenses)` — loops and calls `expense.formatted()` per item.
- `total_by_category(expenses)` — accumulates via `expense.category` / `expense.amount` (dot access, not dict brackets), returns the totals dict.
- `main()` — unchanged menu loop; still passes `expenses` into every function as a parameter.

## Key decisions / why
- Switched from dict to class specifically to catch attribute-name typos immediately (`AttributeError`) instead of silently creating a wrong key, as a dict would.
- `formatted()` lives on the `Expense` object itself, not rewritten in each function that needs to display one — same DRY principle from Day 7, applied to behavior instead of a standalone utility function.
- `money_utils.format_currency()` (Day 7) is reused inside `Expense.formatted()` rather than duplicated — one function underneath, multiple layers using it.

## Known limitation (by design, for now)
- Still no persistence — closing the program loses all data. File Handling hasn't been taught yet.

## Resume bullet (draft)
> Refactored a Python CLI application from dictionary-based data to a proper class-based object model, improving data integrity and encapsulating display logic within the domain object.

## Interview questions to be ready for
1. Why pass `expenses` into each function instead of making it global? *(still applies, unchanged from v1)*
2. Why refactor from a dict to a class here — what does it actually protect against?
3. Where does `formatted()` live, and why does putting it there matter?
4. How would you extend this to support a different *kind* of expense (e.g. recurring)? *(preview of Day 9 — inheritance)*

# Day 17: Clean Code Principles — Notes

## 1. Revision Notes

**Clean code today wasn't new syntax — it was auditing 17 days of real, already-written code** against principles like naming, DRY, avoiding magic values, shallow nesting, and comments that explain *why* rather than *what*. Most of these were already being followed correctly by this point — the value was in the audit itself, not in learning something brand new.

**`black` and `ruff` — first real use, despite being in `requirements.txt` since Day 1.** `black` is an opinionated auto-formatter (no style debates, it just enforces one consistent style). `ruff` is a fast linter (catches unused imports, style issues, and some real bugs, without running the code). Structurally different CLI shapes worth remembering: `black --check <file>` (a flag), `ruff check <file>` (a subcommand) — same idea as `git commit -m`, `docker run`, `pip install`: tool → subcommand → options.

**Linter output needs triage, not blind fixing.** Six `ruff` findings today were consciously *not* fixed — not because they're wrong, but because they were correctly weighed as lower priority right now:
- Implicit `Optional` typing (`date: str = None` should be `date: str | None = None`) — purely a type-hint correctness issue, zero runtime effect.
- `datetime.now()` without a timezone — irrelevant for a single-user local app.
- Root logger usage instead of a named logger (`logging.getLogger(__name__)`) — a real best practice, but a broader refactor touching every log call, deferred rather than rushed.

Knowing *which* linter warnings matter right now versus which are safe to defer is itself a clean-code skill — not everything flagged needs fixing immediately.

**The real find of the day:** `is_valid_category()` was built and tested on Day 11, but never actually called in the live `add_expense()` function — discovered by direct inspection, not by being told. A tested, working function sitting completely unused in the codebase is a specific, real kind of bug: the code *looks* validated because the validation function exists, but nothing was actually enforcing it.

**The fix surfaced a second, subtler problem:** once two different validations (`category`, `amount`) could both raise into the same `except ValueError` block, a *hardcoded* error message became actively misleading — it would show the wrong explanation depending on which validation actually failed. Fixed by printing the exception's own message (`str(e)`) instead of a fixed string — the correct, specific message follows automatically from whichever `raise` actually fired.

---

## 2. Cheat Sheet

```bash
# black — auto-formatter
black --check path/to/file.py     # preview only, no changes
black path/to/file.py             # apply formatting

# ruff — linter
ruff check path/to/file.py            # report issues
ruff check --fix path/to/file.py      # auto-fix what's safely fixable
```

**Ambiguous exception messages — the pattern to avoid and the fix:**
```python
# BAD — message is hardcoded, wrong if a DIFFERENT validation actually failed
try:
    if not is_valid_category(category):
        raise ValueError("bad category")
    if not is_valid_amount(amount_input):
        raise ValueError("bad amount")
except ValueError:
    print("Invalid amount. Please enter a number.")   # wrong if category failed!

# GOOD — the exception carries its own correct message
try:
    if not is_valid_category(category):
        raise ValueError(f"Invalid category: '{category}'")
    if not is_valid_amount(amount_input):
        raise ValueError(f"Invalid amount: '{amount_input}'")
except ValueError as e:
    print(str(e))   # always shows the message that actually matches what failed
```

---

## 3. Active Recall Questions

1. What's the core difference in what `black` does versus what `ruff` does?
2. Why is `ruff check <file>` correct but `ruff --check <file>` is not?
3. What does "implicit Optional" mean for a parameter typed `date: str = None`?
4. Why is printing `str(e)` inside an `except` block often better than a hardcoded message, once more than one thing could raise that same exception type?
5. What real, working, tested function existed in the codebase since Day 11 but was never actually called anywhere — and how was that discovered?
6. Why is it acceptable clean-code practice to *not* fix every single linter warning immediately?
7. Name one specific `ruff` finding from today that was deliberately deferred, and explain why deferring it was the reasonable choice.

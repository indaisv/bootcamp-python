# Week 1, Day 17: Clean Code Principles

> **Learning Objectives:**
> 1. Audit real, already-written code against core clean-code principles instead of learning them abstractly.
> 2. Use `black` (auto-formatter) and `ruff` (linter) for the first time — install already existed since Day 1/15, never run until today.
> 3. Read and triage linter output: fix what matters now, consciously defer what doesn't.
> 4. Find and fix a real gap: a validated-but-never-called function sitting unused in the codebase.

---

## Business Motivation

17 days of working code — today isn't new syntax, it's stepping back and asking: could another engineer open `expense_tracker.py` cold and understand it in 10 minutes? That's the literal promise from the project's own Day 1 README. Clean code is what separates code that passes a code review from code that doesn't.

---

## Lesson: Principles, Audited Against Real Code

- **Naming** — already strong: `is_valid_amount`, `total_by_category`, `RecurringExpense` are all self-explanatory.
- **DRY** — already applied for real: `@log_call` (Day 14) exists specifically to avoid repeating `logging.info(...)` in every function.
- **Magic numbers/strings** — already avoided: `DATA_FILE` is a single named constant instead of a repeated literal path.
- **Avoid deep nesting** — `load_expenses()`'s one level of `if/else` inside a `for` inside a `with` is reasonable, not a violation.
- **Comments explain *why*, not *what*** — self-documenting naming does most of the work here; worth a periodic skim for comments that just restate the next line.
- **Consistent docstrings/type hints** — present on every function, a real marker of professional code.

---

## Tooling: `black` and `ruff` (First Time)

**`black`** — opinionated auto-formatter; enforces one consistent style with zero manual debate.
**`ruff`** — fast linter; catches unused imports/variables, style issues, and some real bugs without running the code.

```bash
venv\Scripts\activate
black --check projects/expense_tracker/src/expense_tracker.py   # preview only
black projects/expense_tracker/src/expense_tracker.py            # apply formatting
ruff check projects/expense_tracker/src/expense_tracker.py       # lint (subcommand, not a flag — unlike black's --check)
ruff check --fix projects/expense_tracker/src/expense_tracker.py # auto-fix what's safely fixable
```

**Real results today:**
- `black` reformatted the file (whitespace/style only, confirmed via `git diff` — no logic changes).
- `ruff check --fix` auto-sorted the import block (`I001`) — safe, cosmetic.
- Six findings deliberately **not** fixed today, triaged by priority:
  - `RUF013` (implicit `Optional` on `date: str = None`, x2) — Good to Know, purely a typing-correctness nit, zero runtime effect.
  - `DTZ005` (`datetime.now()` with no timezone) — Learn Later, irrelevant for a single-user local app with no multi-timezone need.
  - `LOG015` (using the root logger directly, x3) — Good to Know, real best practice (`logging.getLogger(__name__)` instead of bare `logging.info`), but a broader refactor touching every log call — deferred to a future cleanup pass rather than bolted onto today.

---

## The Real Gap Found and Fixed

**Discovery:** `is_valid_category()` was built and tested back on Day 11 (`day11_regex_datetime.py`) — but was never actually wired into `add_expense()` in the live project. `category = input(...).strip().title()` went straight through with zero validation the entire time. Confirmed by direct inspection, not assumption.

**The fix:**
1. Copied `is_valid_category()` into `expense_tracker.py` (matching the existing pattern used for `is_valid_amount()` — no cross-folder imports, avoiding the Day 13 import-path headache).
2. Added a category check in `add_expense()`, `raise ValueError(...)` on failure, same pattern as the amount check.
3. **Resolved a real ambiguity:** with two different validation failures both landing in one `except ValueError` block, a hardcoded message would show the wrong text for whichever error *didn't* actually happen. Fixed by printing `str(e)` — the exception's own message — instead of a hardcoded string, so the correct, specific message always displays regardless of which validation failed.

**Verified end-to-end:** bad category + bad amount → correct category-specific message. Valid category + bad amount → correct amount-specific message. Both directions confirmed working.

**Side discovery while testing:** typing `"F00d"` produced the error message `'F00D'` (all caps `D`) — not a bug. `.title()` runs *before* validation, and since `0` isn't a letter, Python's `.title()` treats the character after it as the start of a new "word," capitalizing it. A small but real illustration of why transformation order matters.

---

## Interview Questions (Day 17 Level)

1. What's the difference between what `black` does and what `ruff` does?
2. Why is `ruff check` a subcommand while `black --check` is a flag — what does that reveal about how each tool is structured?
3. What does "implicit Optional" mean, and why does `date: str = None` trigger it?
4. Walk through why hardcoding an error message in an `except` block can become misleading once more than one validation can fail there.
5. What's the risk of a validation function existing and being tested, but never actually being called anywhere in the real application?

---

## Resume Relevance

> "Conducted a clean-code review of a Python CLI application using black and ruff, identified and fixed an unused validation function, and resolved an error-message ambiguity in exception handling."

---

## Next Steps

Phase 1's **skills checklist** is now complete — but Phase 1 itself isn't finished. Per `ROADMAP.md`'s Project Milestones, Phase 1 includes four projects: Expense Tracker (done), Password Manager (CLI), Contact Book with Search, and Task Scheduler. Next up: **Project 2 — Password Manager (CLI)**, applying everything from Days 1–17 to a new build from scratch.

---

## ✅ Day 17 Checklist

- [x] `black`/`ruff` run for the first time; output read and understood.
- [x] `is_valid_category()` gap found by direct code inspection.
- [x] Category validation wired into `add_expense()`.
- [x] Error-message ambiguity resolved (`str(e)` instead of hardcoded text).
- [x] End-to-end tested: both validation failure paths show correct, specific messages.
- [ ] Code committed to Git.
- [ ] `PROGRESS.md` synced (Current Day, Overall Progress notes, Project 1 description).
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 17 complete."**

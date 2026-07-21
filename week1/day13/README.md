# Week 1, Day 13: Testing with Pytest

> **Learning Objectives:**
> 1. Understand why automated tests replace manually re-running the program after every change.
> 2. Install and run `pytest`; understand its `test_*` naming-convention-based auto-discovery.
> 3. Write tests using plain `assert` statements.
> 4. Use `pytest.raises()` to test that code correctly raises exceptions (Day 12 callback).
> 5. Understand multi-folder project structure with `pytest.ini` + `pythonpath`, so tests can import code from anywhere in the repo.
> 6. Recognize a test that silently passes without testing anything — and why that's worse than no test at all.

---

## Business Motivation

This week alone: `KeyError: 'date'`, a misplaced-parenthesis `TypeError`, a `self.date` defaulting-to-`None` bug, a CSV schema mismatch. Every one was caught by manually running the program and hitting the error. That doesn't scale — you can't re-click through every menu option by hand after every change. Automated tests check your code's behavior in seconds, every time, without you lifting a finger.

---

## Lesson 1: pytest Basics

**Install/verify:**
```bash
pytest --version
```

**Naming convention pytest relies on — nothing else:**
- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_*`

Get the name wrong and pytest silently never runs it — no error, no warning.

**A test is just a function with an `assert`:**
```python
def test_format_currency_basic():
    assert format_currency(500) == "INR500.00"
```
`assert` true → passes silently. `assert` false → pytest reports the failure with expected-vs-actual diff.

**Testing exceptions (Day 12 callback):**
```python
def test_parse_amount_raises_on_bad_input():
    with pytest.raises(ValueError):
        parse_amount("abc")
```

**Run:**
```bash
pytest         # quiet
pytest -v      # verbose — shows each test by name and PASSED/FAILED
```

---

## Lesson 2: Multi-Folder Import Resolution (Real Problem, Real Fix)

Hit for real today: moving `test_money_utils.py` from `src/` (where it worked by accident, sitting next to `money_utils.py`) into `tests/` broke the import — `Import "money_utils" could not be resolved`.

**Why:** pytest only auto-adds a test file's *own* folder to the import path. Once the test moved out of `src/`, that folder dropped off the path entirely.

**The fix — `pytest.ini` at the repo root:**
```ini
[pytest]
pythonpath =
    src
    projects/expense_tracker/src
```
This explicitly tells pytest which folders to search for imports, regardless of where any given test file lives — the correct setup for a repo with more than one source folder.

**Rule going forward:** always run `pytest -v` from the repo root (`C:\Users\Viraj\Documents\bootcamp-python`), not from inside a subfolder — it then discovers and runs every test across the whole project in one pass.

---

## Exercise 13.1 — `tests/test_day11_regex_datetime.py`

8 tests written against Day 11's `is_valid_amount`, `is_valid_category`, `extract_numbers`, `days_between`. Two real bugs caught along the way — both worth remembering:

**Bug 1 — a test that always "passes" without testing anything:**
```python
def test_is_valid_amount_rejects_three_decimals():
    return test_is_valid_amount_rejects_three_decimals   # exits immediately
    assert is_valid_amount("450.505") == ...              # never reached
```
`return` exits the function before the `assert` line ever runs. pytest reported `PASSED` — because a test with no assertion reached always passes by default. Caught via pytest's own `PytestReturnNotNoneWarning`. Fixed by deleting the `return` and asserting for real: `assert is_valid_amount("450.505") == False` (3 decimal places exceeds the pattern's `{1,2}` limit).

**Bug 2 — testing the function's own name instead of calling it:**
```python
assert test_is_valid_category_accepts_letters_only == True   # wrong — compares the test to itself
```
Fixed to actually call the function under test: `assert is_valid_category("Food") == True`.

**Final result:** 10/10 passing (2 from `test_money_utils.py` + 8 from `test_day11_regex_datetime.py`), zero warnings.

---

## Common Mistakes (Day 13)

| Mistake | Fix |
|---------|-----|
| Test function not prefixed `test_` | Silently never runs |
| `return` before an `assert` | Function exits early, assertion never reached, test "passes" without checking anything |
| Asserting against the test's own name/reference instead of calling the real function | Always double check you're calling the actual function under test |
| One giant test checking many things | Split into small, named tests — a failure instantly tells you which behavior broke |
| Relative imports breaking when a test moves folders | Fix at the project level with `pytest.ini` + `pythonpath`, not by moving tests back next to source files |

---

## Interview Questions (Day 13 Level)

1. How does pytest know which functions are tests, with no configuration?
2. What's the danger of a test function that never reaches an `assert`?
3. What does `pytest.raises(ValueError)` do, and when would you use it?
4. Why did moving a test file into `tests/` break its import, and how was it fixed?
5. What's the difference between a failing test meaning "the code is broken" vs. "the test's expectation is wrong" — how do you tell which is true?

---

## Resume Relevance

> "Wrote and debugged an automated pytest test suite for a Python CLI application, including exception-based test cases and multi-module import path configuration via pytest.ini."

---

## Next Lesson Preview (Day 14)

**Topic:** Decorators & Generators — per the roadmap's Phase 1 skill order.

---

## ✅ Day 13 Checklist

- [x] pytest installed and verified.
- [x] First test written against `money_utils.py`, failure correctly diagnosed and fixed.
- [x] `pytest.ini` created to resolve multi-folder imports.
- [x] `tests/test_day11_regex_datetime.py` — 8 tests written, 2 real bugs found and fixed.
- [x] Full suite passes: 10/10, zero warnings.
- [ ] Code committed to Git.
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 13 complete."**

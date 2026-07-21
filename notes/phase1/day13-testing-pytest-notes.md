# Day 13: Testing with Pytest — Notes

## 1. Revision Notes

**Why automated tests:** manually re-running the program after every change doesn't scale. A test suite checks every function's behavior in seconds, repeatably, without you touching the keyboard.

**pytest discovers tests by name alone** — files must match `test_*.py`/`*_test.py`, functions must start with `test_`. No config, no registration — but also no error if you get the name wrong; it just silently never runs.

**A test = a function with an `assert`.** True → passes silently. False → pytest shows expected vs. actual with a diff.

**A failing test has two possible causes** — the code under test is genuinely broken, OR the test's own expectation was wrong to begin with. Both happened today (real `money_utils.py` docstring said `INR`, not `₹` — the test's assumption was wrong, not the code). Always check which side is actually correct before "fixing" either one.

**The most dangerous kind of test: one that never reaches its `assert`.** A `return` (or any early exit) before the assertion means the test always reports `PASSED` without checking anything at all — worse than no test, because it creates false confidence. pytest's `PytestReturnNotNoneWarning` is one signal this happened; the real habit is reading your own test body and asking "does execution actually reach the assert line?"

**Multi-folder projects need explicit import path config.** pytest only auto-adds a test file's own folder to the import path. A `pytest.ini` at the project root with a `pythonpath` list fixes this once, for the whole project, regardless of where any individual test file lives.

**`pytest.raises()`** tests that code correctly raises an exception — the Day 12 callback: testing the *failure* path, not just the happy path.

---

## 2. Cheat Sheet

```bash
pytest --version      # check installed
pytest                # run all tests, quiet
pytest -v             # run all tests, verbose (shows each by name)
pytest path/to/file.py -v   # run just one file
```

```python
# Basic test
def test_something():
    assert my_function(x) == expected_value

# Testing an exception is raised
import pytest

def test_raises_on_bad_input():
    with pytest.raises(ValueError):
        my_function("bad input")

# pytest.ini at repo root — fixes multi-folder imports
# [pytest]
# pythonpath =
#     src
#     projects/expense_tracker/src
```

**Reading a failure:**
```
E    AssertionError: assert 'INR500.00' == '₹500.00'
E      - ₹500.00      <- expected (what your test said)
E      ? ^
E      + INR500.00    <- actual (what the function really returned)
```

---

## 3. Active Recall Questions

1. How does pytest decide which functions in a file are tests?
2. What happens if a test function has a `return` statement before its `assert` line?
3. Given a failing test, what are the two possible explanations, and how do you decide which one is true?
4. Why did moving a test file from `src/` into `tests/` break its import — what specifically does pytest add to the import path by default?
5. What does `pytest.ini`'s `pythonpath` setting actually do?
6. What is `pytest.raises()` used for, and what would today's `parse_amount()` test using it look like?
7. Why is a test with no reachable assertion worse than having no test at all?
8. What's the difference between `assert x == True` and just `assert x` — does it matter here?

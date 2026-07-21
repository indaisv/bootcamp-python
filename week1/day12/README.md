# Week 1, Day 12: Exception Handling & Logging

> **Learning Objectives:**
> 1. Use `try`/`except` to catch expected failures instead of letting the program crash.
> 2. Know the difference between a bare `except:` (bad) and catching specific exception types (correct).
> 3. Recognize the common built-in exceptions: `ValueError`, `TypeError`, `KeyError`, `FileNotFoundError`, `ZeroDivisionError`.
> 4. Use `raise` to signal your own validation failures using Python's exception system.
> 5. Set up the `logging` module for the first time — timestamped, severity-leveled records instead of `print()` debugging.
> 6. Apply both to the real Expense Tracker: proper validation via `raise`, and logging around save/load.

---

## Business Motivation

This week alone you've hit two real crashes: `KeyError: 'date'` when the CSV was missing a column, and a `TypeError` from a misplaced parenthesis in an f-string. Both times, the whole program died and dumped a raw traceback — fine while you're sitting there debugging, useless the moment this needs to run unattended or for someone else.

Two problems, two tools:
- **Exception handling** — catch *expected* failures (bad input, missing file, missing dict key) and respond sensibly instead of crashing outright.
- **Logging** — once a program isn't running live in front of you, `print()` output is gone forever. A log file is a permanent, timestamped record you can open tomorrow and actually investigate.

---

## Lesson 1: `try`/`except`

```python
try:
    risky_code()
except SomeSpecificError:
    handle_it()
```

**Rule #1: never use a bare `except:`.** It catches *everything*, including bugs you didn't anticipate, and hides them silently.

```python
# Bad — catches literally everything, including typos in your own code
try:
    result = 10 / 0
except:
    print("something went wrong")

# Good — catches only what you expect, lets real bugs surface
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
```

**Multiple exception types, and `finally`:**
```python
try:
    value = int(user_input)
except ValueError:
    print("Not a valid number")
except TypeError:
    print("Wrong type entirely")
finally:
    print("This runs no matter what — success or failure")
```

**`raise` — triggering your own exception:**
```python
def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive")
```
`raise` is how *you* signal "this input is unacceptable" using Python's own exception system, instead of a manual `print()` + `return`.

---

## Lesson 2: Common Built-in Exceptions (Must Know)

| Exception | When it happens |
|-----------|------------------|
| `ValueError` | Right type, bad value — `int("abc")` |
| `TypeError` | Wrong type entirely — `"5" + 5` |
| `KeyError` | Dict key doesn't exist — hit this literally, twice, this week |
| `FileNotFoundError` | File doesn't exist — currently dodged with `os.path.exists()` |
| `ZeroDivisionError` | Division by zero |

**Tie-back:** `os.path.exists()` in `load_expenses()` *avoids* `FileNotFoundError` by checking first. An equally valid alternative is `try`/`except FileNotFoundError` — attempt to open it, only handle the failure if it actually happens. Both are correct; `try`/`except` is generally preferred when failure is the *exception*, not the *norm*.

---

## Lesson 3: The `logging` Module (First Time — Full Setup)

**What it is:** Python's built-in system for recording events with a timestamp and a severity level, instead of scattering `print()` calls everywhere.

**Why `print()` doesn't scale:** no timestamps, no severity (minor note vs. real problem?), can't be toggled on/off, vanishes the moment the terminal closes.

**The 5 severity levels, low to high:** `DEBUG` → `INFO` → `WARNING` → `ERROR` → `CRITICAL`.

**First working setup:**
```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("Amount was unusually high")
logging.error("Failed to save expenses")
```

`level=logging.INFO` means: log `INFO` and anything *more severe* — but silently skip `DEBUG`. This is the standard way to control log noise without deleting log calls from the code.

---

## Common Mistakes (Day 12)

| Mistake | Fix |
|---------|-----|
| Bare `except:` | Always name the specific exception |
| Catching an exception and doing nothing (`except: pass`) | At minimum, log it — silent failures are the hardest bugs to find |
| Using `print()` for errors in real code | Use `logging.error()` — persists, has a timestamp |
| Setting `level=logging.DEBUG` in production | Floods the log file; use `INFO` or higher normally |
| `raise` with no message | `raise ValueError("Amount must be positive")`, not just `raise ValueError()` |

---

## Best Practices (Day 12)

1. **Catch specific exceptions, never bare `except:`.**
2. **Log errors, don't just print them,** anywhere the code isn't running live in front of you.
3. **`raise` with a clear message** — the caller (or future you, reading the log) needs to know *why* it failed.
4. **`finally` for cleanup that must always run**, regardless of success or failure.
5. **Don't catch an exception you don't know how to handle** — let unexpected bugs surface instead of hiding them.

---

## Exercise 12.1: `day12_exceptions_logging.py`

```python
"""
day12_exceptions_logging.py
Practicing try/except and the logging module.
Author: Viraj
"""
import logging

logging.basicConfig(
    filename="day12.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def safe_divide(a: float, b: float) -> float | None:
    """
    Divide a by b. If b is 0, log a warning and return None instead of crashing.
    """
    # TODO: try the division, except ZeroDivisionError, log a warning, return None
    pass


def parse_amount(text: str) -> float:
    """
    Convert text to a float. If it fails, log an error and RAISE a ValueError
    with a clear message (don't swallow it — the caller needs to know it failed).
    """
    # TODO: try float(text), except ValueError: log it, then raise ValueError(...)
    pass


def read_file_safe(path: str) -> str:
    """
    Read and return a file's full contents. If the file doesn't exist,
    log an error and return an empty string instead of crashing.
    """
    # TODO: try open()+read(), except FileNotFoundError, log error, return ""
    pass


def test_all():
    print(safe_divide(10, 2))    # 5.0
    print(safe_divide(10, 0))    # None (check day12.log for the warning)
    try:
        parse_amount("abc")
    except ValueError as e:
        print(f"Caught it: {e}")
    print(read_file_safe("nonexistent_file.txt"))  # "" (check day12.log for the error)


if __name__ == "__main__":
    test_all()
```

Fill in the three `TODO`s. Run it, then open `day12.log` and confirm the warning/error entries actually got written with timestamps.

---

## Project Integration Preview

Once the warm-up passes, the plan for `expense_tracker.py`:
- Swap `add_expense()`'s manual `if not is_valid_amount(...): print(...); return` for a `raise ValueError(...)`-based pattern.
- Add `logging` calls around `save_expenses()`/`load_expenses()` so failures leave a permanent trace instead of a printed line that's easy to miss.

---

## Interview Questions (Day 12 Level)

1. Why is a bare `except:` considered bad practice?
2. What's the difference between `ValueError` and `TypeError`? Give an example of each.
3. What does `finally` guarantee, and when would you use it?
4. Why use `logging` instead of `print()` for error reporting?
5. What do the 5 logging severity levels mean, and what does setting `level=logging.INFO` actually filter out?
6. When would you choose `try`/`except FileNotFoundError` over checking `os.path.exists()` first?

---

## Resume Relevance

> "Implemented exception handling and a logging system in a Python CLI application, replacing print-based debugging with timestamped, severity-leveled logs and proper validation via raised exceptions."

---

## Next Lesson Preview (Day 13)

**Topic:** Testing with Pytest — writing automated tests for the functions built across Days 5–12, instead of manually running the program and eyeballing the output.

---

## ✅ Day 12 Checklist

- [ ] `day12_exceptions_logging.py` created — all three `TODO`s implemented.
- [ ] `day12.log` confirmed to contain timestamped warning/error entries.
- [ ] `add_expense()` updated to `raise ValueError` instead of print-and-return.
- [ ] Logging added around `save_expenses()`/`load_expenses()`.
- [ ] Code committed to Git.
- [ ] I can answer all 6 interview questions.

---

**When you are done, tell me: "Day 12 complete."**

# Day 12: Exception Handling & Logging — Notes

## 1. Revision Notes

**Why this mattered:** every crash hit earlier this week (`KeyError`, misplaced-parenthesis `TypeError`) killed the program outright with a raw traceback. `try`/`except` catches *expected* failures and lets the program respond sensibly instead of dying. `logging` replaces `print()` debugging with a permanent, timestamped record — `print()` output vanishes the moment the terminal closes; a log file doesn't.

**`try`/`except` — never use a bare `except:`.** It silently catches everything, including real bugs you didn't anticipate and would rather know about. Always name the specific exception (`except ValueError:`, `except FileNotFoundError:`).

**Common built-in exceptions:**
- `ValueError` — right type, bad value (`int("abc")`)
- `TypeError` — wrong type entirely (`"5" + 5`)
- `KeyError` — dict key doesn't exist
- `FileNotFoundError` — file doesn't exist
- `ZeroDivisionError` — division by zero

**`raise`** is how *you* trigger an exception on purpose, to signal "this input is unacceptable" — using Python's own exception system instead of a manual `print()` + `return`. Always `raise` with a message: `raise ValueError("Amount must be positive")`, not just `raise ValueError()`.

**The `logging` module** — severity levels low to high: `DEBUG` → `INFO` → `WARNING` → `ERROR` → `CRITICAL`. Setting `level=logging.INFO` in `basicConfig()` logs `INFO` and anything more severe, silently skipping `DEBUG` — the standard way to control log noise without deleting log calls.

**Real bugs hit today, worth remembering:**
- A test/function with an early exit (`return` or a misplaced line) before the code that's supposed to run — the check-then-do pattern needs the "do" part to actually be reachable. Happened twice: `raise` sitting outside the `except` block (ran unconditionally instead of only on failure), and a `logging.warning()` call sitting outside the function entirely due to indentation (ran once on file load, not per call).
- Matching log **severity to intent** — a missing file logged as `warning` instead of `error` doesn't break anything technically, but undermines the whole point of severity levels: being able to scan a log file later and immediately tell what's serious.
- `.gitignore` needs `*.log` added — log files are generated output, same reasoning as `*.csv`; they shouldn't be committed to version control.

---

## 2. Cheat Sheet

```python
# Basic try/except — never bare except:
try:
    risky_code()
except SpecificError:
    handle_it()

# Multiple exception types + finally
try:
    value = int(user_input)
except ValueError:
    print("Not a valid number")
except TypeError:
    print("Wrong type entirely")
finally:
    print("Runs no matter what")

# Raising your own exception
def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive")

# logging setup (do this once, top of file)
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Normal event happened")
logging.warning("Something worth noting, not broken")
logging.error("Something failed")
```

**Combining raise + except + logging (the actual project pattern):**
```python
try:
    if not is_valid(x):
        raise ValueError(f"Invalid input: '{x}'")
    # ... success path ...
    logging.info("Success details here")
except ValueError as e:
    logging.error(str(e))
    print("User-friendly error message")
```

---

## 3. Active Recall Questions

1. Why is a bare `except:` considered bad practice?
2. What's the difference between `ValueError` and `TypeError`?
3. What does `finally` guarantee?
4. Why use `logging` instead of `print()` for error reporting in real code?
5. What do the 5 logging severity levels mean, low to high?
6. What does `level=logging.INFO` in `basicConfig()` actually filter?
7. If a `raise` statement is indented at the same level as `try` instead of inside `except`, when does it fire?
8. Why should `.gitignore` exclude `*.log` files?
9. What's the risk of catching an exception and doing nothing in the `except` block (`except: pass`)?

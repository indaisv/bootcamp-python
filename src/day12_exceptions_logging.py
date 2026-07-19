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
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        logging.warning(f"Attempted to divide {a} by zero")
        return None

def parse_amount(text: str) -> float:
    """
    Convert text to a float. If it fails, log an error and RAISE a ValueError
    with a clear message (don't swallow it — the caller needs to know it failed).
    """
    # TODO: try float(text), except ValueError: log it, then raise ValueError(...)
    try:
        return float(text)
    except ValueError:
        logging.warning(f"Failed converting text to a float{text}")
        raise ValueError(f"Failed converting text to a float{text}")


def read_file_safe(path: str) -> str:
    """
    Read and return a file's full contents. If the file doesn't exist,
    log an error and return an empty string instead of crashing.
    """
    # TODO: try open()+read(), except FileNotFoundError, log error, return ""
    try:
        with open(path) as f: return f.read()
    except FileNotFoundError:
        logging.error(f"File doesnt exist")
        return ""

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
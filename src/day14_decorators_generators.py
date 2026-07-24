"""
day14_decorators_generators.py
Practicing decorators and generators.
Author: Viraj
"""
import functools
import logging
import time

logging.basicConfig(
    filename="day14.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_call(func):
    """Decorator: logs the function's name every time it's called."""
    # TODO: define wrapper(*args, **kwargs), log func.__name__ via logging.info,
    # call func and return its result. Don't forget @functools.wraps(func).
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def timer(func):
    """Decorator: logs how long the function took to run, in seconds."""
    # TODO: record time.time() before calling func, again after,
    # log the difference. Hint: same wrapper shape as log_call.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logging.info(f"Function {func.__name__} took {end - start} seconds to run")
        return result
    return wrapper


@log_call
def add(a: int, b: int) -> int:
    return a + b


@timer
def slow_function():
    time.sleep(1)
    return "done"


def count_down(n: int):
    """Generator: yields n, n-1, ..., 1."""
    # TODO: use a while or for loop with yield instead of building a list
    while n > 0:
        yield n
        n -= 1


def filter_large_amounts(amounts: list, threshold: float):
    """Generator: yields only amounts greater than threshold, one at a time."""
    # TODO: loop over amounts, yield the ones > threshold
    for amount in amounts:
        if amount > threshold:
            yield amount


def test_all():
    print(add(3, 4))              # 7 — check day14.log for "Calling add"
    print(slow_function())        # "done" — check day14.log for the timing entry

    for num in count_down(5):
        print(num)                 # 5, 4, 3, 2, 1

    amounts = [200, 1500, 300, 5000, 50]
    for amt in filter_large_amounts(amounts, 500):
        print(amt)                 # 1500, 5000


if __name__ == "__main__":
    test_all()
# Week 1, Day 14: Decorators & Generators

> **Learning Objectives:**
> 1. Understand what a decorator is and why it avoids repeating the same wrapping logic across functions.
> 2. Write a decorator using the `def wrapper(*args, **kwargs)` pattern and apply it with `@`.
> 3. Always use `functools.wraps(func)` to preserve the original function's identity.
> 4. Understand what `yield` does differently from `return`, and why generators save memory.
> 5. Recognize that a generator can only be iterated once.
> 6. Build a logging decorator and a timing decorator; build two small generators.

---

## Business Motivation

Right now, every function in `expense_tracker.py` that needs logging (`save_expenses`, `load_expenses`) has a manually typed `logging.info(...)` line inside it — repetitive, and easy to forget on new functions. A decorator lets you write that logic once and apply it anywhere with one line.

Separately: `load_expenses()` reads the **entire** CSV into a RAM list before doing anything. Fine for hundreds of rows. Completely unworkable at real scale — a generator produces values one at a time, on demand, instead of building the whole list upfront.

---

## Lesson 1: Decorators

**What it is:** a function that wraps another function to add behavior before/after it runs, without touching the original function's code.

**The shape every decorator follows:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # do something BEFORE
        result = func(*args, **kwargs)
        # do something AFTER
        return result
    return wrapper
```
`*args, **kwargs` let `wrapper` accept whatever arguments the wrapped function needs — the decorator doesn't know in advance what that'll be.

**The `@` syntax:**
```python
@my_decorator
def greet(name):
    print(f"Hello, {name}")
```
`@my_decorator` is shorthand for `greet = my_decorator(greet)`.

**A real one — automatic call logging:**
```python
import logging
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b
```

**`functools.wraps(func)` — Must Know.** Without it, `wrapper` silently replaces the original function's `__name__` and docstring, breaking debugging and any code that inspects function metadata. Always include it.

**Good to know (later):** decorators that take their own arguments (`@retry(times=3)`). Not needed yet.

---

## Lesson 2: Generators

**What it is:** a function that produces values one at a time, pausing between each, instead of computing and returning everything at once.

**`yield` instead of `return` — the whole difference:**
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```
Calling `count_up_to(5)` returns a **generator object** immediately — the function body only runs as values are pulled, one `yield` at a time:
```python
for num in count_up_to(5):
    print(num)   # 1, 2, 3, 4, 5 — one at a time
```

**Why it saves memory:**
```python
def make_list(n):
    return [i for i in range(n)]   # allocates ALL of it immediately

def make_generator(n):
    for i in range(n):
        yield i                     # one value at a time, almost no memory used
```

**Critical gotcha: generators are one-shot.** Once a `for` loop exhausts a generator, looping over the *same object* again yields nothing. Convert to a list (`list(my_generator)`) if you need to reuse it, or call the generator function again for a fresh one.

---

## Common Mistakes (Day 14)

| Mistake | Fix |
|---------|-----|
| `wrapper` missing `*args, **kwargs` | Breaks on any function that takes arguments |
| Forgetting `return wrapper` | Decorator returns `None`; decorated function becomes uncallable |
| Forgetting `@functools.wraps(func)` | Silently corrupts `__name__`/docstring |
| Using `return` where `yield` was intended | No laziness, no memory savings — it's just a normal function |
| Re-iterating an exhausted generator | One-shot only — convert to a list first if reuse is needed |
| Expecting a generator function call to return a list immediately | Returns a generator object — nothing runs until iterated |

---

## Best Practices (Day 14)

1. **Always `functools.wraps(func)`** inside a decorator — no exceptions.
2. **Use decorators for cross-cutting concerns** (logging, timing) — not for core business logic, which belongs in the function itself.
3. **Use generators when processing large or unknown-size data**, especially file reads — don't load everything into memory just because it's convenient.
4. **Convert a generator to a list explicitly** (`list(...)`) the moment you know you need to iterate it more than once.

---

## Exercise 14.1: `day14_decorators_generators.py`

```python
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
    pass


def timer(func):
    """Decorator: logs how long the function took to run, in seconds."""
    # TODO: record time.time() before calling func, again after,
    # log the difference. Hint: same wrapper shape as log_call.
    pass


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
    pass


def filter_large_amounts(amounts: list, threshold: float):
    """Generator: yields only amounts greater than threshold, one at a time."""
    # TODO: loop over amounts, yield the ones > threshold
    pass


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
```

---

## Project Integration Preview

Once the warm-up passes, the plan for `expense_tracker.py`: replace the manual `logging.info(...)` lines inside `save_expenses()`/`load_expenses()` with a `@log_call`-style decorator applied directly above each function definition — same behavior, written once instead of copy-pasted.

---

## Interview Questions (Day 14 Level)

1. What does `@my_decorator` actually do, under the hood?
2. Why does a decorator's inner function need `*args, **kwargs`?
3. What does `functools.wraps(func)` fix, and what breaks without it?
4. What's the practical difference between `return` and `yield`?
5. Why are generators more memory-efficient than building a full list?
6. Why can a generator only be iterated once, and how do you work around that if needed?

---

## Resume Relevance

> "Implemented Python decorators for cross-cutting logging and performance timing, and used generators for memory-efficient lazy iteration over data."

---

## Next Lesson Preview (Day 15)

**Topic:** Virtual Environments & pip — isolating project dependencies properly, per the roadmap's Phase 1 skill order.

---

## ✅ Day 14 Checklist

- [ ] `day14_decorators_generators.py` created — all four `TODO`s implemented.
- [ ] `day14.log` confirmed to contain entries from both `log_call` and `timer`.
- [ ] `expense_tracker.py`'s manual logging lines replaced with a decorator.
- [ ] Code committed to Git.
- [ ] I can answer all 6 interview questions.

---

**When you are done, tell me: "Day 14 complete."**

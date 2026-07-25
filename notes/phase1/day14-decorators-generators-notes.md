# Day 14: Decorators & Generators — Notes

## 1. Revision Notes

**Decorators exist to avoid repeating the same wrapping logic across many functions.** Instead of manually adding a `logging.info(...)` line inside every function that needs it, a decorator writes that behavior once and applies it to any function with `@decorator_name`.

**The shape every decorator follows:**
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```
`*args, **kwargs` let `wrapper` accept whatever arguments the wrapped function needs — the decorator doesn't know that in advance. `@my_decorator` above a function is shorthand for `func = my_decorator(func)`.

**`functools.wraps(func)`** — without it, the wrapped function silently loses its real `__name__`/docstring, replaced by `wrapper`'s. Always include it; it's a one-line fix with no downside.

**Generators produce values one at a time, on demand, instead of building a full list upfront.** The only syntactic difference from a normal function is `yield` instead of `return`. Calling a generator function doesn't run its body — it returns a generator object; the body only executes as values are pulled out, one `yield` at a time (via a `for` loop or `next()`).

**Why generators matter:** memory. A list comprehension building 10 million items allocates all of them immediately. A generator doing the same produces one value at a time — each exists only for the instant it's used.

**The generator gotcha that matters most:** they're one-shot. Once exhausted (looped over fully), iterating the *same* generator object again yields nothing. If you need the data twice, either materialize it into a list (`list(my_generator)`) once, or call the generator function again for a fresh object.

**Applied today, for real:** `save_expenses()` and `load_expenses()` in the actual Expense Tracker were switched from manual `logging.info(...)` lines to a shared `@log_call` decorator — a genuine DRY (Don't Repeat Yourself) improvement, with a conscious trade-off: the decorator logs *that* the function was called, but not the specific detail (expense count) the old manual line included. A real, deliberate simplicity-vs-detail decision, not just following instructions blindly.

---

## 2. Cheat Sheet

```python
import functools
import logging

# --- Decorator template ---
def my_decorator(func):
    @functools.wraps(func)          # ALWAYS include this
    def wrapper(*args, **kwargs):
        # do something before
        result = func(*args, **kwargs)
        # do something after
        return result
    return wrapper

@my_decorator
def some_function(x, y):
    return x + y

# --- Logging decorator (real pattern used in the project) ---
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# --- Timing decorator ---
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} took {time.time() - start} seconds")
        return result
    return wrapper

# --- Generator template ---
def my_generator(n):
    for i in range(n):
        yield i

for value in my_generator(5):     # runs lazily, one value per iteration
    print(value)

# Materializing a generator into a reusable list
values = list(my_generator(5))
```

---

## 3. Active Recall Questions

1. What does `@my_decorator` actually expand to behind the scenes?
2. Why does a decorator's `wrapper` function need `*args, **kwargs`?
3. What specifically breaks if you forget `@functools.wraps(func)` inside a decorator?
4. What's the one-word syntax difference between a normal function and a generator function?
5. Why is a generator more memory-efficient than returning a full list?
6. What happens if you try to loop over a generator a second time after it's already been fully consumed?
7. In today's project change, what specific detail did the Expense Tracker's logging lose when `logging.info(...)` calls were replaced by `@log_call`, and why was that an acceptable trade-off?
8. If you needed to iterate the same generated data twice, what are your two options?

# Day 6 — Functions & Scope

## Revision Notes

**The mutable default argument trap** — default argument values are created **once**, when Python reads the `def` line, not fresh on every call. A mutable default (`def f(items=[])`) means every call that doesn't supply its own `items` silently shares and accumulates onto the *same* list object across calls. Fix: default to `None`, then build a fresh mutable object inside the function body if it's `None`:
```python
def add_item_safe(item, collection=None):
    if collection is None:
        collection = []   # new object, created fresh, every call
    collection.append(item)
    return collection
```

**`return` vs `print()` — not interchangeable.**
- A function that `print()`s hands nothing back — its result only exists as text on a terminal, unusable by any other code.
- A function that `return`s hands back real data — the caller decides what to do with it (print it, save it, compare it, test it).
- Rule of thumb: functions that *calculate* should `return`. Functions that *display* can `print()`. Often a function that does both should be split into two.

**Local scope** — variables created inside a function only exist inside that function. They vanish once the function returns. This is *why* data has to be explicitly passed in (as a parameter) or handed back out (via `return`) — a function can't reach into another function's variables, and nothing outside can see a function's local variables either.

**Why pass data in as a parameter instead of using a global variable** — two real reasons:
1. **Traceability** — a function's parameters tell you exactly what it depends on just by reading the `def` line. A global dependency is invisible until you read the whole function body.
2. **Testability** — a function that takes its data as a parameter can be tested with any fake/small input. A function tied to a global can only ever be tested against whatever that global currently holds.

**Today's real refactor:** `total_by_category()` went from calculating *and* printing, to only calculating and returning a dict. `main()` now does the printing, using the exact same `.items()` loop that used to live inside the function — just relocated to the caller. This is the concrete shape of "split calculation from display."

---

## Cheat Sheet

```python
# Safe mutable default pattern
def f(item, collection=None):
    if collection is None:
        collection = []
    collection.append(item)
    return collection

# Calculation function — returns, never prints
def calculate_total(expenses):
    return sum(e["amount"] for e in expenses)

def calculate_average(expenses):
    if not expenses:
        return 0
    return calculate_total(expenses) / len(expenses)

# Dict-accumulator, returned instead of printed
def total_by_category(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals

# Caller decides what to do with the return value
totals = total_by_category(expenses)
for category, total in totals.items():
    print(f"{category}: INR{total}")
```

---

## Active Recall — Day 6

1. Why is `def f(items=[])` dangerous? What actually happens across multiple calls, mechanically?
2. What's the practical difference between a function that prints its result and one that returns it?
3. What is local scope, in your own words?
4. Why does the Expense Tracker pass `expenses` into every function instead of using a global variable? (Two separate reasons.)
5. In the `total_by_category()` refactor, what moved from the function into `main()`, and what stayed inside the function?
6. Why does `collection = None` (immutable) work safely as a default, but `collection = []` (mutable) doesn't?

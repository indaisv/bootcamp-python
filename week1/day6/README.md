# Week 1, Day 6: Functions & Scope

> **Learning Objectives:**
> 1. Understand parameters, default arguments, and why mutable defaults are dangerous.
> 2. Understand `return` vs `print()` — and why it matters for testing and reuse.
> 3. Understand local vs global scope.
> 4. Refactor the Expense Tracker's functions to `return` data instead of printing directly.

---

## Business Motivation

Right now, `add_expense()`, `view_expenses()`, and `total_by_category()` all work — but they `print()` their results directly instead of `return`-ing them. That's fine for a quick script, but it breaks down the moment you need to:
- **Test** the function (a test checks a *return value*, not what got printed to a terminal).
- **Reuse** the result somewhere else (e.g. save totals to a file, send them in an email, display them in a dashboard).

Today's refactor makes your existing functions usable in more than one context — the actual difference between a script and a real piece of software.

---

## Lesson 1: Parameters & Default Arguments (Quick Review + Deeper)

You've already used default arguments — `tax_rate: float = 0.18` in `invoice_formatter.py`. The rule: parameters with defaults must come *after* parameters without them.

```python
def apply_discount(price: float, discount_percent: float = 10) -> float:
    return price * (1 - discount_percent / 100)

apply_discount(1000)          # uses default 10%
apply_discount(1000, 25)      # overrides to 25%
```

### ⚠️ The Mutable Default Argument Trap

```python
def add_item(item, cart=[]):   # DANGEROUS
    cart.append(item)
    return cart

print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['apple', 'banana']  ← wait, what?
```

**Why this happens:** default argument values are created **once**, when the function is defined — not every time it's called. `cart=[]` is the *same list object* every time you call `add_item()` without passing a cart. It silently accumulates across calls.

**The fix:**
```python
def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart
```

This is exactly the `is None` check from Day 2 — same reasoning, new context.

---

## Lesson 2: `return` vs `print()` — Why It Matters

```python
# Prints, returns nothing usable
def get_total_v1(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total: {total}")

# Returns, caller decides what to do with it
def get_total_v2(expenses):
    total = sum(e["amount"] for e in expenses)
    return total
```

With `get_total_v1`, you can *only* see the total in the terminal. With `get_total_v2`, you can:
```python
total = get_total_v2(expenses)
print(f"Total: {total}")          # print it
save_to_file(total)                 # save it
if total > 10000:                   # make decisions with it
    print("High spender!")
```

**Rule of thumb going forward:** functions that *calculate* something should `return` it. Functions that *display* something can `print()`. Often you'll split what used to be one function into two — a calculator and a printer.

---

## Lesson 3: Local vs Global Scope

```python
def show_total():
    total = 500          # local — only exists inside this function
    print(total)

show_total()
print(total)              # NameError! total doesn't exist out here
```

Variables created inside a function are **local** — they vanish when the function returns. This is exactly why your Expense Tracker passes `expenses` *into* every function as a parameter, instead of functions reaching out to a global variable. You already did this correctly by instinct in Day 5 — today gives you the vocabulary for *why* it was the right call.

**Global variables are usually a smell in this context.** If a function needs data, pass it in as a parameter. If it produces data, `return` it. Reaching for `global` to dodge this is a shortcut that causes bugs later (a function silently depending on state you can't see at the call site).

---

## Exercise 6.1: Warm-up

Create `src/day6_functions.py`:

```python
"""
day6_functions.py
Practicing return vs print, default arguments, and scope.
Author: Viraj
"""


def calculate_total(expenses: list) -> int:
    """Return the sum of all expense amounts. Do NOT print inside this function."""
    # YOUR CODE
    pass


def calculate_average(expenses: list) -> float:
    """Return the average expense amount. Handle the empty-list case (avoid ZeroDivisionError)."""
    # YOUR CODE
    pass


def add_item_safe(item, collection=None) -> list:
    """Demonstrate the mutable default argument fix. Append item, return the list."""
    # YOUR CODE — use the `if collection is None:` pattern from Lesson 1
    pass


def main():
    expenses = [
        {"category": "Food", "amount": 500},
        {"category": "Travel", "amount": 1200},
        {"category": "Bills", "amount": 300},
    ]

    total = calculate_total(expenses)
    average = calculate_average(expenses)
    print(f"Total: INR{total}")
    print(f"Average: INR{average:.2f}")

    cart = add_item_safe("apple")
    cart = add_item_safe("banana", cart)
    print(cart)


if __name__ == "__main__":
    main()
```

**Expected output:**
```
Total: INR2000
Average: INR666.67
['apple', 'banana']
```

---

## Exercise 6.2: Refactor the Expense Tracker

Go back to `projects/expense_tracker/src/expense_tracker.py`. Refactor **`total_by_category()`** so it `return`s the `totals` dict instead of printing inside the function. Then update `main()` to call it and print the result there.

```python
def total_by_category(expenses: list) -> dict:
    """Return {category: total_amount} instead of printing directly."""
    # same accumulator logic as before, but return totals instead of printing it
    pass
```

```python
# in main(), option "3" becomes:
elif choice == "3":
    totals = total_by_category(expenses)
    if not totals:
        print("No expenses recorded yet.")
    else:
        for category, total in totals.items():
            print(f"{category}: INR{total}")
```

**Why only this one function today:** `add_expense` and `view_expenses` are fine to leave printing directly for now (they're inherently "display" actions) — `total_by_category` is the one that's genuinely a *calculation* wearing a print statement, which is exactly the smell this lesson is about spotting.

---

## Common Beginner Mistakes (Day 6)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| `def f(items=[])` | Looks harmless, defaults feel like they reset each call | They don't — use `None` + `if x is None:` |
| Function prints instead of returns | Feels "done" once it displays correctly | Ask: will anything ever need this value besides the terminal? |
| Using a global variable instead of a parameter | Feels like less typing | Breaks testability — pass data in explicitly |
| Forgetting `return` entirely (function implicitly returns `None`) | Easy to forget when refactoring from print-based code | Trace through: what does the caller receive? |

---

## Interview Questions (Day 6 Level)

1. Why is `def f(items=[])` dangerous? Walk through what actually happens across multiple calls.
2. What's the practical difference between a function that prints its result and one that returns it?
3. What is local scope? What happens if you try to access a function's local variable from outside it?
4. Why does the Expense Tracker pass `expenses` into every function instead of using a global variable?

---

## ✅ Day 6 Checklist

- [ ] `day6_functions.py` created — Exercise 6.1 complete.
- [ ] `calculate_total()` and `calculate_average()` return values, don't print internally.
- [ ] Mutable default argument trap explained in your own words.
- [ ] `total_by_category()` refactored to return instead of print.
- [ ] `main()` updated to handle the new return value.
- [ ] Code committed to Git.
- [ ] I can answer all 4 interview questions.

---

**When you are done, tell me: "Day 6 complete."**

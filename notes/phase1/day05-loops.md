# Day 5 — Loops & Control Flow

## Revision Notes

**`for` vs `while`**
- `for`: iterating over something known — a list, `range()`.
- `while`: looping until a *condition* changes, not a known count.
- Menu pattern = `while True` + `break`: loop forever, exit only when the user says so. The exit check lives right where the exit happens.

**`enumerate()`**
- Gives `(index, value)` pairs. Replaces the beginner habit of `range(len(x))`.
- `enumerate(list, start=1)` — numbering starts at 1 for human-readable output.

**`zip()`**
- Walks two (or more) lists together, pair by pair. Stops at the shorter list if lengths differ.
- Use case: parallel columns of data (e.g. categories list + amounts list from a CSV).

**The accumulator pattern** (the core idea of the whole day)
1. Init a variable *before* the loop (`total = 0`, or `totals = {}` for grouped totals).
2. Update it *inside* the loop.
3. Use/print it *after* the loop ends — not inside it, or it prints once per iteration instead of a final answer.
- Grouped version uses `dict.get(key, 0) + value` to accumulate per-category instead of one single number.

**`break` / `continue` / `pass`**
- `break` — exit the loop entirely.
- `continue` — skip the rest of this iteration, keep looping.
- `pass` — do nothing; a placeholder so the file still runs.

**Validating input before converting types**
- `str.isdigit()` check *before* `int()` — never trust raw `input()`.
- If invalid: print a message and `return` early — don't let the function continue with bad data.

**Common bug pattern I hit today:** using the *outer collection* name inside a loop instead of the *loop variable* (e.g. checking `if expenses > 1000` instead of `if amount > 1000`). Always double check which name the `for`/`if` should reference.

---

## Cheat Sheet

```python
# enumerate — index + value
for i, val in enumerate(my_list, start=1):
    ...

# zip — two lists together
for a, b in zip(list1, list2):
    ...

# accumulator — single running total
total = 0
for x in items:
    if condition:
        total += x
print(total)          # outside the loop

# accumulator — grouped totals (dict)
totals = {}
for item in items:
    key = item["category"]
    totals[key] = totals.get(key, 0) + item["amount"]
for key, val in totals.items():
    print(key, val)

# menu loop
while True:
    choice = input(...).strip()
    if choice == "1":
        ...
    elif choice == "2":
        ...
    else:
        print("Invalid option.")
    if choice == "4":
        break

# validate before converting
raw = input(...).strip()
if not raw.isdigit():
    print("Invalid input.")
else:
    value = int(raw)
```

---

## Active Recall — Day 5

1. What's the difference between `for` and `while`? When do you pick each?
2. Why is `enumerate()` preferred over `range(len(x))`?
3. What does `zip()` do if the two lists are different lengths?
4. In the accumulator pattern, why does the `print()` go *outside* the loop, not inside?
5. What's the difference between `break`, `continue`, and `pass`?
6. Why check `.isdigit()` before calling `int()` on user input?
7. In `totals.get(category, 0) + amount`, what does the `0` do, and when does it matter?
8. Why does `choice` from `input()` need to be compared as a string (`"1"`), not an integer (`1`)?
9. What happens if you forget the `break` after handling the exit option in a menu loop?
10. Why does `add_expense` `return` early on invalid input instead of continuing?

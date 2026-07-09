# Day 4 — Lists, Tuples, Sets, Dictionaries

## Revision Notes

**Choosing the right structure is a design decision, not a syntax choice**
| Structure | Ordered? | Mutable? | Duplicates? | Use for |
|---|---|---|---|---|
| List | Yes | Yes | Yes | Sales rows, product names — order matters, will change |
| Tuple | Yes | No | Yes | Fixed records (coordinates), dict keys, "don't touch this" data |
| Set | No | Yes | No | Deduplication, fast membership checks |
| Dict | Insertion-order | Yes | Keys unique | Customer profiles, JSON API responses |

**Lists** — `.append()`/`.insert()`/`.remove()`/`.pop()` all mutate in place and return `None`. Classic bug: `result = my_list.sort()` — `result` is `None`, because `.sort()` sorts in place and returns nothing. Sort first, *then* use the list.

**List comprehensions** — `[expr for item in list if condition]`. Faster and more idiomatic than a manual loop + `.append()`. Used in `build_customer_database()` for `mumbai_customers`.

**Tuples** — immutable. Used when data should never change, or needs to be a dict key (lists can't be — they're unhashable).

**Sets** — automatic deduplication, `O(1)` membership checks (`in` is near-instant vs. scanning a list). Operations: `|` union, `&` intersection, `-` difference. Used in `deduplicate_emails()`.

**Dictionaries — the most-used structure in real business code.**
- `dict.get(key, default)` is the safe alternative to `dict[key]`, which raises `KeyError` if the key is missing. This is the pattern behind `total_by_category()`'s accumulator: `totals.get(category, 0) + amount`.
- `in` on a dict checks **keys only**, not values.
- `.items()` for iterating key+value pairs together — cleaner than `.keys()` + manual lookup.

**The mutable trap, nested version** — `.copy()` is a *shallow* copy: for a list of dicts, the outer list is new, but the inner dicts are still shared references. Modifying `shallow[0]["age"]` still changes the original. Use `copy.deepcopy()` for nested structures.

**Finding the "top" item pattern** (from `build_customer_database`):
```python
top_customer = customers[0]        # assume the first is the max
for c in customers:
    if c["orders"] > top_customer["orders"]:
        top_customer = c
```
This "start with first, compare and replace" pattern generalizes to any max/min-by-field search — worth recognizing on sight.

---

## Cheat Sheet

```python
# Lists
lst.append(x)       # add to end — returns None
lst.sort()           # in-place — returns None, don't reassign!
lst.sort(reverse=True)
[x for x in lst if condition]      # comprehension

# Tuples
t = (lat, lon)       # immutable
lat, lon = t          # unpacking

# Sets
s = set(raw_list)                  # dedupe
sorted(s)                           # dedupe + order
a | b   # union     a & b   # intersection     a - b   # difference

# Dicts
d.get(key, default)                 # safe access, never KeyError
d.get(key, 0) + amount               # accumulator pattern
for k, v in d.items():               # iterate pairs
    ...

# Deep copy for nested structures
import copy
deep = copy.deepcopy(original)

# Find max-by-field
top = items[0]
for item in items:
    if item["field"] > top["field"]:
        top = item
```

---

## Active Recall — Day 4

1. Why does `result = my_list.sort()` leave `result` as `None`?
2. When would you choose a tuple over a list, concretely?
3. Why is checking membership in a set faster than in a list?
4. What does `dict.get(key, default)` protect you from, compared to `dict[key]`?
5. Does `in` on a dictionary check keys, values, or both?
6. What's the difference between `.copy()` and `copy.deepcopy()`, and when does the difference actually matter?
7. Walk through the "find the customer with the most orders" pattern — why start with `customers[0]` instead of `0`?
8. Why can't a list be used as a dictionary key, but a tuple can?

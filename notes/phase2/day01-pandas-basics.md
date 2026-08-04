# Phase 2 — Day 1: Pandas Fundamentals

## Revision Notes

- Pandas = programmable spreadsheet engine. DataFrame ≈ worksheet, Series ≈ single column.
- Every DataFrame column is a Series under the hood.
- `pd.read_csv()` resolves relative paths against CWD, not script location — same class of bug as `open()` in Project 2.
- `.info()` + `.describe()` are the first two calls on any unfamiliar dataset — non-null counts catch missing data early, `.describe()` catches outliers/scale issues.
- Single bracket `df['col']` → Series (1D). Double bracket `df[['col']]` → DataFrame (2D, one column). This distinction matters because many pandas/sklearn methods expect 2D input even for a single column.
- Pandas 3.0 (Jan 2026) changed default string dtype from `object` → `str`. Version-dependent, not code-dependent — check `pd.__version__` before trusting dtype checks written elsewhere.

## Cheat Sheet

```python
import pandas as pd

# Load
df = pd.read_csv("path/to/file.csv")

# Explore
df.shape          # (rows, cols)
df.columns        # column names
df.dtypes         # type per column
df.head(n=5)      # first n rows
df.tail(n=5)      # last n rows
df.info()         # dtype + non-null + memory
df.describe()     # numeric summary stats

# Select
df['col']            # Series
df[['col']]           # DataFrame
df[['col1', 'col2']]  # DataFrame, multiple cols
```

## Active Recall

1. What's the fundamental building block a DataFrame is made of?
2. `df['amount']` vs `df[['amount']]` — what type does each return?
3. Name two things `.info()` shows that `.head()` doesn't.
4. Why can `read_csv()` silently succeed but return the wrong data?
5. What's the risk of checking `df['col'].dtype == 'object'` in pandas 3.0+?
6. When would you want a single column as a DataFrame instead of a Series?
7. What's the pandas equivalent of Excel's AutoFilter?


---

## Day 2: Filtering, Sorting, `.loc`/`.iloc`

### Revision Notes
- Boolean mask: `df['col'] > x` → Series of True/False. `df[mask]` → filtered rows.
- `&` / `|` required for combining conditions on Series, not `and`/`or` — each condition needs its own parentheses.
- `.sort_values('col', ascending=False)` for descending; pass a list for multi-column.
- `.loc` = label-based, `.iloc` = position-based. Identical on a fresh default index, diverge after filtering because filtered rows keep their *original* labels.
- `.iloc[n]` = single row at position n. `.iloc[a:b]` = slice, multiple rows. Don't confuse the two.

### Cheat Sheet
```python
df[df['col'] > x]                                  # filter
df[(df['a'] > x) & (df['b'] == y)]                  # AND
df[(df['a'] == x) | (df['a'] == y)]                 # OR
df.sort_values('col', ascending=False)              # sort desc
df.sort_values(['a', 'b'])                          # multi-col sort
df.loc[label, 'col']                                # by label
df.iloc[pos]                                        # by position, one row
df.iloc[start:end]                                  # by position, slice
```

### Active Recall
1. Why does `and`/`or` fail on Series conditions but `&`/`|` work?
2. What does `.iloc[2]` return that's different from `.iloc[2:3]`?
3. Give an example where `.loc[n]` and `.iloc[n]` return different rows.
4. What's the pandas equivalent of Excel's AutoFilter + multiple criteria?
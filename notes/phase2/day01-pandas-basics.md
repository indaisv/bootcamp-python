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
# Phase 2, Day 1: Pandas Fundamentals — Reading & Exploring Data

> **Learning Objectives:**
> 1. Understand why Pandas exists — the spreadsheet-engine mental model.
> 2. Master the Series vs. DataFrame distinction.
> 3. Read a CSV with `pd.read_csv()`.
> 4. Explore a DataFrame: `.shape`, `.columns`, `.dtypes`, `.head()`, `.tail()`, `.info()`, `.describe()`.
> 5. Select columns correctly — single bracket vs. double bracket.

---

## Business Motivation

Everything done by hand in Excel — open a file, eyeball columns, sum a range,
sanity-check for weird values — is what `pandas` automates.

| Excel / SQL | Pandas |
|---|---|
| A worksheet / a table | `DataFrame` |
| A single column | `Series` |
| Header row | `df.columns` |
| `=SUM()`, `=AVERAGE()` | `df['col'].sum()`, `.mean()` |
| Filter/AutoFilter | boolean indexing (Day 2) |
| Pivot table | `.groupby()` (later) |

Foundation for **Project 5: Automated Report Generator**.

---

## Lesson 1: Series vs. DataFrame

```python
import pandas as pd

amounts = pd.Series([500, 1200, 300, 4500])  # one labeled column

data = {
    "category": ["Food", "Travel", "Bills", "Rent"],
    "amount": [500, 1200, 300, 4500],
}
df = pd.DataFrame(data)  # dict of columns, like a table
```

Every column in a DataFrame **is** a Series.

## Lesson 2: Reading a File

```python
df = pd.read_csv("data/sample_sales.csv")
```

`*.csv` is git-ignored globally in this repo — intentional, sample data doesn't
get committed. Same relative-path gotcha as `open()` from Project 2: resolves
against the terminal's CWD, not the script's location.

## Lesson 3: Exploring

```python
df.shape        # (rows, columns)
df.columns      # column names
df.dtypes       # type per column
df.head()       # first 5 rows
df.tail(3)      # last 3
df.info()       # dtypes + non-null counts + memory
df.describe()   # summary stats, numeric columns only
```

`.info()` + `.describe()` = first move on any new dataset.

## Lesson 4: Column Selection

```python
df['amount']         # Series
df[['amount']]        # DataFrame, one column
df[['category', 'amount']]  # DataFrame, multiple columns
```

One bracket = values. Two brackets = table.

## Common Mistakes

| Mistake | Fix |
|---|---|
| `df.amount` breaks on spaced/colliding names | Always `df['amount']` |
| Assuming CSV row order | Check with `.head()` |
| `print(df)` on a huge file | Use `.head()`/`.tail()` |

## Real-World Finding (not a lesson, a discovery)

Ran on this machine's pandas version, `dtypes` showed `str` instead of the
`object` you'll see in every older tutorial. **Pandas 3.0 changed the
default string dtype from `object` to `str`** (PDEP-14, released Jan 2026).
Not a bug — just a version-drift trap. Any old code checking
`dtype == 'object'` to detect string columns will silently break on this
version. Verify with `python -c "import pandas as pd; print(pd.__version__)"`.

## Exercise: `src/phase2_day01_pandas_basics.py`

```python
def load_sales_data(filepath: str) -> pd.DataFrame: ...
def explore_data(df: pd.DataFrame) -> None: ...
def show_single_column(df: pd.DataFrame, column: str) -> None: ...
def show_multiple_columns(df: pd.DataFrame, columns: list) -> None: ...
```

## Interview Questions

1. Difference between a Series and a DataFrame?
2. Fastest way to get summary statistics for every numeric column?
3. Why prefer `df['col']` over `df.col`?
4. What does `.info()` tell you that `.head()` doesn't?
5. What happens if `read_csv` gets a bad path?

## Next: Day 2

Boolean indexing, `.sort_values()`, `.loc`/`.iloc`.

---

## ✅ Day 1 Checklist

- [x] `phase2_day01_pandas_basics.py` written, runs without errors
- [x] `load_sales_data`, `explore_data`, `show_single_column`, `show_multiple_columns` complete
- [x] Series vs. DataFrame distinguished correctly
- [ ] Q2 (when to prefer DataFrame-shaped single column) — in progress
- [ ] Committed to Git with descriptive message

**Say "Day 1 complete" once the checklist above is fully checked.**
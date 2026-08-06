# Phase 2, Day 3: GroupBy — Aggregating Data Like a Pivot Table

> **Learning Objectives:**
> 1. Understand split-apply-combine.
> 2. Aggregate with a single key and a single column.
> 3. Aggregate with multiple keys.
> 4. Run multiple aggregations at once with `.agg()`.
> 5. Know when and why `.reset_index()` is needed.

---

## Business Motivation

Every "total sales by region" or "average order value by rep" you've ever built in an Excel PivotTable is the same operation. The difference: a PivotTable needs a human to open the file and click. `.groupby()` runs the same logic inside a script, unattended — which is the entire premise of automation work. Project 5 (Automated Report Generator) is built directly on this.

---

## Lesson: Split → Apply → Combine

1. **Split** — pandas splits the DataFrame into groups based on a column's values (same as a PivotTable's row field).
2. **Apply** — a function runs on each group separately (`sum()`, `mean()`, `count()` — same as a PivotTable's "Values" field).
3. **Combine** — results come back as one summary.

```python
import pandas as pd

data = {
    "Region": ["North", "South", "North", "East"],
    "Amount": [45000, 800, 1500, 45000],
}
df = pd.DataFrame(data)

totals = df.groupby("Region")["Amount"].sum()
print(totals)
```

`df.groupby("Region")` alone returns a `GroupByObject`, not a table — it only becomes useful once you chain an aggregation onto it.

**Multiple keys** (like a PivotTable with two row fields):
```python
df.groupby(["Region", "Product"])["Amount"].sum()
```

**Multiple aggregations at once**, plus getting the group key back as a normal column:
```python
summary = df.groupby("Region")["Amount"].agg(["sum", "mean", "count"])
summary = summary.reset_index()   # Region: index -> column
```

---

## Exercise 3.1

```python
def total_by_region(df: pd.DataFrame) -> None:
    """Print total Amount per Region."""
    # TODO: group by "Region", select "Amount", sum it
    pass


def average_by_product(df: pd.DataFrame) -> None:
    """Print average Amount per Product."""
    # TODO
    pass


def multi_key_summary(df: pd.DataFrame) -> None:
    """Print total Amount grouped by BOTH Region and Product."""
    # TODO: groupby(["Region", "Product"])
    pass


def full_report(df: pd.DataFrame) -> None:
    """
    One summary DataFrame per Region: total, average, count.
    Hint: .agg(["sum", "mean", "count"]) then .reset_index()
    """
    # TODO
    pass
```

---

## Common Mistakes

| Mistake | Why it happens | Fix |
|---|---|---|
| `df.groupby("Region")` prints an object, not a table | Forgot to chain an aggregation | Always end with `.sum()`, `.mean()`, `.agg(...)` |
| `.mean()`/`.sum()` on the whole DataFrame errors or misbehaves | Text columns get swept in too | Select the numeric column first: `df.groupby("Region")["Amount"].sum()` |
| Group key "disappears," can't merge/export it | `groupby()` moves the key into the index | `.reset_index()` after aggregating |
| Confusing single vs double brackets after groupby | Same Series-vs-DataFrame rule as Day 1 column selection | Single brackets unless you deliberately want a DataFrame back |

---

## ✅ Day 3 Checklist

- [x] `phase2_day03_groupby.py` created and runs without errors.
- [x] `total_by_region()` completed and verified against raw data.
- [x] `average_by_product()` completed.
- [x] `multi_key_summary()` completed.
- [x] `full_report()` completed — this is the exact output shape Project 5 needs.
- [x] Code committed to Git.

**Day 3 complete.**
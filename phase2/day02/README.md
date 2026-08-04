# Phase 2, Day 2: Filtering, Sorting, and `.loc` / `.iloc`

> **Learning Objectives:**
> 1. Build boolean masks and filter rows with them.
> 2. Combine conditions correctly with `&` / `|` (not `and`/`or`).
> 3. Sort with `.sort_values()`, single and multi-column.
> 4. Distinguish `.loc` (label-based) from `.iloc` (position-based).
> 5. Understand why filtered DataFrames keep their original index labels.

---

## Business Motivation

Pandas equivalent of Excel's AutoFilter + `=SUMIF()`. "Show me Mumbai sales,"
"sort by amount descending," "get row 3 specifically" — every automated
report starts with filtering rows down to what matters.

---

## Lesson 1: Boolean Indexing

```python
df['amount'] > 500        # mask: True/False per row
df[df['amount'] > 500]    # actual filtered rows
```

Combine conditions with `&` (AND) / `|` (OR), each condition parenthesized:

```python
df[(df['amount'] > 500) & (df['region'] == 'Mumbai')]
df[(df['category'] == 'Food') | (df['category'] == 'Bills')]
```

`and`/`or` expect one True/False value; a Series holds many at once, so
Python can't collapse it — hence `&`/`|`, which operate element-by-element.

## Lesson 2: Sorting

```python
df.sort_values('amount')                    # ascending
df.sort_values('amount', ascending=False)   # descending
df.sort_values(['region', 'amount'])        # multi-column
```

## Lesson 3: `.loc` vs `.iloc`

```python
df.loc[0]               # row with INDEX LABEL 0
df.loc[0, 'amount']     # label-based, row + column
df.iloc[0]               # row at POSITION 0
df.iloc[0:3]              # first 3 rows by position (slice)
df.iloc[2]                # single row at position 2
```

`.loc` = by name/label. `.iloc` = by number/position. They agree on a fresh
DataFrame with the default 0,1,2... index — but **diverge after filtering**,
because a filtered DataFrame keeps its *original* row labels. Confirmed live
in this session's own output: `high_value_transactions()` returned rows
labeled `1, 3, 6` — not renumbered to `0, 1, 2` — even though those are
positions `0, 1, 2` in the filtered result.

## Exercise: `src/phase2_day02_filtering.py`

- `high_value_transactions(df, threshold)` — boolean filter, single condition
- `mumbai_food_orders(df)` — boolean filter, AND condition
- `top_5_by_amount(df)` — `.sort_values()` + `.head()`
- `get_third_row_category(df)` — `.iloc`, single position, not a slice

## Common Mistakes (from this session)

| Mistake | Fix |
|---|---|
| `df.iloc[0:3]` for "the 3rd row" | Slice ≠ single row. `.iloc[2]` for one row at position 2 (0-indexed: 1st=0, 2nd=1, 3rd=2) |
| `df[df['amount']>500 and df['region']=='Mumbai']` | Use `&`, wrap each condition in `()` |
| Assuming `.loc[n]` == `.iloc[n]` after filtering | Only true before any filtering/reordering |

## Interview Questions

1. Why does `df[cond1 and cond2]` raise an error instead of filtering?
2. What's the difference between `.iloc[0:3]` and `.iloc[2]`?
3. After filtering, why might `.loc[3]` and `.iloc[3]` return different rows?
4. How do you sort by two columns at once, one ascending and one descending? *(not covered yet — think about it)*

## Next: Day 3

`.groupby()` — the pandas equivalent of a pivot table. Ties directly into
Project 5 (per-category, per-region totals for the report generator).

---

## ✅ Day 2 Checklist

- [x] `phase2_day02_filtering.py` written, runs correctly
- [x] All 4 functions verified against expected output
- [x] `.loc` vs `.iloc` divergence observed in real output, not just theory
- [ ] Committed to Git

**Say "Day 2 complete" once committed.**
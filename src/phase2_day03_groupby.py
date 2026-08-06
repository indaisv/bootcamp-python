"""
day03_groupby.py
Phase 2, Day 3: GroupBy — aggregating data like a pivot table.
Author: Viraj
Date: 2026-08-06
"""

import pandas as pd


def build_sales_data() -> pd.DataFrame:
    """Sample sales data — stand-in for a real CSV in Project 5."""
    data = {
        "Region": ["North", "South", "North", "East", "South", "North", "East", "South"],
        "Product": ["Laptop", "Mouse", "Mouse", "Laptop", "Laptop", "Keyboard", "Mouse", "Keyboard"],
        "Amount": [45000, 800, 800, 45000, 45000, 1500, 800, 1500],
        "Units": [1, 1, 2, 1, 1, 1, 3, 2],
    }
    return pd.DataFrame(data)


def total_by_region(df: pd.DataFrame) -> None:
    """Print total Amount per Region."""
    # TODO: group by "Region", select "Amount", sum it
    grouped = df.groupby("Region")["Amount"].sum()
    print(grouped)

def average_by_product(df: pd.DataFrame) -> None:
    """Print average Amount per Product."""
    # TODO
    average = df.groupby("Product")["Amount"].mean()
    print(average)


def multi_key_summary(df: pd.DataFrame) -> None:
    """Print total Amount grouped by BOTH Region and Product."""
    # TODO: groupby(["Region", "Product"])
    multi_grouped = df.groupby(["Region", "Product"])["Amount"].sum()
    print(multi_grouped)


def full_report(df: pd.DataFrame) -> None:
    """
    Build one summary DataFrame, per Region, with:
      - total Amount
      - average Amount
      - count of transactions
    Hint: .agg(["sum", "mean", "count"]) on the Amount column,
    then .reset_index() so Region becomes a normal column again.
    """
    # TODO
    full_report_df = df.groupby("Region")["Amount"].agg(["sum", "mean", "count"]).reset_index()
    print(full_report_df)

def main():
    df = build_sales_data()
    print(df)
    print()
    total_by_region(df)
    print()
    average_by_product(df)
    print()
    multi_key_summary(df)
    print()
    full_report(df)


if __name__ == "__main__":
    main()
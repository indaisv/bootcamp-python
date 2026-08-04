"""
phase2_day02_filtering.py
Phase 2, Day 2: Boolean indexing, sorting, .loc/.iloc.
Author: Viraj
"""
import pandas as pd


def high_value_transactions(df: pd.DataFrame, threshold: int) -> pd.DataFrame:
    """Return only rows where amount > threshold."""
    # YOUR CODE
    return df[df["amount"]>threshold]


def mumbai_food_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows where region is Mumbai AND category is Food."""
    # YOUR CODE
    return df[(df["region"] == "Mumbai") & (df["category"] == "Food")]


def top_5_by_amount(df: pd.DataFrame) -> pd.DataFrame:
    """Return the 5 highest-amount rows, sorted descending."""
    # YOUR CODE
    return df.sort_values(by="amount", ascending=False).head(5)


def get_third_row_category(df: pd.DataFrame) -> str:
    """Return the category value from the 3rd row, by position."""
    # YOUR CODE: use .iloc
    return df.iloc[2]["category"]


def main():
    df = pd.read_csv("data/sample_sales.csv")

    print("High value (>800):")
    print(high_value_transactions(df, 800))

    print("\nMumbai Food orders:")
    print(mumbai_food_orders(df))

    print("\nTop 5 by amount:")
    print(top_5_by_amount(df))

    print("\n3rd row category:")
    print(get_third_row_category(df))


if __name__ == "__main__":
    main()
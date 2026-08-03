"""
phase2_day01_pandas_basics.py
Phase 2, Day 1: Pandas fundamentals.
Author: Viraj
"""
import pandas as pd


def load_sales_data(filepath: str) -> pd.DataFrame:
    """Load the sales CSV into a DataFrame."""
    # YOUR CODE: use pd.read_csv()
    df = pd.read_csv(filepath)
    return df


def explore_data(df: pd.DataFrame) -> None:
    """Print shape, columns, dtypes, head(), and describe()."""
    # YOUR CODE: print each of the five, one per line, with a label
    print("Shape:", df.shape)
    print("Columns:", df.columns)
    print("Dtypes:")
    print(df.dtypes)
    print("Head():")
    print(df.head())
    print("Describe():")
    print(df.describe())


def show_single_column(df: pd.DataFrame, column: str) -> None:
    """Print one column as a Series."""
    # YOUR CODE
    print(df[column])


def show_multiple_columns(df: pd.DataFrame, columns: list) -> None:
    """Print a subset of columns as a DataFrame."""
    # YOUR CODE
    print(df[columns])


def main():
    df = load_sales_data("data/sample_sales.csv")
    explore_data(df)
    show_single_column(df, "amount")
    show_multiple_columns(df, ["category", "amount"])


if __name__ == "__main__":
    main()
"""
day10_files.py
Practicing file I/O: plain text and CSV.
Author: Viraj
"""

import csv


def text_file_practice():
    """Write a few lines to a text file, then read them back."""
    lines = ["Line one", "Line two", "Line three"]

    # YOUR CODE: open "practice.txt" in write mode.
    with open ("practice.txt", "w") as f: 
    # Loop through `lines` and write each one, adding "\n" after it.
        for line in lines:
            f.write(line + "\n")
    # YOUR CODE: open "practice.txt" in read mode.
    with open ("practice.txt", "r") as f:
    # Read and print the whole contents.
        for line in f:
            print(line)
    


def csv_practice():
    """Write a small CSV of expenses, then read it back."""
    rows = [
        {"category": "Food", "amount": 500},
        {"category": "Travel", "amount": 1200},
    ]

    # YOUR CODE: open "practice.csv" in write mode (remember newline="").
    with open ("practice.csv", "w", newline= "") as f:
    # Use csv.DictWriter with fieldnames=["category", "amount"].
        writer = csv.DictWriter(f, fieldnames=["category", "amount"])
        writer.writeheader()
    # Call writeheader(), then write each row.
        for row in rows:
            writer.writerow(row)
    # YOUR CODE: open "practice.csv" in read mode (remember newline="").
    with open ("practice.csv", "r", newline= "") as f:
    # Use csv.DictReader, loop through it, and print each row.
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    text_file_practice()
    print()
    csv_practice()
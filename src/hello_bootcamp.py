"""
hello_bootcamp.py

My first professional Python program.
Author: Viraj
Date: 1-07-26
"""


def greet(name: str) -> str:
    """
    Return a professional greeting message.

    Args:
        name: The name of the person to greet.

    Returns:
        A formatted greeting string.
    """
    return f"Hello, {name}! Welcome to the bootcamp."


def main() -> None:
    """Main entry point of the program."""
    print("=" * 50)
    print("BOOTCAMP PYTHON — Day 1")
    print("=" * 50)

    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

    print("\nYour environment is ready. Let's build something amazing.")
    print("=" * 50)


# This ensures main() only runs when we execute this file directly.
# It does NOT run when this file is imported by another file.
if __name__ == "__main__":
    main()
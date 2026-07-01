"""
hello_bootcamp.py

My first professional Python program.
Author: Viraj
Date: 2026-07-01
"""


def greet(name: str, city: str) -> str:
    """
    Return a professional greeting message.

    Args:
        name: The name of the person to greet.
        city: the city of the person.
    Returns:
        A formatted greeting string.
    """
    return f"Hello, {name} from {city}! Welcome to the bootcamp."

def calculated_age(birth_year: int) -> int:
    """
    Calculate approximate age based on birth year.

    Args:
        birth_year: The year the person was born.

    Returns:
        The approximate age as an integer.
    """
    current_year = 2026
    return current_year - birth_year


def main() -> None:
    """Main entry point of the program."""
    print("=" * 50)
    print("BOOTCAMP PYTHON — Day 1")
    print("=" * 50)

    user_name = input("Enter your name: ")
    user_city = input("Enter your city: ")
    message = greet(user_name, user_city)
    print(message)
    
    birth_year_input = input("Enter birth year: ")
    birth_year = int(birth_year_input)
    age = calculated_age(birth_year)
    print(f"You are approximately {age} years old.")
    

    print("\nYour environment is ready. Let's build something amazing.")
    print("=" * 50)


# This ensures main() only runs when we execute this file directly.
# It does NOT run when this file is imported by another file.
if __name__ == "__main__":
    main()
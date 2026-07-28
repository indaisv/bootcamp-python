"""
password_manager.py
Project 2: Password Manager (CLI)
Author: Viraj
"""

import getpass
import json
import logging
import re
from pathlib import Path

from cryptography.fernet import Fernet

BASE_DIR = Path(__file__).resolve().parent
KEY_FILE = BASE_DIR / ".." / "data" / "secret.key"
VAULT_FILE = BASE_DIR / ".." / "data" / "vault.json"
LOG_FILE = BASE_DIR / ".." / "password_manager.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_call(func):
    """Log that a function was called — name only, never its arguments
    (arguments may contain a plaintext password)."""

    def wrapper(*args, **kwargs):
        logging.info(f"{func.__name__} called")
        return func(*args, **kwargs)

    return wrapper


def generate_or_load_key() -> bytes:
    """
    Return the encryption key, loading it from KEY_FILE if it already
    exists, or generating and saving a new one if it doesn't.
    """
    try:
        with open(KEY_FILE, "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        new_key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(new_key)
        return new_key


def encrypt_password(plain_password: str, key: bytes) -> bytes:
    """
    Encrypt a plaintext password using the given Fernet key.
    Returns the encrypted token as bytes.
    """
    fernet = Fernet(key)
    return fernet.encrypt(plain_password.encode())


def decrypt_password(token: bytes, key: bytes) -> str:
    """
    Decrypt a Fernet token back into the original plaintext password.
    """
    fernet = Fernet(key)
    return fernet.decrypt(token).decode()


def load_vault() -> list:
    """
    Load all password entries from VAULT_FILE.
    Returns an empty list if the vault doesn't exist yet or is corrupted.
    """
    try:
        with open(VAULT_FILE, "r") as vault_file:
            return json.load(vault_file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: Vault file is corrupted. Returning empty vault.")
        return []


def save_vault(entries: list) -> None:
    """Write all password entries back to VAULT_FILE."""
    with open(VAULT_FILE, "w") as vault_file:
        json.dump(entries, vault_file, indent=2)


def print_menu():
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("PASSWORD MANAGER")
    print("=" * 40)
    print("1. Add new entry")
    print("2. View all entries (passwords hidden)")
    print("3. Retrieve a password")
    print("4. Delete an entry")
    print("5. Exit")


def is_strong_password(password: str) -> bool:
    """
    Check password strength: at least 8 characters, with at least
    one uppercase, one lowercase, one digit, and one special character.
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


@log_call
def add_entry(entries: list, key: bytes) -> None:
    """
    Prompt for a service, username, and password, encrypt the password,
    and append the new entry to entries.

    Note: this does NOT call save_vault() itself — the menu loop handles
    saving after every action, in one place.
    """
    service = input("Service: ").strip()
    username = input("Username: ").strip()
    password = getpass.getpass("Password (hidden): ")
    if not is_strong_password(password):
        print("Warning: The password does not meet the strength requirements.")
    encrypted = encrypt_password(password, key)
    entry = {"service": service, "username": username, "password": encrypted.decode()}
    entries.append(entry)
    logging.info(f"Added entry for service={service}")
    print(f"Added entry for {service}.")


def view_entries(entries: list) -> None:
    """Print every entry with a running number; passwords stay hidden."""
    if not entries:
        print("No entries in vault yet.")
        return
    for i, entry in enumerate(entries, start=1):
        print(f"{i}. {entry['service']} — {entry['username']}")


@log_call
def retrieve_entry(entries: list, key: bytes) -> None:
    """Let the user pick an entry by number and see its decrypted password."""
    if not entries:
        print("No entries in vault yet.")
        return
    view_entries(entries)
    choice = input("Enter entry number to retrieve: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(entries)):
        print("Invalid choice. Please enter a valid entry number.")
        return
    selected = entries[int(choice) - 1]
    decrypted_password = decrypt_password(selected["password"].encode(), key)
    logging.info(f"Retrieved password for service={selected['service']}")
    print(f"Service: {selected['service']}")
    print(f"Username: {selected['username']}")
    print(f"Password: {decrypted_password}")


@log_call
def delete_entry(entries: list) -> None:
    """Let the user pick an entry by number and remove it from entries."""
    if not entries:
        print("No entries in vault yet.")
        return
    view_entries(entries)
    choice = input("Enter entry number to delete: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(entries)):
        print("Invalid choice. Please enter a valid entry number.")
        return
    removed = entries.pop(int(choice) - 1)
    logging.info(f"Deleted entry for service={removed['service']}")
    print(f"Deleted entry for {removed['service']}.")


def main():
    """The menu loop."""
    key = generate_or_load_key()
    entries = load_vault()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_entry(entries, key)
            save_vault(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            retrieve_entry(entries, key)
        elif choice == "4":
            delete_entry(entries)
            save_vault(entries)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
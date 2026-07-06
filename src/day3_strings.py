"""
day3_strings.py
Mastering string slicing and methods.
Author: Viraj
Date: 2026-07-01
"""

'''
def slicing_practice():
    """Practice string slicing with real data."""
    # Extract year, month, day from this date string
    date_str = "2026-07-15"
    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:]
    

    # Extract the phone number without country code
    phone = "+91-98765-43210"
    phone_without_code = phone[4:]

    # Extract first name from "Viraj_Indais_123"
    username = "Viraj_Indais_123"
    first_name = username[0:5]

    # Reverse this transaction ID
    txn_id = "TXN-2026-78432"
    reversed_txn = txn_id[::-1]

    # Print all results
    print(f"Year: {year}")
    print(f"Month: {month}")
    print(f"Day: {day}")
    print(f"Phone without code: {phone_without_code}")
    print(f"First name: {first_name}")
    print(f"Reversed TXN: {reversed_txn}")


if __name__ == "__main__":
    slicing_practice()
    
'''
#3.2

def clean_customer_data(raw_name: str, raw_email: str, raw_phone: str) -> dict:
    """
    Clean messy customer data.

    Args:
        raw_name: Name with extra spaces and wrong case.
        raw_email: Email with possible uppercase and spaces.
        raw_phone: Phone with country code and dashes.

    Returns:
        Dictionary with cleaned name, email, phone.
    """
    # Clean name: strip spaces, title case
    # Example: "  viraj  INDais  " -> "Viraj Indais"
    cleaned_name = raw_name.strip().title()

    # Clean email: strip spaces, lowercase
    cleaned_email = raw_email.strip().lower()

    # Clean phone: remove country code and dashes
    # Example: "+91-98765-43210" -> "9876543210"
    # Hint: use .replace() twice or .split("-")
    cleaned_phone = raw_phone.replace("+91-", "").replace("-", "")

    return {
        "name": cleaned_name,
        "email": cleaned_email,
        "phone": cleaned_phone,
    }


def test_data_cleaning():
    """Test the data cleaning utility."""
    raw_data = [
        ("  viraj  INDais  ", "Viraj.Indais@GMAIL.COM", "+91-98765-43210"),
        ("ALICE  smith", " alice@Yahoo.com ", "+91-87654-32109"),
        ("  BOB JONES  ", "BOB@EXAMPLE.COM", "+91-76543-21098"),
    ]

    for raw_name, raw_email, raw_phone in raw_data:
        cleaned = clean_customer_data(raw_name, raw_email, raw_phone)
        print(f"Raw:    {raw_name!r} | {raw_email!r} | {raw_phone!r}")
        print(f"Clean:  {cleaned['name']!r} | {cleaned['email']!r} | {cleaned['phone']!r}")
        print()
        
if __name__ == "__main__":
    test_data_cleaning()
    

text = "abcdef"
print(text[::2])      # ?
print(text[1::2])     # ?
print(text[::-1])     # ?
print(text[::-2])     # ?
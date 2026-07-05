"""
test_fstring.py
Understanding f-strings and !r.
"""

name = "Viraj"
age = 23
salary = 50000.50
is_active = True

# Normal f-string
print(f"My name is {name} and I am {age} years old.")
print(f"My salary is ₹{salary}.")

# With !r
print(f"\n--- With !r (debug mode) ---")
print(f"Name: {name!r}")
print(f"Age: {age!r}")
print(f"Salary: {salary!r}")
print(f"Is Active: {is_active!r}")

# The confusion
data = ""
print(f"\nEmpty string without !r: '{data}'")   # Hard to see
print(f"Empty string with !r: {data!r}")         # Clearly shows ''
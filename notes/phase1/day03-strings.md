# Day 3 — Strings, The Professional Way

## Revision Notes

**Why this day matters:** data analysts spend a large chunk of their time cleaning messy text — names with weird casing, emails with stray spaces, phone numbers with country codes baked in. `clean_customer_data()` (built this day) is the template for that entire category of work.

**Slicing — `[start:end:step]`**
- `start` is included, `end` is excluded. This trips everyone up at least once.
- `text[:4]` = "from the beginning up to (not including) index 4."
- `text[::-1]` reverses a string — used for the reversed transaction ID exercise.
- Slicing works identically on lists (confirmed in Day 4).

**Core string methods**
- Cleaning: `.strip()`, `.lstrip()`, `.rstrip()` — removes whitespace from ends.
- Case: `.upper()`, `.lower()`, `.title()`, `.capitalize()`.
- Search: `.find()` returns index or `-1` if not found — always check for `-1` before trusting the result.
- Split/join: `.split(",")` breaks a string into a list (how you'd parse a CSV line); `" ".join(list)` does the reverse.
- Checks: `.startswith()`, `.endswith()`, `.isdigit()`.

**Strings are immutable — same rule as Day 2, applied here specifically.** `raw_name.strip().title()` works because each method call returns a *new* string that the next method chains onto — the original `raw_name` is never touched. This is why `clean_customer_data()` reassigns into new variables (`cleaned_name`, etc.) rather than trying to mutate the inputs.

**Business data cleaning pattern** (from `clean_customer_data` in `day3_strings.py`):
```python
cleaned_name = raw_name.strip().title()
cleaned_email = raw_email.strip().lower()
cleaned_phone = raw_phone.replace("+91-", "").replace("-", "")
```
Note: names get `.title()` (professional casing), emails get `.lower()` (so comparisons work — `Gmail.com` and `gmail.com` must match), phone numbers get literal characters stripped out via `.replace()`.

---

## Cheat Sheet

```python
# Slicing
s = "abcdef"
s[0:3]      # "abc" — start included, end excluded
s[:3]       # same as above
s[2:]       # "cdef" — to the end
s[-3:]      # "def" — last 3 chars
s[::2]      # "ace" — every 2nd char
s[::-1]     # "fedcba" — reversed

# Cleaning
s.strip()              # trim whitespace both ends
s.upper() / s.lower() / s.title()

# Searching
idx = s.find("x")      # -1 if not found — ALWAYS check
"x" in s                # True/False membership check

# Split / join
"a,b,c".split(",")             # ['a', 'b', 'c']
" ".join(["a", "b", "c"])      # "a b c"

# Checks
s.startswith("abc")
s.endswith(".com")
s.isdigit()

# Data cleaning pattern
def clean_customer_data(raw_name, raw_email, raw_phone):
    return {
        "name": raw_name.strip().title(),
        "email": raw_email.strip().lower(),
        "phone": raw_phone.replace("+91-", "").replace("-", ""),
    }
```

---

## Active Recall — Day 3

1. In slicing, is the `end` index included or excluded? Give an example that would break if you got this backwards.
2. Why does `.find()` return `-1` instead of raising an error, and what does that mean for how you use it?
3. What does `.split(",")` return, and how does `.join()` reverse that operation?
4. Why does `clean_customer_data()` reassign into new variables instead of modifying `raw_name` directly?
5. Why `.title()` for names but `.lower()` for emails — what's the business reason for the difference?
6. What does `text[::-1]` do, mechanically?
7. If `raw_phone.replace("+91-", "")` is called on a number *without* a country code, what happens? Is that a bug?

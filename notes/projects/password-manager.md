# Project 2: Password Manager (CLI) — Notes

## Concepts
- Encryption vs hashing: encryption is reversible (needed here — you must get
  the original password back); hashing is one-way (used for login/auth
  verification only, never for storage you need to retrieve).
- Fernet (cryptography library): symmetric encryption — one key encrypts and
  decrypts. Never roll your own crypto.
- Key management: generate once with Fernet.generate_key(), persist to disk,
  always load the existing key rather than regenerating — regenerating
  permanently invalidates every password encrypted with the old key.
- bytes vs str: Fernet works on bytes. Typed passwords are str -> .encode()
  before encrypting. JSON only stores text -> .decode() the encrypted token
  before saving, .encode() it back before decrypting.
- File path resolution: open() resolves relative paths against the
  terminal's cwd, not the script's location. Path(__file__).resolve().parent
  anchors paths to where the script actually lives, regardless of cwd.
- getpass.getpass(): like input(), but doesn't echo typed characters — used
  for password entry so it's not visible on screen or in shell history.
- Regex reused for password strength checks — same skill as Project 1's
  category/amount validation, new use case.
- Logging discipline: log that an action happened and which service it
  touched — never the password, plaintext or encrypted. Secrets leaking into
  log files is a real, common vulnerability class.
- Numbered-selection pattern for retrieve/delete: service names aren't
  unique (two "gmail" entries can coexist), so act on list position.

## Cheat sheet
\`\`\`python
from cryptography.fernet import Fernet

key = Fernet.generate_key()              # bytes — generate ONCE, persist it
f = Fernet(key)
token = f.encrypt(b"plaintext")          # str -> bytes -> encrypted bytes
plaintext = f.decrypt(token).decode()    # encrypted bytes -> bytes -> str

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent   # anchored to script, not cwd

import getpass
password = getpass.getpass("Password: ")     # hidden input

entry["password"] = token.decode()                  # bytes -> str, for JSON
decrypt_password(entry["password"].encode(), key)   # str -> bytes, to decrypt
\`\`\`

## Active recall
1. Why can't a password manager use hashing the way a login system does?
2. What happens if you generate a new Fernet key instead of loading the existing one?
3. Why does open("../data/secret.key") behave differently depending on which folder you run the script from?
4. What does Path(__file__).resolve().parent give you, and why does it fix that?
5. Why does encrypt() need .encode() on the input, and why does the result need .decode() before saving to JSON?
6. Why getpass.getpass() instead of input() for passwords?
7. Why do retrieve/delete work off a numbered list instead of matching on service name?
8. What's the rule for what a logging call is allowed to include?
9. How does this project's "key file on disk" security model differ from a "real" password manager with a master password?
10. Why does save_vault() only get called after add/delete, not after view/retrieve?
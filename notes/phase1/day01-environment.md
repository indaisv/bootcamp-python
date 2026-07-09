# Day 1 — Professional Dev Environment

## Revision Notes

**Tooling, and why each piece exists**
- **VS Code** — editor with built-in debugger, terminal, Git integration, and extensions. Industry-standard, not a personal preference.
- **Python 3.11+** — interpreted language, huge ecosystem (pandas, requests, etc.), no fixed integer size limit.
- **Git** — version control. Tracks every change, enables collaboration without overwriting others' work, lets you undo mistakes. Non-negotiable for employability.
- **Windows Terminal** — modern shell wrapper; optional but standard in professional setups.

**Project structure is a signal, not decoration**
```
bootcamp-python/
├── src/            ← source code
├── tests/          ← tests (Pytest, later)
├── data/            ← sample data files
├── .gitignore
├── README.md
└── requirements.txt
```
A new engineer should understand the codebase layout in ~10 minutes. That's the actual bar.

**`.gitignore`** — tells Git what *not* to track: `__pycache__/`, `venv/`, `.csv`/`.xlsx` (large data), IDE clutter. Without it, the repo balloons with junk that shouldn't be version-controlled.

**`if __name__ == "__main__":`** — separates "code that runs when this file is executed directly" from "code that runs when this file is *imported* by another file." Without this guard, importing a module would trigger its side effects (like `input()` prompts) unintentionally.

**Type hints** (`name: str`, `-> str`) — document expected types for other engineers (and future-you). Not enforced at runtime, but critical for readability and tooling (autocomplete, linters).

---

## Cheat Sheet

```bash
# Verify installs
python --version
git --version
pip --version

# Git identity (once per machine)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# First-time repo setup
git init
git add .
git commit -m "Initial commit: Project structure and first Python program"
git log
```

```python
"""
module_name.py
One-line description.
Author: Viraj
Date: YYYY-MM-DD
"""

def greet(name: str, city: str) -> str:
    """Docstring: what it does, args, returns."""
    return f"Hello, {name} from {city}!"

def main() -> None:
    user_name = input("Enter your name: ")
    print(greet(user_name, "Mumbai"))

if __name__ == "__main__":
    main()
```

---

## Active Recall — Day 1

1. What's the difference between an IDE and a plain text editor?
2. Why is Git non-negotiable in professional development, even solo?
3. What does `.gitignore` actually do, mechanically?
4. What does `if __name__ == "__main__":` prevent from happening?
5. Why use type hints if Python doesn't enforce them at runtime?
6. What's the purpose of a docstring, beyond "documentation"?
7. Why do `src/` and `tests/` live in separate folders instead of one flat folder?

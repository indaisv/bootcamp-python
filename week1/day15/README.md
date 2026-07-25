# Week 1, Day 15: Virtual Environments & pip

> **Learning Objectives:**
> 1. Understand why isolating project dependencies matters, instead of installing everything globally.
> 2. Create and activate a `venv` for this project, from scratch.
> 3. Understand the difference between global and venv-scoped package installs.
> 4. Install project dependencies from `requirements.txt` inside an active venv.
> 5. Configure VS Code to actually use the venv's Python interpreter.
> 6. Know the common gotchas: PowerShell execution policy, per-terminal activation, never committing `venv/`.

---

## Business Motivation

Every package used so far (`pytest`, and now `pandas`, `requests`, etc.) had been installed **globally**, shared across every Python project on the machine. That breaks down the moment two projects need different, incompatible versions of the same package. A virtual environment isolates a project's dependencies completely — installs inside it never touch the global Python or any other project.

Worth noting: this project's own `README.md` and Day 1 setup instructions already assumed a venv would be used from the start — but no terminal output across Days 1–14 ever showed a `(venv)` prefix. Every day so far actually ran against the global Python install. Today closed that gap.

---

## What It Is

`venv` is built into Python 3.3+ — no separate install needed. Creating one makes a `venv/` folder containing its own `python.exe`, `pip.exe`, and a private `site-packages` directory, fully separate from the system-wide Python installation.

---

## Step-by-Step Setup (Completed Today)

```bash
cd C:\Users\Viraj\Documents\bootcamp-python
python -m venv venv
venv\Scripts\activate          # prompt shows (venv) prefix on success
pip list                       # confirms isolation — near-empty on a fresh venv
pip install -r requirements.txt
pytest -v                      # confirms it's running via venv's own python.exe
deactivate
```

**Common PowerShell blocker (not hit this time, but good to know):** `cannot be loaded because running scripts is disabled on this system`. Fix:
```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Result:** all packages from `requirements.txt` installed cleanly into the isolated venv, and the full 10-test pytest suite passed, confirmed running against `venv\Scripts\python.exe` rather than the global interpreter.

---

## VS Code Interpreter Selection

`Ctrl + Shift + P` → **"Python: Select Interpreter"** → choose `.\venv\Scripts\python.exe`.

Callback to Day 1: the checklist already had **"Python > Terminal: Activate Environment On Terminal Creation"** checked in VS Code settings — with no venv to activate at the time, it did nothing. Now that a real venv exists, correctly selecting the interpreter makes that setting auto-activate the venv in every new terminal opened inside this project.

---

## Common Mistakes (Day 15)

| Mistake | Fix |
|---------|-----|
| `pip install` before activating | Installs globally again — always confirm `(venv)` is showing first |
| Forgetting to reactivate in a new terminal | Activation is per-terminal session; reactivate each time, or rely on VS Code auto-activate |
| Committing `venv/` to Git | Never needed in version control — already excluded via existing `.gitignore` |
| VS Code interpreter still pointed at global Python | Code runs, but silently uses the wrong environment — verify via "Python: Select Interpreter" |
| Assuming `requirements.txt` alone isolates anything | It's just a list — isolation only happens with an *activated* venv |
| `>=` minimums silently pulling in a much newer major version | Happened today — `pandas>=2.0.0` installed `pandas 3.0.5`. Worth remembering if Phase 2 pandas code behaves unexpectedly vs. older tutorials |

## Best Practices

1. One venv per project — this whole repo, one venv at the root.
2. Check for `(venv)` in the prompt before any `pip install` or `python` command.
3. Never commit `venv/` — already handled.
4. Keep `requirements.txt` current — `pip freeze > requirements.txt` captures exact installed versions (a different style from the current hand-written `>=` minimums; either is valid, just stay consistent).

---

## Interview Questions (Day 15 Level)

1. Why use a virtual environment instead of installing packages globally?
2. What's actually inside a `venv/` folder?
3. Why should `venv/` never be committed to Git?
4. What does `requirements.txt` do, and how is it different from having an activated venv?
5. What's the practical difference between `pip freeze > requirements.txt` and manually maintaining version minimums with `>=`?

---

## Resume Relevance

> "Set up isolated Python virtual environments and dependency management via pip and requirements.txt, following professional project setup standards."

---

## Next Lesson Preview (Day 16)

**Topic:** Git Branches & Pull Requests — moving beyond basic `add`/`commit`/`push` into real collaborative Git workflow, per the roadmap's Phase 1 skill order.

---

## ✅ Day 15 Checklist

- [x] `venv/` created at the project root.
- [x] Activated successfully.
- [x] `requirements.txt` installed inside the venv.
- [x] `pytest -v` confirmed working inside the venv (10/10 passed, correct interpreter path).
- [ ] VS Code interpreter pointed at `.\venv\Scripts\python.exe` (confirm).
- [x] `.gitignore` already excludes `venv/`.
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 15 complete."**

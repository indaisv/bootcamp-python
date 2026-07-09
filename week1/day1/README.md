# Week 1, Day 1: Your Professional Development Environment

> **Learning Objectives:**
> 1. Understand WHY we use specific tools in professional development.
> 2. Install and configure VS Code, Python, Git, and Windows Terminal on Windows 11.
> 3. Create your first professional project folder with proper structure.
> 4. Write, run, and debug your first Python program.
> 5. Make your first Git commit.
> 6. Understand the difference between a student workflow and a professional workflow.

---

## Business Motivation

Companies do NOT hire people who write Python in online editors or Notepad. They hire engineers who:
- Use professional IDEs with debugging, linting, and version control built-in.
- Write code that other engineers can read, test, and deploy.
- Use Git to track every change and collaborate without breaking things.
- Organize projects so a new teammate can understand the codebase in 10 minutes.

Today you stop being a student and start becoming a professional engineer. The tools you install today are the exact same tools used at TCS, Infosys, Wipro, Accenture, Deloitte, and every startup in Bangalore and Hyderabad.

---

## Phase 1: The Big Picture (Week 1–10)

Over the next 10 weeks, you will master Python as a professional software engineer—not as a hobbyist. By the end of Phase 1, you will have:
- Written 4 complete Python projects with professional structure.
- Used Git for every single line of code you write.
- Written unit tests for your functions.
- Handled errors like a senior engineer (no more `print` debugging).
- Built code that you can proudly put on your resume and GitHub.

---

## Today's Tools: What, Why, and Where to Download

### 1. VS Code (Visual Studio Code)

**What is it?**  
VS Code is a free, open-source code editor built by Microsoft. It is the #1 most popular code editor in the world.

**Why do companies use it?**  
- It's free, fast, and infinitely customizable.
- It has extensions for Python, Git, Docker, SQL, and every language you will ever use.
- It has a built-in debugger, terminal, and Git integration.
- It's used by 70%+ of professional developers worldwide.

**Which companies use it?**  
Microsoft, Google, Facebook, Amazon, Netflix, and virtually every company you will apply to.

**Official download:**  
https://code.visualstudio.com/download

**System requirements:**
- Windows 11 (64-bit)
- 1 GB RAM minimum (4 GB recommended)
- 500 MB disk space

---

### 2. Python 3.11+

**What is it?**  
Python is a high-level, interpreted programming language. Version 3.11 is the current stable version with significant performance improvements.

**Why do companies use it?**  
- Python is the #1 language for data science, automation, and AI.
- It is the standard language for data analytics, machine learning, and scripting.
- It has the largest ecosystem of libraries (pandas, numpy, requests, openai, etc.).

**Which companies use it?**  
Google, Netflix, Spotify, Instagram, Uber, Dropbox, and every data team in the Fortune 500.

**Official download:**  
https://www.python.org/downloads/

**System requirements:**
- Windows 11 (64-bit)
- 2 GB RAM minimum
- 100 MB disk space (base install)

---

### 3. Git

**What is it?**  
Git is a version control system. It tracks every change you make to your code. It allows you to collaborate with other developers without overwriting each other's work.

**Why do companies use it?**  
- Without Git, teams cannot work on the same codebase simultaneously.
- It allows you to undo mistakes instantly.
- It is the industry standard. If you don't know Git, you are not hireable as a software engineer.

**Which companies use it?**  
Every single software company on Earth. Period.

**Official download:**  
https://git-scm.com/download/win

**System requirements:**
- Windows 11 (64-bit)
- Minimal resources (~50 MB)

---

### 4. Windows Terminal (Optional but Recommended)

**What is it?**  
Windows Terminal is a modern, fast terminal application from Microsoft. It replaces the old Command Prompt with tabs, themes, and better font support.

**Why do we use it?**  
- Professional developers live in the terminal.
- You will run Python, Git, pip, and Docker commands here.
- It looks professional and is faster than the old Command Prompt.

**Download:**  
https://apps.microsoft.com/detail/9n0dx20hk701 (Microsoft Store)

---

## Step-by-Step Installation Guide

### ⚠️ CRITICAL: Before You Start

1. Close all other applications.
2. Ensure you have at least 2 GB of free disk space.
3. You need administrator rights on your Windows 11 machine.
4. Read EVERY step. Do not skip. Do not assume.

---

### Step 1: Install Python 3.11

1. Open your browser and go to: **https://www.python.org/downloads/**
2. Click the big yellow button: **"Download Python 3.11.x"**
3. Run the downloaded `.exe` file.
4. **⚠️ EXTREMELY IMPORTANT:** On the first screen of the installer, check the box that says:  
   **"Add python.exe to PATH"**  
   (This is at the bottom of the window. If you skip this, Python will NOT work from the terminal.)
5. Click **"Customize installation"** (NOT "Install Now").
6. On the "Optional Features" screen, ensure ALL checkboxes are checked:
   - ☑ Documentation
   - ☑ pip
   - ☑ tcl/tk and IDLE
   - ☑ Python test suite
   - ☑ py launcher
   - ☑ for all users (if available)
7. Click **Next**.
8. On the "Advanced Options" screen, check:
   - ☑ Install for all users
   - ☑ Associate files with Python
   - ☑ Create shortcuts for installed applications
   - ☑ Add Python to environment variables
   - ☑ Precompile standard library (optional, makes Python faster)
9. The install path should show something like: `C:\Program Files\Python311\`
10. Click **Install**.
11. Wait for the installation to complete. Click **Close**.

**Verify Python Installation:**
1. Press `Win + R`, type `cmd`, press Enter.
2. In the black window, type: `python --version`
3. You should see: `Python 3.11.x` (or similar)
4. If you see an error like "python is not recognized," you did NOT check "Add to PATH." Uninstall and reinstall.

**Verify pip Installation:**
1. In the same window, type: `pip --version`
2. You should see a version number. If not, Python was not installed correctly.

---

### Step 2: Install Git

1. Go to: **https://git-scm.com/download/win**
2. The download should start automatically. If not, click **"Click here to download manually."**
3. Run the downloaded `.exe` file.
4. Click **Next** through the license.
5. **Select Destination Location:** Keep the default (`C:\Program Files\Git`). Click **Next**.
6. **Select Components:** Keep the defaults checked. Click **Next**.
7. **Select Start Menu Folder:** Keep default. Click **Next**.
8. **Choose the default editor used by Git:** Select **"Use Visual Studio Code as Git's default editor"** from the dropdown. Click **Next**.
9. **Adjusting the name of the initial branch:** Select **"Override the default branch name for new repositories"** and type: `main`. Click **Next**.
10. **Adjusting your PATH environment:** Select **"Git from the command line and also from 3rd-party software"**. Click **Next**.
11. **Choosing the SSH executable:** Select **"Use bundled OpenSSH"**. Click **Next**.
12. **Choosing HTTPS transport backend:** Select **"Use the OpenSSL library"**. Click **Next**.
13. **Configuring the line ending conversions:** Select **"Checkout Windows-style, commit Unix-style line endings"**. Click **Next**.
14. **Configuring the terminal emulator:** Select **"Use MinTTY (the default terminal of MSYS2)"**. Click **Next**.
15. **Choose the default behavior of `git pull`:** Select **"Fast-forward or merge"**. Click **Next**.
16. **Choose a credential helper:** Select **"Git Credential Manager"**. Click **Next**.
17. **Enable file system caching:** Keep default checked. Click **Next**.
18. **Configuring experimental options:** Do NOT check any experimental options. Click **Next**.
19. Click **Install**.
20. Wait for installation. Click **Finish**.

**Verify Git Installation:**
1. Open Command Prompt (or Windows Terminal).
2. Type: `git --version`
3. You should see: `git version 2.x.x`

---

### Step 3: Configure Git (Your Identity)

Git needs to know who you are. Every commit you make will be tagged with your name and email.

1. Open Command Prompt.
2. Type these commands exactly (replace with your actual name and email):

```cmd
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

3. Verify with:
```cmd
git config --global user.name
git config --global user.email
```

---

### Step 4: Install VS Code

1. Go to: **https://code.visualstudio.com/download**
2. Click **"Windows"** (the blue button).
3. Run the downloaded `.exe` file.
4. Accept the license agreement. Click **Next**.
5. **Select Destination Location:** Keep default (`C:\Users\<YourName>\AppData\Local\Programs\Microsoft VS Code`). Click **Next**.
6. **Select Start Menu Folder:** Keep default. Click **Next**.
7. **Select Additional Tasks:** CHECK these boxes:
   - ☑ Add "Open with Code" action to Windows Explorer file context menu
   - ☑ Add "Open with Code" action to Windows Explorer directory context menu
   - ☑ Register Code as an editor for supported file types
   - ☑ Add to PATH (requires shell restart)
   - ☑ **Create a desktop icon** (optional, your choice)
8. Click **Next**, then **Install**.
9. Wait for installation. Click **Finish**.

**Verify VS Code:**
1. Press `Win + S`, type `Visual Studio Code`, and open it.
2. It should open without errors.

---

### Step 5: Install VS Code Extensions (Critical for Python Development)

Extensions are what make VS Code powerful. You MUST install these.

1. Open VS Code.
2. Click the **Extensions** icon on the left sidebar (it looks like four squares with one separated).
3. In the search bar, type and install EACH of these:

| Extension | Publisher | Why You Need It |
|-----------|-----------|-----------------|
| **Python** | Microsoft | Official Python support: IntelliSense, debugging, linting, Jupyter |
| **Pylance** | Microsoft | Advanced Python language server (auto-completes your code) |
| **Python Indent** | Kevin Rose | Auto-fixes Python indentation |
| **GitLens** | GitKraken | See who changed what and when directly in your code |
| **Error Lens** | Alexander | Shows errors inline (red underline) without hovering |
| **Python Docstring Generator** | Nils Werner | Auto-generates professional docstrings |
| **Code Runner** | Jun Han | Run Python code with one button (Ctrl+Alt+N) |
| **Better Comments** | Aaron Bond | Highlights TODO, FIXME, and important comments |
| **Material Icon Theme** | Philipp Kief | Makes your file icons look professional |
| **One Dark Pro** | BinaryFy | A clean, professional color theme (optional but recommended) |

**To install each:**
1. Type the extension name in the search bar.
2. Click the extension.
3. Click **"Install"**.
4. Wait for it to finish.

---

### Step 6: Configure VS Code for Python (One-Time Setup)

1. In VS Code, press `Ctrl + ,` (comma) to open Settings.
2. In the search bar at the top, type each setting and set the value:

| Setting | Value | Why |
|---------|-------|-----|
| `Editor: Tab Size` | `4` | Python standard is 4 spaces |
| `Editor: Insert Spaces` | ☑ Checked | Python uses spaces, not tabs |
| `Editor: Word Wrap` | `on` | Lines wrap so you don't scroll horizontally |
| `Python > Terminal: Activate Environment On Terminal Creation` | ☑ Checked | Auto-activates virtual environments |
| `Files: Auto Save` | `afterDelay` | Saves your file automatically |

3. Close the Settings tab.

---

### Step 7: Install Windows Terminal (Optional but Recommended)

1. Open Microsoft Store (search "Microsoft Store" in Start Menu).
2. Search for **"Windows Terminal"**.
3. Click **"Get"** or **"Install"**.
4. Once installed, open it from the Start Menu.
5. You can set it as your default terminal in VS Code by going to Settings and searching `Terminal > External: Windows Exec` and setting it to `wt.exe`.

---

## Your First Professional Project Folder

### Step 8: Create the Folder Structure

Professional Python projects follow a standard structure. We will create it now.

1. Open File Explorer.
2. Navigate to `C:\Users\Viraj\Documents\` (or wherever you keep your work).
3. Create a new folder named: **`bootcamp-python`**
4. Inside `bootcamp-python`, create these folders and files:

```
bootcamp-python/
├── src/                    ← All your Python code lives here
│   └── __init__.py         ← Makes this a Python package
├── tests/                  ← All your tests live here
│   └── __init__.py
├── data/                   ← Sample data files (CSV, JSON, etc.)
├── docs/                   ← Documentation, notes, diagrams
├── notebooks/              ← Jupyter notebooks (if needed)
├── scripts/                ← Standalone utility scripts
├── .vscode/                ← VS Code settings for this project
│   └── settings.json
├── .gitignore              ← Tells Git what files to ignore
├── README.md               ← Project description
├── requirements.txt        ← List of Python packages
└── setup.py                ← Project metadata (optional for now)
```

5. Create each folder by right-clicking → New → Folder.
6. Create each file by right-clicking → New → Text Document, then rename it (including the extension).

**Pro tip:** To create the `.vscode` folder, you must type the name exactly as `.vscode` (with the dot). Windows will warn you about the name, but click **Yes** to confirm.

---

### Step 9: Create `.gitignore`

The `.gitignore` file tells Git which files to ignore (not track). This is CRITICAL.

1. Open `bootcamp-python` folder in VS Code (File → Open Folder → select `bootcamp-python`).
2. Click on `.gitignore` in the Explorer panel.
3. Paste this content exactly:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/settings.json
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data (large files)
*.csv
*.xlsx
*.db
*.sqlite3
```

4. Save the file (`Ctrl + S`).

**Why this matters:**  
Without `.gitignore`, Git will try to track Python cache files, virtual environments, and large data files. This makes your repository huge and unprofessional. Every company has a `.gitignore`. Every single one.

---

### Step 10: Create `README.md`

Every professional project has a README. It is the first thing anyone sees on GitHub.

1. In VS Code, click on `README.md`.
2. Paste this:

```markdown
# Bootcamp Python

Professional Python projects created during the AI Automation & Data Analytics Bootcamp.

## Projects

- Project 1: Personal Expense Tracker (Coming Soon)

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`

## Author

Viraj — B.Sc. Data Science 2026
```

3. Save the file.

---

### Step 11: Create `requirements.txt`

This file lists all Python packages your project needs. Right now it will be empty, but we will fill it as we go.

1. Click on `requirements.txt`.
2. Paste this (these are common packages we will use):

```text
# Core
python-dotenv>=1.0.0

# Data
pandas>=2.0.0
numpy>=1.24.0
openpyxl>=3.1.0

# Web
requests>=2.31.0
beautifulsoup4>=4.12.0

# Testing
pytest>=7.4.0

# Linting & Formatting
black>=23.0.0
ruff>=0.1.0
```

3. Save.

**Note:** We will NOT install these yet. We will create a virtual environment first (Day 2 or 3).

---

## Your First Python Program

### Step 12: Write `hello_bootcamp.py`

1. In VS Code, right-click on the `src/` folder → **New File**.
2. Name it: `hello_bootcamp.py`
3. Type this code EXACTLY:

```python
"""
hello_bootcamp.py

My first professional Python program.
Author: Viraj
Date: (today's date)
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
```

4. Save the file (`Ctrl + S`).

---

### Step 13: Run Your First Program

**Method 1: Using VS Code Terminal**
1. In VS Code, press `` Ctrl + ` `` (backtick) to open the terminal.
2. Make sure you are in the `bootcamp-python` folder.
3. Type: `python src/hello_bootcamp.py`
4. Press Enter.
5. Type your name when prompted.
6. You should see the greeting message.

**Method 2: Using Code Runner Extension**
1. Open `hello_bootcamp.py` in the editor.
2. Press `Ctrl + Alt + N`.
3. The output will appear in the "Output" panel at the bottom.

**Method 3: Using Right-Click**
1. Right-click in the code editor.
2. Click **"Run Python File in Terminal"**.

---

### Step 14: Initialize Git and Make Your First Commit

1. In the VS Code terminal, type: `git init`
   - You should see: `Initialized empty Git repository in C:/Users/.../.git/`

2. Type: `git add .`
   - This stages all your files for commit.

3. Type: `git commit -m "Initial commit: Project structure and first Python program"`
   - This saves a snapshot of your project.

4. Verify with: `git log`
   - You should see your commit with your name, email, date, and message.

**Congratulations. You are now using Git like a professional engineer.**

---

## Common Beginner Mistakes (Day 1)

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| Forgetting to check "Add Python to PATH" | Rushing through installation | Uninstall Python, reinstall, CHECK THE BOX |
| Typing `python` and getting "not recognized" | PATH issue or Python not installed | Verify installation, restart terminal |
| Git commit says "Please tell me who you are" | Forgot `git config` | Run `git config --global user.name` and `user.email` |
| VS Code says "Python interpreter not selected" | No Python selected in VS Code | Press `Ctrl + Shift + P`, type "Python: Select Interpreter", choose Python 3.11 |
| `.gitignore` not working | File already tracked by Git | Run `git rm -r --cached .` then `git add .` then `git commit` |
| `__init__.py` confusion | Thinking it's where code goes | It's usually EMPTY. It just tells Python "this folder is a package." |

---

## Best Practices (Already Applied Today)

1. **Every project gets a folder.** No more `script1.py` on the Desktop.
2. **Every project gets a README.** Even if it's just you.
3. **Every project gets a `.gitignore`.** Always.
4. **Every project gets a `src/` folder.** Source code lives here.
5. **Every project gets a `tests/` folder.** Tests live here.
6. **Every Python file gets a docstring.** The triple-quoted text at the top explains what the file does.
7. **Every function gets a docstring.** It explains what the function does, what it takes, and what it returns.
8. **Use `if __name__ == "__main__":`** This separates reusable code from execution code.
9. **Use type hints.** `name: str` and `-> str` tell other engineers (and your future self) what types to expect.

---

## Mini Exercise (Complete Before Day 2)

**Exercise 1.1: Modify the Greeting**

Edit `hello_bootcamp.py` to also ask for the user's city and include it in the greeting.

Example output:
```
==================================================
BOOTCAMP PYTHON — Day 1
==================================================
Enter your name: Viraj
Enter your city: Mumbai
Hello, Viraj from Mumbai! Welcome to the bootcamp.

Your environment is ready. Let's build something amazing.
==================================================
```

**Hints:**
- Add another `input()` call.
- Modify the `greet()` function to accept a second parameter.
- Update the `f-string` to include the city.

**Exercise 1.2: Create a Math Function**

Add a new function `calculate_age(birth_year: int) -> int` that calculates how old the user is.

- Ask the user for their birth year.
- Use `2026` as the current year (or `import datetime` and get the real year for bonus points).
- Print: "You are approximately X years old."

**Exercise 1.3: Git Commit Your Changes**

After completing the exercises:
1. `git add .`
2. `git commit -m "Day 1 exercises: Added city greeting and age calculator"`
3. `git log` to verify.

---

## Mini Project Preview (Week 1 End)

By the end of Week 1, you will build a **Personal Expense Tracker** (Project 1). It will:
- Store expenses in a JSON file.
- Allow adding, viewing, and deleting expenses.
- Calculate total spending by category.
- Use functions, file I/O, dictionaries, and lists.
- Be fully committed to Git with a professional README.

---

## Challenge Project (Week 2 Preview)

After mastering variables, data types, and control flow, you will build a **Password Manager (CLI)**. It will:
- Store passwords encrypted (using basic encryption).
- Allow adding, retrieving, and deleting passwords.
- Validate password strength.
- Use dictionaries, file I/O, exception handling, and modules.

---

## Interview Questions (Day 1 Level)

1. **What is the difference between an IDE and a text editor?**
2. **Why do we use Git in professional development?**
3. **What is the purpose of `.gitignore`?**
4. **What does `if __name__ == "__main__":` do?**
5. **Why do we use type hints in Python?**
6. **What is a docstring and why is it important?**
7. **What is the difference between `src/` and `tests/` folders?**

*(I will quiz you on these at the end of the week.)*

---

## Resume Relevance

**What you can already put on your resume after Day 1:**

> "Set up professional Python development environment with VS Code, Git, and virtual environment best practices."

**What you will add after Week 1:**

> "Built a Personal Expense Tracker in Python using file I/O, JSON, and modular programming. Managed project with Git version control and professional documentation."

---

## Next Lesson Preview (Day 2)

**Topic:** Python Variables, Data Types, and Operators — The Professional Way

**What you will learn:**
- How Python handles memory (why `a = b` can be dangerous).
- The difference between `==` and `is`.
- Mutable vs Immutable types (the #1 source of Python bugs).
- Type casting and when to use it.
- The `math` module and real business calculations.

---

## ✅ Day 1 Checklist

Before you tell me "Day 1 is complete," confirm EACH of these:

- [ ] Python 3.11 installed and `python --version` works.
- [ ] Git installed and `git --version` works.
- [ ] Git configured with my name and email.
- [ ] VS Code installed and opened.
- [ ] All 10 VS Code extensions installed.
- [ ] VS Code settings configured (tab size, auto save, etc.).
- [ ] Windows Terminal installed (optional).
- [ ] `bootcamp-python` folder created with ALL subfolders.
- [ ] `.gitignore` created and saved.
- [ ] `README.md` created and saved.
- [ ] `requirements.txt` created and saved.
- [ ] `hello_bootcamp.py` written and runs successfully.
- [ ] Git initialized with `git init`.
- [ ] First commit made with `git commit`.
- [ ] Exercise 1.1 completed (city greeting).
- [ ] Exercise 1.2 completed (age calculator).
- [ ] Exercise 1.3 completed (git commit exercises).

---

**When you are done, tell me: "Day 1 complete." I will review your setup and then we begin Day 2.**


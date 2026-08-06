# Progress Tracker

## Your Info
- **Name:** Viraj Indais
- **Start Date:** 2026-07-01
- **Target Job Title:** AI Automation Engineer / Data Analyst (Python + SQL + AI)
- **Current Phase:** Phase 2 — Python Automation
- **Current Day:** Phase 2, Day 3 complete (groupby). Project 5 (Automated Report Generator) — architecture defined, Stage 1 scaffolding in progress.

---

## Overall Progress

| Phase | Status | Start Date | End Date | Notes |
|-------|--------|------------|----------|-------|
| 1. Professional Python | 🟡 Paused | 2026-07-01 | — | Core skills complete. Project 1 (Expense Tracker) and Project 2 (Password Manager) built, tested, merged. **Projects 3 (Contact Book) and 4 (Task Scheduler) deliberately deferred, not abandoned** — decision made 2026-07-30 to move to Phase 2 now and return to these later when time allows. |
| 2. Python Automation | 🟡 In Progress | 2026-07-30 | — | Day 1 done: Pandas fundamentals — Series/DataFrame model, `read_csv`, `.info()`/`.describe()`, single vs. double bracket column selection.  Day 2: boolean indexing (&/\|), .sort_values(), .loc vs .iloc — confirmed filtered DataFrames keep original index labels. Day 3: .groupby() — single/multi-key aggregation, .agg(), .reset_index(). All three days: code correct, README + notes/phase2/ committed. **Project 5 scaffolding started** — 3-stage architecture (pandas load/transform → OpenPyXL output → email delivery), folder structure, and Stage 1 skeleton (data_loader.py, transformer.py, main.py) defined; TODOs not yet implemented. |
| 3. REST APIs | ⚪ Not Started | — | — | |
| 4. Modern AI | ⚪ Not Started | — | — | |
| 5. UiPath | ⚪ Not Started | — | — | |
| 6. Data Engineering | ⚪ Not Started | — | — | |
| 7. Cloud & Deployment | ⚪ Not Started | — | — | |
| Capstone Project | ⚪ Not Started | — | — | |

---

## Weekly Reviews

### Week 1 Review
**Date:** —
**Topics Covered:** —
**Projects Completed:** —
**Code Review Notes:** —
**Mock Interview Score:** —
**What to Improve:** —
**Next Week Focus:** —

---

## Skills Mastered

- [x] Windows Command Line & PowerShell
- [x] Professional Project Structure
- [x] Git Basics (init, add, commit, push)
- [x] GitHub (repo created, code pushed, branches/PRs)
- [x] Python Variables & Data Types
- [x] Python Operators & Strings
- [x] Python Strings — slicing & methods (Day 3)
- [x] Python Lists, Tuples, Sets, Dictionaries (Day 4)
- [x] Python Loops & Control Flow (Day 5)
- [x] Python Functions & Scope (Day 6)
- [x] Python Modules & Packages (Day 7)
- [x] Python OOP — Classes & Objects (Day 8)
- [x] Python OOP — Inheritance & Polymorphism (Day 9)
- [x] Python File Handling (txt, csv, json, excel) — (Day 10)
- [x] Python Regex & Datetime (Day 11)
- [x] Python Exception Handling & Logging (Day 12)
- [x] Python Testing (Pytest) (Day 13)
- [x] Python Decorators & Generators (Day 14)
- [x] Python Virtual Environments & pip (Day 15)
- [x] GitHub (branches, PRs — beyond basics) (Day 16)
- [x] Clean Code Principles (Day 17)
- [x] Basic symmetric encryption (cryptography / Fernet) (Project 2)
- [x] Reliable file paths with pathlib + `__file__` (Project 2)
- [x] Secure secrets handling — getpass, git-ignoring keys, logging discipline (Project 2)
- [x] Pandas — Series/DataFrame model, `read_csv`, exploration methods, column selection (Phase 2, Day 1)
- [x] Pandas — boolean filtering, `.sort_values()`, `.loc`/`.iloc` (Phase 2, Day 2)
- [x] Pandas — `.groupby()`, multi-key aggregation, `.agg()`, `.reset_index()` (Phase 2, Day 3)
- [ ] OpenPyXL — formatted Excel report generation (Project 5, Stage 2 — next)
- [ ] Email automation — smtplib (Project 5, Stage 3 — after)
---

## Projects Completed

- [x] Project 1: Personal Expense Tracker *(OOP-based — Expense/RecurringExpense with polymorphic to_dict(); CSV persistence; regex-validated amounts AND categories; datetime timestamps; @log_call decorator; exception handling + logging; pytest coverage; black/ruff-reviewed)*
- [x] Project 2: Password Manager (CLI) *(Fernet symmetric encryption; JSON vault; getpass; pathlib/`__file__`; @log_call decorator with no secrets logged; full Add/View/Retrieve/Delete menu, tested end-to-end)*
- [ ] Project 3: Contact Book with Search *(deferred — Phase 1 skills already mastered, will return to this later)*
- [ ] Project 4: Task Scheduler *(deferred — same reason as above)*
- [ ] Project 5: Automated Report Generator *(*🟡 scaffolding — business problem, 3-stage architecture, folder structure, and data source (fresh simulated sales data) agreed. Stage 1 skeleton given: data_loader.py, transformer.py, main.py. Not yet implemented.)*)*
- [ ] Project 6: Web Scraper for Job Listings
- [ ] Project 7: PDF Invoice Parser
- [ ] Project 8: Database Sync Tool
- [ ] Project 9: REST API for Tasks
- [ ] Project 10: API Integration Dashboard
- [ ] Project 11: AI Email Classifier
- [ ] Project 12: RAG Document Chatbot
- [ ] Project 13: AI Report Generator
- [ ] Project 14: Multi-Agent Workflow
- [ ] Project 15: Invoice Processing Bot (UiPath)
- [ ] Project 16: Email Automation Bot
- [ ] Project 17: Data Pipeline (ETL)
- [ ] Project 18: Cloud Data Sync
- [ ] Project 19: Mid-Capstone
- [ ] Project 20: Final Capstone

---

## Career Prep Checklist

- [ ] LinkedIn headline updated
- [ ] GitHub profile polished
- [ ] Resume draft v1
- [ ] Portfolio website live
- [ ] 5 GitHub projects with READMEs
- [ ] Mock interview #1 completed
- [ ] Mock interview #2 completed
- [ ] Mock interview #3 completed
- [ ] First job application sent
- [ ] Salary research completed

---

## Notes & Reflections

- **2026-07-09:** Switched bootcamp mentorship from Kimi K2.6 to Claude. Continuing same roadmap, no reset, picked up at Day 5.
- **2026-07-28:** Project 2 (Password Manager) completed and tested end-to-end. Harder than Project 1 — new library, real cwd/path bug, bytes-vs-str all stacked close together — flagged as a pacing issue mid-project, fixed by slowing down.
- **2026-07-30:** Decided to defer Project 3 (Contact Book) and Project 4 (Task Scheduler) and move to Phase 2 now, after two Phase 1 projects. Both remain on the roadmap as outstanding, not dropped — revisit when time allows.
- **2026-07-30 (Phase 2, Day 1):** Pandas fundamentals covered — Series/DataFrame model, `read_csv`, `.info()`/`.describe()`, single vs. double bracket selection. Real discovery, not from the lesson: pandas 3.0 changed the default string dtype from `object` to `str` (PDEP-14) — output didn't match textbook expectations, version drift rather than a bug. Logged as a durable lesson, same category as the Password Manager path/bytes issues. Day 1 code correct on first pass; challenge Q2 (when to deliberately prefer a DataFrame-shaped single column over a Series) still open, one retry submitted, not yet fully correct.
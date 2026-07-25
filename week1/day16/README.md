# Week 1, Day 16: Git Branches & Pull Requests

> **Learning Objectives:**
> 1. Understand why professional teams never commit directly to `main`.
> 2. Create, work on, and push a feature branch.
> 3. Open, review, and merge a Pull Request on GitHub.
> 4. Clean up branches correctly after merging, both remotely and locally.
> 5. Know the common mistakes: missing upstream tracking, stale branches, vague names.

---

## Business Motivation

Every day so far, commits went straight to `main`. Fine solo — not how any real team operates. If `main` is broken, everyone's broken. A **branch** isolates work until it's ready; a **Pull Request** is the formal, reviewable step where that work merges back in. This is the single most universal professional Git workflow, and a near-guaranteed interview topic.

---

## What It Is

**A branch** — an independent, parallel line of development. Creating one gives an isolated copy of the codebase; nothing done there touches `main` until explicitly merged.

**A Pull Request** — a GitHub feature (not Git itself) formalizing "merge this branch into main," with review, diff view, and comments. Solo, you review and merge your own; on a team, someone else approves first.

---

## The Full Workflow — Must Know

```bash
# 1. Start from an up-to-date main
git checkout main
git pull

# 2. Create and switch to a new branch
git checkout -b day16-practice
# (modern alternative: git switch -c day16-practice)

# 3. Make a small, real change, then commit as usual
git add .
git commit -m "Fix typo in README setup instructions"

# 4. Push the branch — -u links it for future plain `git push`
git push -u origin day16-practice

# 5. On GitHub.com: click "Compare & pull request" banner,
#    write a title/description, click "Create pull request"

# 6. Merge it on GitHub ("Merge pull request"), then delete the branch there

# 7. Clean up locally
git checkout main
git pull
git branch -d day16-practice
```

---

## Common Mistakes (Day 16)

| Mistake | Fix |
|---------|-----|
| Committing straight to `main` out of habit | Branch first for anything beyond a trivial fix |
| Forgetting `-u` on the first push | Later `git push` complains about no upstream — add `-u origin <branch>` once |
| Never deleting merged branches | Delete both the GitHub copy and the local copy after merging |
| Vague branch names (`test`, `new-stuff`) | Use `type/short-description` — e.g., `fix/readme-typo` |
| Branching off a stale `main` | Always `git pull` on `main` before creating a new branch |
| No PR description | Even solo, it's documentation of *why* — a habit that transfers directly to team settings |

## Best Practices

1. One branch per feature/fix — small and focused.
2. Descriptive branch names, `type/short-description` format.
3. Real PR descriptions, even solo.
4. Delete branches after merging, remote and local both.
5. Pull `main` before every new branch.

**Good to know:** `git switch` as the modern alternative to `git checkout`. **Learn later:** resolving merge conflicts, squash-merge vs. regular merge vs. rebase, protected branches requiring review — all matter more once working on an actual team.

---

## Today's Task

Hands-on workflow exercise, no code TODOs: run through the 7 steps above on the real repo with one small, genuine change (e.g., a doc fix). Confirm the PR merged successfully on GitHub and the local branch was cleaned up.

---

## Interview Questions (Day 16 Level)

1. Why do professional teams avoid committing directly to `main`?
2. What's the difference between a Git branch and a GitHub Pull Request?
3. What does the `-u` flag do on `git push -u origin <branch>`?
4. Why should branches be deleted after merging?
5. What's a merge conflict, at a high level, and when does it happen?

---

## Resume Relevance

> "Used feature-branch Git workflow with Pull Requests for all code changes, following professional collaborative development practices."

---

## Next Lesson Preview (Day 17)

**Topic:** Clean Code Principles — the final item on the Phase 1 Skills Mastered list. After that, focus shifts to building Projects 2–4 (Password Manager, Contact Book, Task Scheduler) using everything learned across Phase 1, before moving into Phase 2.

---

## ✅ Day 16 Checklist

- [ ] Created a feature branch off an up-to-date `main`.
- [ ] Made a real change and committed it on the branch.
- [ ] Pushed with `-u` and opened a Pull Request on GitHub.
- [ ] Merged the PR and deleted the branch (remote + local).
- [ ] `main` pulled locally, confirmed the change is there.
- [ ] I can answer all 5 interview questions.

---

**When you are done, tell me: "Day 16 complete."**

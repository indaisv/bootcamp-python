# Day 16: Git Branches & Pull Requests — Notes

## 1. Revision Notes

**The core problem this solves:** every commit so far went straight to `main`. Fine solo, but on any real team, a broken commit on `main` breaks things for everyone. A branch isolates work in a separate, independent line of development until it's actually ready to merge.

**The full cycle, in order:**
1. Start from an up-to-date `main` (`git checkout main` + `git pull`) — always branch off current code, not stale code.
2. Create + switch to a new branch (`git checkout -b <name>`).
3. Make changes, commit as usual.
4. Push with `-u` on the *first* push of that branch (`git push -u origin <branch>`) — this sets up "upstream tracking" so future `git push` commands on that branch work without repeating the branch name.
5. Open a Pull Request on GitHub — a formal "please merge this into main" request, with a description of what changed and why.
6. Merge the PR (on a team: after review/approval; solo: reviewing and merging your own).
7. Clean up: switch back to `main`, `git pull` to bring the merged change down locally, then `git branch -d <branch>` to delete the now-merged branch locally too (GitHub deleting its remote copy doesn't delete your local one automatically).

**Real thing hit today:** the "Merge pull request" button showed a "blocked" state briefly right after opening the PR. This is usually just GitHub's async mergeability check still computing — refreshing after a few seconds typically resolves it. If it persists, it points to a branch protection rule under repo Settings → Branches (e.g., requiring a review or a status check that never runs on a solo repo).

**How to actually confirm a merge succeeded, beyond just "the button worked":** `git branch -d <branch>` (lowercase `-d`, not `-D`) is a *safe* delete — Git refuses it if the branch has any unmerged changes. If that command succeeds without needing the force flag, that's Git itself confirming the branch was fully, cleanly merged first.

---

## 2. Cheat Sheet

```bash
# Start clean, every time
git checkout main
git pull

# New branch
git checkout -b feature/short-description
# (modern alt: git switch -c feature/short-description)

# Work + commit as usual
git add .
git commit -m "Clear, specific message"

# First push of this branch — sets upstream tracking
git push -u origin feature/short-description

# ... open PR on GitHub, merge it there ...

# Clean up locally after merge
git checkout main
git pull
git branch -d feature/short-description   # safe delete — fails if not fully merged
```

**Branch naming convention:** `type/short-description` — e.g., `fix/readme-typo`, `feature/recurring-expense-menu`.

---

## 3. Active Recall Questions

1. Why do professional teams avoid committing directly to `main`?
2. What does `-b` do in `git checkout -b <branch>`, in one sentence?
3. What does the `-u` flag on `git push -u origin <branch>` actually set up, and why does it only need to be done once per branch?
4. What's the difference between a Git branch and a GitHub Pull Request?
5. After merging a PR on GitHub, why does the local branch still need to be deleted separately with `git branch -d`?
6. Why does `git branch -d` sometimes refuse to delete a branch — what is it actually protecting against?
7. If a PR's merge button is blocked right after opening it, what's the first thing to try before assuming something's actually wrong?
8. Why is a real PR description a good habit even when working completely solo?

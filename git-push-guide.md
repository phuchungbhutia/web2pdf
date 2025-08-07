

### 📤 Git Push Error: How to Fix "Failed to Push Some Refs"

If you see this error:

```
error: failed to push some refs to 'https://github.com/your-repo.git'
hint: Updates were rejected because the tip of your current branch is behind
```

It means your local branch is **behind** the remote branch. Here's how to fix it:

---

### ✅ Step-by-Step Fix

#### 1. Pull Remote Changes with Rebase

```bash
git pull origin main --rebase
```

This fetches the latest changes from GitHub and applies your local commits on top.

---

#### 2. Resolve Merge Conflicts (if any)

If Git shows a conflict:

* Open the conflicting file
* Fix the conflict manually
* Then run:

```bash
git add <filename>
git rebase --continue
```

Repeat until rebase is complete.

---

#### 3. Push Your Changes

```bash
git push origin main
```

---

### 🧠 Why This Happens

Git protects the remote branch from being overwritten. You must first integrate remote changes before pushing your own.

---

### ⚠️ Optional: Force Push (Use with Caution)

If you're sure you want to overwrite the remote branch:

```bash
git push origin main --force
```

> ⚠️ This can delete remote commits. Only use if you're working solo or know what you're doing.

---

## 🔗 Fix: "No Upstream Branch" Error

If you see:

```
fatal: The current branch main has no upstream branch.
```

Run this to link your local branch to the remote:

```bash
git push --set-upstream origin main
```

This sets the upstream so future `git push` and `git pull` commands work automatically.

---

### 🛠 Optional: Set It Globally

To avoid this issue in all future repos:

```bash
git config --global push.autoSetupRemote true
```

This tells Git to auto-link branches when pushing for the first time.

---

# Update Course Materials

Help the student update their course materials safely.

## Your Task

Guide the student through updating their course repository while preserving their work.

### Check Current State

First, check the current git status:
```bash
git status
git branch
```

### Update Workflow

1. **If on main branch with no changes:**
   ```bash
   git pull origin main
   ```

2. **If on a working branch (recommended):**
   ```bash
   # Stash any uncommitted changes
   git stash

   # Switch to main and update
   git checkout main
   git pull origin main

   # Return to working branch
   git checkout -

   # Optionally merge updates
   git merge main

   # Restore stashed changes
   git stash pop
   ```

3. **If on main with local changes:**
   Recommend creating a branch first:
   ```bash
   git checkout -b my-work
   git add .
   git commit -m "Save my work before updating"
   git checkout main
   git pull origin main
   git checkout my-work
   git merge main
   ```

### Handle Merge Conflicts

If notebook conflicts occur:
```bash
git mergetool --tool=nbdime
```

For other conflicts, help the student understand and resolve them.

### Verify Update

After updating, confirm:
```bash
git log --oneline -5
```

Show what changed in the update.

### Troubleshooting

- **"You have uncommitted changes"**: Stash or commit first
- **"Merge conflict"**: Use nbdime for notebooks, manual resolution for others
- **"Not a git repository"**: They need to clone the course first

Run the appropriate update commands based on the student's current state.

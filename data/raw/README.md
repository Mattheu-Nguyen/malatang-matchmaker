# data/raw/ — Raw Yelp Dataset

**Drop the Yelp dataset files HERE.**

This folder is intentionally excluded from git (see `.gitignore`) because
the Yelp dataset is too large for GitHub.

---

## What files go here?

The Yelp Open Dataset typically comes as multiple JSON files:

| File | Contents |
|------|----------|
| `yelp_dataset.json` | Business/restaurant info (name, location, categories, stars) |
| `yelp_academic_dataset_review.json` | Review text for each business |
| `yelp_academic_dataset_business.json` | Alternative business file name |

Use whichever files you were given. Check what columns are inside before writing code.

---

## How to share this data with teammates

Since the JSON is too large for GitHub, share it via:
- Google Drive / OneDrive link in your group chat
- USB drive
- The datathon's provided shared folder

---

## NEVER commit these files to GitHub

Large JSON files will break GitHub and slow down the whole team.
The `.gitignore` already blocks them, but double-check before `git add .`

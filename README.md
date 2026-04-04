# 🍲 Malatang Finder — Datathon Project

A personalized Malatang restaurant recommendation website.
Users input their preferences and get matched to real restaurants from the Yelp dataset.

---

## Team

| Person | Role | Folder |
|--------|------|--------|
| Person 1 | Data Engineer | `data/` |
| Person 2 | Backend Developer | `backend/` |
| Person 3 | Recommendation Engineer | `recommendation/` |
| Person 4 | Frontend Developer | `frontend/` |

---

## Tech Stack

- **Frontend**: HTML / CSS / JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Data Processing**: pandas
- **Dataset**: Yelp JSON

---

## Project Structure

```
datathon-malatang/
├── data/               ← Person 1: process Yelp JSON → SQLite
├── backend/            ← Person 2: Flask API
├── recommendation/     ← Person 3: scoring/matching algorithm
├── frontend/           ← Person 4: HTML form + results page
└── docs/               ← architecture diagrams and agreements
```

---

## How to Run (once everything is built)

### 1. Set up Python environment
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### 2. Process the Yelp data (Person 1 must do this first)
```bash
cd data
python process_data.py
```
This creates `data/processed/malatang.db`

### 3. Start the Flask server
```bash
cd backend
python app.py
```
Server runs at: http://localhost:5000

### 4. Open the frontend
Open `frontend/index.html` directly in your browser.

---

## Team Communication

- Before writing code, read your folder's README carefully
- On Day 1 as a team: agree on DB schema + API response format (document in `docs/architecture.md`)
- Use GitHub issues or group chat to flag blockers early
- If your work depends on someone else's piece, test with mock/fake data first

---

## Git Workflow

```bash
# Before starting work each day
git pull

# After finishing a feature
git add .
git commit -m "short description of what you did"
git push
```

Try not to edit other people's folders to avoid merge conflicts!

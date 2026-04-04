# System Architecture — Malatang Finder

This document describes how all four parts of the project connect.
**Fill in agreed details (table names, field names, API format) here during your Day 1 kickoff.**

---

## Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                        USER'S BROWSER                        │
│                                                              │
│   index.html  →  fills form  →  clicks submit               │
│       │                                                      │
│   main.js  →  POST /recommend  →  { preferences JSON }      │
└──────────────────────────┬───────────────────────────────────┘
                           │ HTTP POST
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                  FLASK BACKEND  (backend/)                   │
│                                                              │
│   app.py  →  routes/restaurants.py  →  POST /recommend      │
│       │                                                      │
│       └──  calls  recommendation/engine.py                  │
│                           │                                  │
│                           ▼                                  │
│   engine.py  →  queries SQLite  →  scores restaurants       │
│                           │                                  │
│                           ▼                                  │
│              returns ranked list of restaurants              │
└──────────────────────────┬───────────────────────────────────┘
                           │ JSON response
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                        USER'S BROWSER                        │
│                                                              │
│   main.js  →  renders results  →  results.html              │
└──────────────────────────────────────────────────────────────┘
```

---

## Team Responsibilities

| Person | Role | Folder | Depends On |
|--------|------|--------|------------|
| Person 1 | Data Engineer | `data/` | Yelp JSON dataset |
| Person 2 | Backend Dev | `backend/` | Person 1's DB schema |
| Person 3 | Recommendation | `recommendation/` | Person 1's data + Person 2's API |
| Person 4 | Frontend Dev | `frontend/` | Person 2's API response format |

---

## Agreed Interfaces
*(Fill these in together on Day 1 — this is the contract between team members)*

### Database Schema (Person 1 → Person 2 & 3)

**Table: `restaurants`**

| Column | Type | Notes |
|--------|------|-------|
| `business_id` | TEXT | |
| `name` | TEXT | |
| `address` | TEXT | |
| `city` | TEXT | |
| `state` | TEXT | |
| `stars` | REAL | |
| `review_count` | INTEGER | |
| `categories` | TEXT | |
| *(add more as needed)* | | |

> Person 1: update this table when your DB schema is finalized!

---

### User Preferences Format (Person 4 → Person 2 → Person 3)

This is the JSON object the frontend sends to the backend:

```json
{
  "spice_level": "high",
  "broth": "spicy_mala",
  "meats": ["beef", "pork"],
  "ingredients": ["fish_cake", "tofu"],
  "side_dishes": ["rice"]
}
```

> Confirm and update the exact field names and allowed values before coding!

---

### API Response Format (Person 2 → Person 4)

This is the JSON the backend returns to the frontend:

```json
[
  {
    "name": "Mala Hot Pot",
    "address": "123 Main St",
    "city": "San Francisco",
    "state": "CA",
    "stars": 4.5,
    "review_count": 200,
    "match_score": 87
  },
  ...
]
```

> Person 2: update this with the real fields once routes are built!

---

## Development Phases

| Phase | When | Who | What |
|-------|------|-----|------|
| Setup | Day 1 AM | Everyone | Clone repo, read READMEs, agree on schemas above |
| Build | Day 1-2 | Each person | Work in own folder using mock data |
| Integrate | Day 2-3 | Pairs | Connect DB → backend → frontend end-to-end |
| Polish | Day 3-4 | Everyone | Styling, scoring improvements, demo prep |

---

## Running the Project Locally

```
Terminal 1 — Start Flask server:
  cd backend
  python app.py

Browser — Open frontend:
  Open frontend/index.html in your browser
  (or use Live Server extension in VS Code)
```

The frontend talks to the backend at: `http://localhost:5000`

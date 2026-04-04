# Backend Folder — Person 2 (Backend Developer)

**Your job**: Build a Flask web server that accepts user preference requests from the
frontend, queries the SQLite database, runs the recommendation engine, and returns
a ranked list of restaurants as JSON.

---

## Your Tasks (in order)

### Step 1 — Set up your Python environment
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### Step 2 — Learn the DB schema from Person 1
Before writing any queries, ask Person 1:
- What is the SQLite file called and where is it? (`data/processed/malatang.db`)
- What are the table names?
- What are the column names?

Write these down in `database/README.md` so everyone has them.

### Step 3 — Build the database connection helper
Open `database/db.py` and follow the TODO comments.
This helper opens the SQLite connection so all routes can use it without repeating code.

### Step 4 — Build the Flask routes
Open `routes/restaurants.py` and follow the TODO comments.
You need to implement two endpoints:

| Method | Route | What it does |
|--------|-------|--------------|
| `GET` | `/restaurants` | Returns all restaurants as JSON (for testing) |
| `POST` | `/recommend` | Accepts user preferences, returns ranked recommendations |

### Step 5 — Connect the recommendation engine
The `/recommend` route should:
1. Read the user preferences from the request body (JSON)
2. Pass them to `recommendation/engine.py`'s main function
3. Return the ranked results as JSON

**Talk to Person 3** about:
- What format should preferences be passed in?
- What does the function return?

### Step 6 — Test your routes
Before connecting to the frontend, test with curl or Postman:
```bash
# Test GET all restaurants
curl http://localhost:5000/restaurants

# Test POST recommend
curl -X POST http://localhost:5000/recommend \
  -H "Content-Type: application/json" \
  -d '{"spice_level": "high", "broth": "spicy", "meats": ["beef", "pork"]}'
```

### Step 7 — Enable CORS
The frontend runs as a plain HTML file, not on a server, so the browser will block
requests unless you enable CORS. Add `flask-cors` to your app.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `app.py` | Flask app entry point — run this to start the server |
| `routes/restaurants.py` | API route definitions |
| `database/db.py` | SQLite connection helper |
| `requirements.txt` | Python package dependencies |

---

## Who Depends on You

- **Person 3** needs you to call their recommendation function correctly
- **Person 4 (Frontend)** needs to know the exact JSON format your API returns

Share a sample API response with Person 4 as soon as possible, like:
```json
[
  {
    "name": "Mala Hot Pot",
    "address": "123 Main St",
    "city": "San Francisco",
    "stars": 4.5,
    "match_score": 87
  }
]
```

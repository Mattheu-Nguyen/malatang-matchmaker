# Data Folder — Person 1 (Data Engineer)

**Your job**: Take the raw Yelp JSON dataset, filter it down to malatang/hot pot restaurants,
clean it up with pandas, and save it as a SQLite database for the backend to use.

---

## Your Tasks (in order)

### Step 1 — Drop the dataset in the right place
Put the Yelp JSON file(s) inside `data/raw/`.
See `data/raw/README.md` for details on which files to use.

### Step 2 — Explore the data first
Before writing any processing code, open the JSON and look at:
- What columns/fields exist?
- How is the "categories" field formatted?
- What does a typical restaurant record look like?
- What does a review record look like?

Write down your findings in a comment at the top of `process_data.py`.

### Step 3 — Filter for malatang restaurants
You only want restaurants relevant to malatang. Filter by keywords like:
- "Malatang", "Hot Pot", "Hotpot", "Mala", "Szechuan", "Chinese"

Keep only these columns (ask Person 2 if they need more):
- `business_id`
- `name`
- `address`
- `city`
- `state`
- `stars` (average rating)
- `review_count`
- `categories`

### Step 4 — Process reviews
Reviews are in a separate part of the Yelp dataset. For each restaurant:
- Find all its reviews
- Look for flavor keywords: spicy, mild, broth type, fish cake, beef, pork, etc.
- Maybe store the top keywords per restaurant, or a combined review text

### Step 5 — Save to SQLite
Create `data/processed/malatang.db` with at least these tables:
- `restaurants` — one row per restaurant
- (optional) `reviews` — one row per review

**IMPORTANT**: Before writing the DB, share your planned table/column names with Person 2
so they know how to query it!

### Step 6 — Verify your output
Run a quick test query to make sure the DB looks right.
Print the first 5 rows to confirm everything loaded.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `process_data.py` | Your main script — follow the TODO comments |
| `raw/` | Drop the raw Yelp JSON files here |
| `processed/` | The generated `malatang.db` goes here (auto-created by your script) |

---

## Who Depends on You

- **Person 2 (Backend)** needs the SQLite DB and the table/column names
- **Person 3 (Recommendation)** needs to know what data is available to score restaurants

Communicate early! They can work with mock data while you're building, but they need your
schema (table + column names) as soon as possible.

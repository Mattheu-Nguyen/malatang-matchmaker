# Recommendation Folder — Person 3 (Recommendation Engineer)

**Your job**: Build the algorithm that takes a user's malatang preferences and returns
a ranked list of restaurants that best match those preferences.

---

## Your Tasks (in order)

### Step 1 — Understand the user preferences
The frontend (Person 4) will collect these inputs from the user:

| Preference | Type | Example values |
|------------|------|----------------|
| `spice_level` | string | "mild", "medium", "high", "extra spicy" |
| `broth` | string | "spicy mala", "clear", "tomato", "mushroom" |
| `meats` | list | ["beef", "pork", "chicken", "lamb"] |
| `ingredients` | list | ["fish cake", "tofu", "mushroom", "noodles"] |
| `side_dishes` | list | ["rice", "fried dough", "sesame noodles"] |

> Confirm the exact field names with Person 4 early so you're aligned!

### Step 2 — Understand the available data
Talk to Person 1 about:
- What columns are in the `restaurants` table?
- Is there review text available? (useful for keyword matching)
- Are there any columns that map to spice level or broth type?

### Step 3 — Design your scoring logic
Your function should score each restaurant and sort them.
Ideas for scoring:

**Keyword matching** (most practical for this dataset):
- Search review text for words like "spicy", "mala", "mild", "fish cake", etc.
- Count how many preference keywords appear in the reviews

**Category matching**:
- Check if the restaurant's categories match the user's preferences
- E.g., if user wants "spicy" and categories include "Szechuan", give a bonus

**Star rating tiebreaker**:
- When two restaurants score the same, rank the higher-rated one first

### Step 4 — Write the scoring function in engine.py
Follow the TODO comments in `engine.py`.
Your main function signature should look like:
```python
def get_recommendations(preferences):
    # preferences is a dict from the API request
    # returns a list of dicts, sorted by match score
```

### Step 5 — Test with sample data
Before connecting to the real DB, test your function with hardcoded fake data.
Make sure it returns a sorted list and handles missing preferences gracefully.

### Step 6 — Connect to the real DB
Once Person 1's DB is ready, update your function to query the real data.

---

## Who Depends on You

- **Person 2 (Backend)** will call `get_recommendations(preferences)` from the `/recommend` route
- Agree with Person 2 on the exact input dict format and output list format

## Files in This Folder

| File | Purpose |
|------|---------|
| `engine.py` | Your main recommendation function |

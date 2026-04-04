# backend/routes/ — API Route Definitions

This folder contains Flask "blueprints" — groups of related API routes.
Each file handles one area of the app.

---

## What is a Blueprint?

A Flask blueprint is a way to organize routes into separate files instead of
putting everything in `app.py`. You define routes in a blueprint file, then
register it in `app.py`.

Basic pattern:
```python
from flask import Blueprint
restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    # your code here
    pass
```

---

## Files in This Folder

| File | Routes inside |
|------|--------------|
| `restaurants.py` | `GET /restaurants` and `POST /recommend` |

---

## Routes to Build

### GET /restaurants
- No input required
- Query the SQLite DB for all restaurants
- Return a JSON list of all restaurants
- Useful for testing that the DB connection works

### POST /recommend
- Input: JSON body with user preferences (defined together with Person 3 and Person 4)
- Pass preferences to the recommendation engine
- Return a ranked JSON list of matching restaurants

Example input body:
```json
{
  "spice_level": "high",
  "broth": "spicy mala",
  "meats": ["beef", "pork"],
  "ingredients": ["fish cake", "tofu"],
  "side_dishes": ["rice"]
}
```

Example output:
```json
[
  {
    "name": "Mala Hot Pot",
    "address": "123 Main St",
    "city": "San Francisco",
    "stars": 4.5,
    "match_score": 87
  },
  ...
]
```

# backend/database/ — SQLite Connection Helper

This folder contains the helper that opens a connection to the SQLite database.
All routes use this helper instead of opening the DB directly — keeps things clean.

---

## Database Location

The SQLite database is at: `data/processed/malatang.db`
It is created by Person 1's `data/process_data.py` script.

---

## Table Schema (fill this in after talking to Person 1!)

**Table: `restaurants`**

| Column | Type | Description |
|--------|------|-------------|
| `business_id` | TEXT | Unique Yelp ID |
| `name` | TEXT | Restaurant name |
| `address` | TEXT | Street address |
| `city` | TEXT | City |
| `state` | TEXT | State |
| `stars` | REAL | Average star rating |
| `review_count` | INTEGER | Number of reviews |
| `categories` | TEXT | Comma-separated categories |

> Update this table with the real column names once Person 1 finalizes the DB!

---

## How to use db.py in a route

```python
from database.db import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM restaurants LIMIT 10")
rows = cursor.fetchall()
conn.close()
```

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `db.py` | Returns an open sqlite3 connection to malatang.db |

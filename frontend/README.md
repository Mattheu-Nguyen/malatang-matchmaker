# Frontend Folder — Person 4 (Frontend Developer)

**Your job**: Build the user-facing website. Users fill out a preference form, hit submit,
and see a list of recommended malatang restaurants.

---

## Your Tasks (in order)

### Step 1 — Build the preference form (index.html)
Open `index.html` and build a form with these input fields:

| Field | Input Type | Options |
|-------|-----------|---------|
| Spice Level | Dropdown or slider | Mild / Medium / High / Extra Spicy |
| Broth Type | Dropdown | Spicy Mala / Clear / Tomato / Mushroom |
| Meats | Checkboxes | Beef / Pork / Chicken / Lamb / Seafood |
| Ingredients | Checkboxes | Fish Cake / Tofu / Mushroom / Noodles / Veggies |
| Side Dishes | Checkboxes | Rice / Fried Dough / Sesame Noodles |

Make the form fun and on-brand! This is a malatang themed site.

### Step 2 — Style everything (css/style.css)
See `css/README.md` for styling suggestions.
Keep it clean, readable, and mobile-friendly.

### Step 3 — Write the form submit logic (js/main.js)
When the user clicks submit:
1. Collect all the form values into a JavaScript object
2. Send a POST request to `http://localhost:5000/recommend` using `fetch()`
3. Wait for the response
4. Display the results on the page (or redirect to results.html)

See `js/README.md` for the fetch pattern.

### Step 4 — Build the results display (results.html)
Show each recommended restaurant as a card with:
- Restaurant name
- Address and city
- Star rating (show as stars ⭐)
- Match score or "why it matched" text

### Step 5 — Handle loading and errors
- Show a loading spinner or message while the fetch is running
- Show a friendly error message if the API call fails
- Show "No results found" if the list is empty

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `index.html` | Preference input form |
| `results.html` | Recommendation results display |
| `css/style.css` | All styling |
| `js/main.js` | Form logic and API fetch calls |

---

## Important: Coordinate with Person 2

Before writing your fetch call, ask Person 2 what the API response JSON looks like.
You need to know the exact field names to display results correctly.

Example response to expect:
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

Also share your final form field names with Person 3 so they know
what keys to expect in the preferences object.

---

## Testing Without the Backend

While the backend isn't ready yet, test your UI with hardcoded fake data.
In `main.js`, you can comment out the fetch call and use a fake response array
to build and test the results display.

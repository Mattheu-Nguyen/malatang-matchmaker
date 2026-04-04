# frontend/js/ — JavaScript

All client-side logic lives in `main.js`. No frameworks — just plain JavaScript.

---

## What main.js needs to do

### On index.html (form page)
1. Listen for the form submit event
2. Collect all form field values into a preferences object
3. POST that object to `http://localhost:5000/recommend`
4. Show a loading indicator while waiting
5. When results arrive, either display them on the page or redirect to results.html

### On results.html (results page)
1. Read the results data (from sessionStorage if you redirected)
2. Loop through each restaurant and create a card element
3. Append all cards to `#results-container`

---

## The fetch() pattern

```javascript
fetch('http://localhost:5000/recommend', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(preferences)
})
  .then(response => response.json())
  .then(data => {
    // data is the array of restaurant results
    // display them here
  })
  .catch(error => {
    // something went wrong — show error message
    console.error(error);
  });
```

---

## Passing data between pages (sessionStorage)

If you redirect from index.html to results.html, use sessionStorage to pass the data:

**On index.html** (before redirecting):
```javascript
sessionStorage.setItem('results', JSON.stringify(data));
window.location.href = 'results.html';
```

**On results.html** (reading the data):
```javascript
const results = JSON.parse(sessionStorage.getItem('results'));
```

---

## Files

| File | Purpose |
|------|---------|
| `main.js` | All JavaScript logic — follow the TODO comments |

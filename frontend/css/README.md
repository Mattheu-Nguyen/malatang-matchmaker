# frontend/css/ — Styling

All CSS for the site lives in `style.css`. Both `index.html` and `results.html` link to it.

---

## Style Guide Suggestions

### Color Theme
Malatang is bold and spicy — lean into warm reds, oranges, and deep browns.

| Use | Suggested Color |
|-----|----------------|
| Primary / buttons | `#d94f2b` (spicy red-orange) |
| Accent | `#f5a623` (warm yellow) |
| Background | `#fff8f0` (warm off-white) |
| Text | `#2c2c2c` (near-black) |
| Cards | `#ffffff` with a soft box-shadow |

Use CSS custom properties (`--color-primary`, etc.) defined in `:root` so you can
change the whole palette in one place.

### Fonts
Recommended free Google Fonts:
- **Poppins** — clean, modern, great for headings
- **Noto Sans** — supports Chinese characters if you want to add any

Add in `<head>` of your HTML:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">
```

### Layout Tips
- Use `max-width: 700px; margin: 0 auto;` on the main container so it doesn't stretch on wide screens
- Use `display: flex; flex-wrap: wrap; gap: 10px;` for the checkbox groups
- Use CSS Grid for the results cards on desktop (2 columns), single column on mobile

---

## Files

| File | Purpose |
|------|---------|
| `style.css` | All styles — follow the section TODO comments |

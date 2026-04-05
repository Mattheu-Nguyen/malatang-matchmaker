import sqlite3
import os

# -----------------------------------------------------------------------------
# DB path — mirrors the same logic as backend/database/db.py
# -----------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'malatang.db')


# -----------------------------------------------------------------------------
# Preference keyword mappings
# -----------------------------------------------------------------------------
SPICE_KEYWORDS = {
    "mild":        ["mild", "not spicy", "light", "no spice", "no spicy", "non spicy", "zero spice", "gentle", "barely spicy", "kid friendly", "low heat", "little spice"],
    "medium":      ["medium spice", "moderate", "medium hot", "balanced spice", "some spice", "bit spicy", "mid spice", "medium heat"],
    "spicy":       ["spicy", "hot", "mala", "spice", "spicy broth", "chili", "chilli", "peppery", "kick", "heat", "szechuan spice", "sichuan spice", "chili oil", "chili broth"],
    "extra spicy": ["very spicy", "extra hot", "numbing", "extra spicy", "super spicy", "insanely spicy", "burning", "mouth burning", "tongue numbing", "ma la", "extreme heat", "nuclear"],
}

BROTH_KEYWORDS = {
    "spicy mala":  ["mala", "spicy broth", "red broth", "sichuan broth", "szechuan broth", "chili broth", "chili oil broth", "mala soup", "mala tang", "peppercorn broth", "ma la broth", "spicy base"],
    "clear":       ["clear broth", "light broth", "plain broth"],
    "tomato":      ["tomato"],
    "mushroom":    ["mushroom broth", "mushroom soup", "vegetarian broth", "vegan broth"],
}

MEAT_KEYWORDS = {
    "beef":   ["beef", "wagyu", "tongue","ribeye", "brisket", "shank", "oxtail"],
    "pork":   ["pork", "bacon"],
    "lamb":   ["lamb", "mutton"],
    "chicken":["chicken"],
    "seafood":["seafood", "shrimp", "fish", "fish cake", "fishcake", "prawn", "squid", "octopus", "scallop", "clam", "mussel", "crab", "surimi"],
}

INGREDIENT_KEYWORDS = {
    "tofu":       ["tofu", "bean curd"],
    "fish cake":  ["fish cake", "fishcake", "fish ball", "fishball", "fish tofu", "seafood ball"],
    "mushroom":   ["mushroom", "enoki","shiitake", "king oyster", "oyster mushroom", "wood ear", "black fungus"],
    "noodles":    ["noodles", "noodle", "vermicelli", "udon", "ramen"],
    "veggies":    ["veggies", "vegetables", "veggie","bok choy", "napa cabbage", "cabbage", "spinach", "lettuce", "lotus root", "corn", "seaweed"]
}

SIDE_DISH_KEYWORDS = {
    "rice":         ["rice", "steamed rice", "white rice", "fried rice"],
    "fried dough":  ["fried dough", "youtiao", "you tiao", "dough fritter", "chinese donut", "chinese doughnut"],
    "sesame noodles": ["sesame noodles", "sesame noodle", "cold noodles", "sesame sauce noodles", "ma jiang noodles", "mee sesame"],
}


def _search(text: str, keywords: list[str]) -> int:
    """Return the number of keyword matches found in text (case-insensitive)."""
    if not text:
        return 0
    text_lower = text.lower()
    return sum(1 for kw in keywords if kw.lower() in text_lower)


def score_restaurant(restaurant: dict, preferences: dict) -> float:
    """Score a single restaurant against the user's preferences."""
    score = 0.0

    # Combine categories + review text into one searchable string
    searchable = " ".join(filter(None, [
        restaurant.get("categories", "") or "",
        restaurant.get("review_text", "") or "",
        restaurant.get("name", "") or "",
    ]))

    # Spice level match (+10 per keyword hit) — accepts a string or list of strings
    spice_pref = preferences.get("spice_level", [])
    if isinstance(spice_pref, str):
        spice_pref = [spice_pref]
    for spice in spice_pref:
        if spice in SPICE_KEYWORDS:
            score += _search(searchable, SPICE_KEYWORDS[spice]) * 10

    # Broth match (+10 per keyword hit) — accepts a string or list of strings
    broth_pref = preferences.get("broth", [])
    if isinstance(broth_pref, str):
        broth_pref = [broth_pref]
    for broth in broth_pref:
        if broth in BROTH_KEYWORDS:
            score += _search(searchable, BROTH_KEYWORDS[broth]) * 10

    # Meat preferences (+8 per keyword hit per meat)
    for meat in preferences.get("meats", []):
        meat_lower = meat.lower()
        keywords = MEAT_KEYWORDS.get(meat_lower, [meat_lower])
        score += _search(searchable, keywords) * 8

    # Ingredient preferences (+5 per keyword hit per ingredient)
    for ingredient in preferences.get("ingredients", []):
        ing_lower = ingredient.lower()
        keywords = INGREDIENT_KEYWORDS.get(ing_lower, [ing_lower])
        score += _search(searchable, keywords) * 5

    # Side dish preferences (+5 per keyword hit per side dish)
    for side in preferences.get("side_dishes", []):
        side_lower = side.lower()
        keywords = SIDE_DISH_KEYWORDS.get(side_lower, [side_lower])
        score += _search(searchable, keywords) * 5

    # Star rating bonus to break ties (max +10)
    try:
        score += float(restaurant.get("stars") or 0) * 2
    except (TypeError, ValueError):
        pass

    return score


def get_recommendations(preferences: dict, top_n: int = 10) -> list[dict]:
    """
    Score every restaurant in the DB against `preferences` and return
    the top_n matches sorted by match_score descending.

    Expected preference keys:
        spice_level  : str  — "mild" | "medium" | "high" | "extra spicy"
        broth        : str  — "spicy mala" | "clear" | "tomato" | "mushroom"
        meats        : list[str]
        ingredients  : list[str]
        side_dishes  : list[str]  — "rice" | "fried dough" | "sesame noodles"
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        cursor = conn.cursor()

        # Fetch all restaurants
        cursor.execute("SELECT * FROM restaurants")
        restaurants = cursor.fetchall()

        # Try to fetch aggregated review text per business (best-effort)
        review_map: dict[str, str] = {}
        try:
            cursor.execute(
                "SELECT business_id, GROUP_CONCAT(text, ' ') AS review_text "
                "FROM reviews GROUP BY business_id"
            )
            for row in cursor.fetchall():
                review_map[row["business_id"]] = row["review_text"] or ""
        except sqlite3.OperationalError:
            pass  # reviews table doesn't exist yet — that's fine

        results = []
        for row in restaurants:
            restaurant = dict(row)
            restaurant["review_text"] = review_map.get(
                restaurant.get("business_id", ""), ""
            )
            match_score = score_restaurant(restaurant, preferences)
            results.append({
                "business_id":  restaurant.get("business_id"),
                "name":         restaurant.get("name"),
                "address":      restaurant.get("address"),
                "city":         restaurant.get("city"),
                "state":        restaurant.get("state"),
                "stars":        restaurant.get("stars"),
                "review_count": restaurant.get("review_count"),
                "categories":   restaurant.get("categories"),
                "match_score":  match_score,
            })

        results.sort(key=lambda x: x["match_score"], reverse=True)
        return results[:top_n]

    finally:
        conn.close()


# -----------------------------------------------------------------------------
# Local test — run:  py -3 recommendation/engine.py
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    test_preferences = {
        "spice_level": "high",
        "broth":       "spicy mala",
        "meats":       ["beef", "pork"],
        "ingredients": ["fish cake", "tofu"],
        "side_dishes": ["rice"],
    }

    print(f"DB path: {DB_PATH}")
    print(f"DB exists: {os.path.exists(DB_PATH)}\n")

    recommendations = get_recommendations(test_preferences, top_n=5)
    if not recommendations:
        print("No results — is the DB populated? Run data/process_data.py first.")
    else:
        print(f"Top {len(recommendations)} recommendations:\n")
        for i, r in enumerate(recommendations, 1):
            print(
                f"  {i}. {r['name']} ({r['city']}, {r['state']}) "
                f"— {r['stars']} stars — score: {r['match_score']:.1f}"
            )

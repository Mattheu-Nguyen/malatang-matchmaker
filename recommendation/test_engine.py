import sys
import os
import sqlite3
import tempfile
import engine

# Make sure the project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import recommendation.engine as engine

# =============================================================================
# Test helpers — build an in-memory DB with fake restaurants
# =============================================================================

FAKE_RESTAURANTS = [
    {
        "business_id": "r1",
        "name": "Mala King",
        "address": "1 Spice St",
        "city": "Houston",
        "state": "TX",
        "stars": 4.5,
        "review_count": 200,
        "categories": "Hot Pot, Malatang, Chinese",
        "review_text": "very spicy mala broth, great beef and tofu options",
    },
    {
        "business_id": "r2",
        "name": "Gentle Pot",
        "address": "2 Mild Ave",
        "city": "Houston",
        "state": "TX",
        "stars": 4.0,
        "review_count": 80,
        "categories": "Hot Pot, Chinese",
        "review_text": "mild broth, light and not spicy, clear broth, good chicken",
    },
    {
        "business_id": "r3",
        "name": "Tomato Garden",
        "address": "3 Tomato Blvd",
        "city": "Austin",
        "state": "TX",
        "stars": 3.8,
        "review_count": 50,
        "categories": "Hot Pot, Chinese",
        "review_text": "tomato broth base, fresh vegetables and egg noodles",
    },
    {
        "business_id": "r4",
        "name": "Seafood Mala",
        "address": "4 Ocean Rd",
        "city": "Dallas",
        "state": "TX",
        "stars": 4.2,
        "review_count": 120,
        "categories": "Hot Pot, Seafood, Chinese",
        "review_text": "spicy mala broth with fresh shrimp, fish cake, and mushroom",
    },
    {
        "business_id": "r5",
        "name": "Plain & Simple",
        "address": "5 Basic Ln",
        "city": "Austin",
        "state": "TX",
        "stars": 3.2,
        "review_count": 20,
        "categories": "Chinese",
        "review_text": "plain broth, nothing special",
    },
]


def _make_temp_db():
    """Create a temporary SQLite DB with fake data and patch engine.DB_PATH."""
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()

    conn = sqlite3.connect(tmp.name)
    conn.execute("""
        CREATE TABLE restaurants (
            business_id TEXT, name TEXT, address TEXT, city TEXT, state TEXT,
            stars REAL, review_count INTEGER, categories TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE reviews (
            business_id TEXT, text TEXT
        )
    """)
    for r in FAKE_RESTAURANTS:
        conn.execute(
            "INSERT INTO restaurants VALUES (?,?,?,?,?,?,?,?)",
            (r["business_id"], r["name"], r["address"], r["city"],
             r["state"], r["stars"], r["review_count"], r["categories"]),
        )
        conn.execute(
            "INSERT INTO reviews VALUES (?,?)",
            (r["business_id"], r["review_text"]),
        )
    conn.commit()
    conn.close()

    engine.DB_PATH = tmp.name
    return tmp.name


# =============================================================================
# Tests
# =============================================================================

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"
_results = []

def check(name, condition, detail=""):
    status = PASS if condition else FAIL
    print(f"  [{status}] {name}" + (f" — {detail}" if detail else ""))
    _results.append(condition)


def test_high_spice_mala_returns_mala_king_first():
    print("\nTest: high spice + spicy mala broth → Mala King should rank first")
    results = engine.get_recommendations({
        "spice_level": "high",
        "broth": "spicy mala",
        "meats": [],
        "ingredients": [],
    })
    check("returns results", len(results) > 0)
    check("Mala King is #1", results[0]["name"] == "Mala King",
          f"got '{results[0]['name']}'")
    check("all results have match_score", all("match_score" in r for r in results))


def test_mild_clear_broth_returns_gentle_pot_first():
    print("\nTest: mild + clear broth → Gentle Pot should rank first")
    results = engine.get_recommendations({
        "spice_level": "mild",
        "broth": "clear",
        "meats": ["chicken"],
        "ingredients": [],
    })
    check("returns results", len(results) > 0)
    check("Gentle Pot is #1", results[0]["name"] == "Gentle Pot",
          f"got '{results[0]['name']}'")


def test_tomato_broth_returns_tomato_garden_first():
    # No spice_level — isolates broth + ingredient so Gentle Pot's spice keywords don't interfere
    print("\nTest: tomato broth + egg ingredient -> Tomato Garden should rank first")
    results = engine.get_recommendations({
        "broth": "tomato",
        "meats": [],
        "ingredients": ["egg"],
    })
    check("returns results", len(results) > 0)
    check("Tomato Garden is #1", results[0]["name"] == "Tomato Garden",
          f"got '{results[0]['name']}'")


def test_seafood_preferences():
    print("\nTest: seafood + mushroom ingredient → Seafood Mala should rank first")
    results = engine.get_recommendations({
        "spice_level": "high",
        "broth": "spicy mala",
        "meats": ["seafood"],
        "ingredients": ["fish cake", "mushroom"],
    })
    check("returns results", len(results) > 0)
    check("Seafood Mala is #1", results[0]["name"] == "Seafood Mala",
          f"got '{results[0]['name']}'")


def test_top_n_limit():
    print("\nTest: top_n=3 returns at most 3 results")
    results = engine.get_recommendations({"spice_level": "high", "broth": "spicy mala"}, top_n=3)
    check("at most 3 results", len(results) <= 3, f"got {len(results)}")


def test_results_sorted_descending():
    print("\nTest: results are sorted by match_score descending")
    results = engine.get_recommendations({
        "spice_level": "high",
        "broth": "spicy mala",
        "meats": ["beef"],
        "ingredients": ["tofu"],
    })
    scores = [r["match_score"] for r in results]
    check("scores are descending", scores == sorted(scores, reverse=True),
          f"scores: {scores}")


def test_empty_preferences_returns_results():
    print("\nTest: empty preferences still returns results (sorted by stars)")
    results = engine.get_recommendations({})
    check("returns results", len(results) > 0)
    check("all have match_score key", all("match_score" in r for r in results))


def test_unknown_preference_values_dont_crash():
    print("\nTest: unknown spice/broth values don't crash")
    try:
        results = engine.get_recommendations({
            "spice_level": "UNKNOWN",
            "broth": "UNKNOWN",
            "meats": ["UNKNOWN_MEAT"],
            "ingredients": ["UNKNOWN_ING"],
        })
        check("no exception raised", True)
        check("returns a list", isinstance(results, list))
    except Exception as e:
        check("no exception raised", False, str(e))


# =============================================================================
# Run all tests
# =============================================================================

if __name__ == "__main__":
    db_path = _make_temp_db()
    try:
        test_high_spice_mala_returns_mala_king_first()
        test_mild_clear_broth_returns_gentle_pot_first()
        test_tomato_broth_returns_tomato_garden_first()
        test_seafood_preferences()
        test_top_n_limit()
        test_results_sorted_descending()
        test_empty_preferences_returns_results()
        test_unknown_preference_values_dont_crash()
    finally:
        os.unlink(db_path)

    passed = sum(_results)
    total = len(_results)
    print(f"\n{'='*40}")
    print(f"Results: {passed}/{total} passed")
    if passed == total:
        print("\033[92mAll tests passed!\033[0m")
    else:
        print(f"\033[91m{total - passed} test(s) failed.\033[0m")
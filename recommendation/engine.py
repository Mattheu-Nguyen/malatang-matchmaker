# =============================================================================
# recommendation/engine.py — Person 3 (Recommendation Engineer)
# =============================================================================
# PURPOSE:
#   Given a user's malatang preferences, score every restaurant in the DB
#   and return a ranked list of the best matches.
#
# MAIN FUNCTION:
#   get_recommendations(preferences) → list of restaurant dicts, sorted by score
#
# CALLED BY:
#   backend/routes/restaurants.py  (Person 2 calls this from the /recommend route)
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# TODO: import sqlite3
# TODO: import os
# TODO: (optional) import re  — useful for text searching in reviews


# -----------------------------------------------------------------------------
# STEP 1: Set up the DB path
# -----------------------------------------------------------------------------
# Same as backend/database/db.py — build a path to data/processed/malatang.db
#
# TODO: Build the absolute path to malatang.db using os.path
# TODO: (Or import get_connection from backend/database/db.py if easier)


# -----------------------------------------------------------------------------
# STEP 2: Define your preference keyword mappings
# -----------------------------------------------------------------------------
# Map user-facing preference values to keywords to search for in reviews/categories.
# This makes your scoring logic flexible and easy to update.
#
# Example structure (you'll customize this):
#
# SPICE_KEYWORDS = {
#     "mild":        ["mild", "not spicy", "light"],
#     "medium":      ["medium spice", "moderate"],
#     "high":        ["spicy", "hot", "mala"],
#     "extra spicy": ["very spicy", "extra hot", "numbing", "口味重"]
# }
#
# BROTH_KEYWORDS = {
#     "spicy mala":  ["mala", "spicy broth", "红汤"],
#     "clear":       ["clear broth", "light broth", "清汤"],
#     "tomato":      ["tomato", "番茄"],
#     "mushroom":    ["mushroom broth", "菌汤"]
# }
#
# TODO: Define keyword mappings for: spice_level, broth, meats, ingredients


# -----------------------------------------------------------------------------
# STEP 3: Write the scoring function for a single restaurant
# -----------------------------------------------------------------------------
# This helper takes one restaurant's data and the user's preferences,
# and returns a numeric score (higher = better match).
#
# TODO: Define score_restaurant(restaurant, preferences)
# TODO: Start with score = 0
#
# TODO: SPICE LEVEL MATCH
#       Get the keywords for preferences['spice_level']
#       Search the restaurant's review text or categories for those keywords
#       Add points for each match (e.g., +10 per keyword found)
#
# TODO: BROTH MATCH
#       Same approach — look up broth keywords, search review text
#       Add points for matches
#
# TODO: MEAT / INGREDIENT MATCH
#       For each meat/ingredient in the user's list,
#       check if it appears in the reviews or menu description
#       Add points per match
#
# TODO: STAR RATING BONUS
#       Add a small bonus based on star rating to break ties
#       e.g., score += restaurant['stars'] * 2
#
# TODO: Return the final score


# -----------------------------------------------------------------------------
# STEP 4: Write the main get_recommendations() function
# -----------------------------------------------------------------------------
# This is the function Person 2 will import and call.
#
# TODO: Define get_recommendations(preferences)
#
# TODO: Connect to the SQLite DB
# TODO: Query all restaurants (you can also JOIN with reviews if available)
#       SELECT * FROM restaurants
#
# TODO: For each restaurant, call score_restaurant(restaurant, preferences)
# TODO: Store each restaurant as a dict with its score added:
#       { 'name': ..., 'address': ..., 'stars': ..., 'match_score': score }
#
# TODO: Sort the list by match_score descending (highest first)
#       results.sort(key=lambda x: x['match_score'], reverse=True)
#
# TODO: (Optional) Only return the top N results, e.g., top 10
# TODO: Return the sorted list
#
# TODO: Close the DB connection


# -----------------------------------------------------------------------------
# STEP 5: Test your function locally
# -----------------------------------------------------------------------------
# Add a quick test at the bottom so you can run this file directly to verify:
#
# if __name__ == '__main__':
#     test_preferences = {
#         "spice_level": "high",
#         "broth": "spicy mala",
#         "meats": ["beef", "pork"],
#         "ingredients": ["fish cake", "tofu"],
#         "side_dishes": ["rice"]
#     }
#     TODO: Call get_recommendations(test_preferences) and print the top 5 results
# =============================================================================

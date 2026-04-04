# =============================================================================
# routes/restaurants.py — Person 2 (Backend Developer)
# =============================================================================
# PURPOSE:
#   Define the two API routes this app needs:
#     GET  /restaurants  → return all restaurants from the DB
#     POST /recommend    → accept user preferences, return ranked results
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# TODO: from flask import Blueprint, request, jsonify
# TODO: from database.db import get_connection
#       (the helper you'll write in database/db.py)
# TODO: import sys, os
#       sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
#       from recommendation.engine import get_recommendations
#       (import Person 3's recommendation function)


# -----------------------------------------------------------------------------
# STEP 1: Create the Blueprint
# -----------------------------------------------------------------------------
# TODO: restaurants_bp = Blueprint('restaurants', __name__)


# -----------------------------------------------------------------------------
# ROUTE 1: GET /restaurants
# -----------------------------------------------------------------------------
# Returns all restaurants in the database as JSON.
# Good for testing that the DB connection and routes are working.
#
# TODO: Define the route with @restaurants_bp.route('/restaurants', methods=['GET'])
# TODO: Open a DB connection using get_connection()
# TODO: Run: SELECT * FROM restaurants
#       (replace 'restaurants' with Person 1's actual table name)
# TODO: Convert the results to a list of dicts
# TODO: Return jsonify(results)
# TODO: Close the DB connection


# -----------------------------------------------------------------------------
# ROUTE 2: POST /recommend
# -----------------------------------------------------------------------------
# Accepts user preferences as JSON in the request body.
# Passes them to the recommendation engine.
# Returns a ranked list of restaurants.
#
# TODO: Define the route with @restaurants_bp.route('/recommend', methods=['POST'])
# TODO: Read the request body: preferences = request.get_json()
# TODO: Validate that preferences is not None (return 400 error if missing)
# TODO: Call: results = get_recommendations(preferences)
#             (Person 3's function — agree on input/output format with them!)
# TODO: Return jsonify(results)
#
# ERROR HANDLING:
# TODO: Wrap in a try/except block
# TODO: If anything goes wrong, return a JSON error message with status 500
# =============================================================================

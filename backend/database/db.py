# =============================================================================
# database/db.py — Person 2 (Backend Developer)
# =============================================================================
# PURPOSE:
#   Provide a single function that opens and returns a connection to the
#   SQLite database. All routes import and use this function.
#
# USAGE:
#   from database.db import get_connection
#   conn = get_connection()
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
# TODO: import sqlite3
# TODO: import os


# -----------------------------------------------------------------------------
# STEP 1: Set the database path
# -----------------------------------------------------------------------------
# The DB lives at data/processed/malatang.db relative to the project root.
# Use os.path to build an absolute path so it works regardless of where
# the script is run from.
#
# TODO: Build the path to malatang.db using os.path.abspath and __file__
#       Something like:
#       BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
#       DB_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'malatang.db')


# -----------------------------------------------------------------------------
# STEP 2: Write the get_connection() function
# -----------------------------------------------------------------------------
# TODO: Define get_connection()
# TODO: Open a sqlite3 connection to DB_PATH
# TODO: Set conn.row_factory = sqlite3.Row
#       (this makes rows behave like dicts, so you can access columns by name)
# TODO: Return the connection
#
# Example:
#   def get_connection():
#       conn = sqlite3.connect(DB_PATH)
#       conn.row_factory = sqlite3.Row
#       return conn
# =============================================================================

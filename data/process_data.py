# =============================================================================
# process_data.py — Person 1 (Data Engineer)
# =============================================================================
# PURPOSE:
#   Load the raw Yelp JSON dataset, filter it to malatang/hot pot restaurants,
#   clean and organize the data, then save it as a SQLite database.
#
# HOW TO RUN:
#   python data/process_data.py
#
# OUTPUT:
#   data/processed/malatang.db
# =============================================================================


# -----------------------------------------------------------------------------
# IMPORTS — you will need these libraries
# -----------------------------------------------------------------------------
# TODO: import pandas as pd
# TODO: import sqlite3
# TODO: import os  (to build file paths)
# TODO: import json  (if reading line-by-line JSON)

import pandas as pd 
import sqlite3 
import os 
import json


# -----------------------------------------------------------------------------
# STEP 1: Define file paths
# -----------------------------------------------------------------------------
# TODO: Set the path to the raw Yelp JSON file in data/raw/
# TODO: Set the output path for the SQLite DB in data/processed/

directory = os.path.dirname(os.path.abspath(__file__))
bus_set = os.path.join(directory, "raw", "yelp_academic_dataset_business.json")
rev_set = os.path.join(directory, "raw", "yelp_academic_dataset_review.json")
output_db = os.path.join(directory, "processed", "malatang.db")



# -----------------------------------------------------------------------------
# STEP 2: Load the Yelp business data
# -----------------------------------------------------------------------------
# NOTE: The Yelp dataset is sometimes "line-delimited JSON" (one JSON object
#       per line), not a single JSON array. Try pd.read_json() with lines=True.
#
# TODO: Load the Yelp business JSON file into a pandas DataFrame
# TODO: Print df.columns and df.head() to see what fields exist
# TODO: Print df.shape to see how many restaurants are in the full dataset

df = pd.read_json(bus_set, lines= True)
print(df.columns.tolist()) #columns
print(df.head(10))
print(df.shape)





# -----------------------------------------------------------------------------
# STEP 3: Filter for malatang / hot pot restaurants
# -----------------------------------------------------------------------------
# The "categories" column is a string like "Chinese, Hot Pot, Restaurants"
# Use .str.contains() to filter rows that match any of these keywords:
#   - "Malatang", "Hot Pot", "Hotpot", "Mala", "Szechuan", "Chinese"
#
# TODO: Filter the DataFrame to only keep malatang-relevant restaurants
# TODO: Print how many restaurants remain after filtering
# TODO: If the result is too small, loosen the keywords (e.g., just "Chinese")

mala_df = df[df["categories"].str.contains('Hot Pot| Hotpot| Sichuan| Malatang', case = False, na = False)]
print(f"Found {len(mala_df)} malatang/hotpot Restaruants! ")



# -----------------------------------------------------------------------------
# STEP 4: Keep only the columns you need
# -----------------------------------------------------------------------------
# Only keep columns that are useful. Suggested columns:
#   business_id, name, address, city, state, stars, review_count, categories
#
# NOTE: Check if these exact column names exist — the Yelp dataset may use
#       slightly different names. Adjust as needed.
#
# TODO: Select only the relevant columns
# TODO: Rename columns if needed to be simpler (e.g., 'stars' → 'avg_rating')
# TODO: Drop any rows where the name or business_id is missing


mala_df = mala_df[['business_id', 'name', 'stars', 'review_count']]
mala_df = mala_df.rename(columns={ 'stars': 'avg_rating', 
'review_count': 'num_reviews'}
)

mala_df = mala_df.dropna(subset=['name', 'business_id'])

print(f"Restaurants after cleaning: {len(mala_df)}")
print(mala_df.head())


# -----------------------------------------------------------------------------
# STEP 5: (Optional but helpful) Load and join review data
# -----------------------------------------------------------------------------
# The Yelp dataset has a separate reviews file. Reviews contain text like
# "great spicy broth" or "mild options available" — useful for recommendations.
#
# TODO: Load the reviews JSON file (if available)
# TODO: Filter reviews to only include reviews for the restaurants you kept
# TODO: Consider grouping all reviews per restaurant into one combined text
#       OR keep individual reviews in a separate 'reviews' table
#
# TALK TO PERSON 3 about what format works best for the recommendation engine!




# -----------------------------------------------------------------------------
# STEP 6: Save to SQLite
# -----------------------------------------------------------------------------
# Use pandas df.to_sql() to write the DataFrame into a SQLite database.
# The database file will be created automatically if it doesn't exist.
#
# TODO: Create a sqlite3 connection to data/processed/malatang.db
# TODO: Write the restaurants DataFrame to a table called 'restaurants'
#       Use: df.to_sql('restaurants', conn, if_exists='replace', index=False)
# TODO: (If you have reviews) Write reviews to a 'reviews' table too
# TODO: Close the connection when done
#
# SHARE YOUR TABLE/COLUMN NAMES WITH PERSON 2 so they can write queries!

print("Saving to database...")
conn = sqlite3.connect(output_db)

mala_df.to_sql('restaurants', conn, if_exists='replace', index=False)
# rev_df.to_sql('reviews', conn, if_exists='replace', index=False)

conn.close()
print(f"Saved to {output_db}")


# -----------------------------------------------------------------------------
# STEP 7: Verify the output
# -----------------------------------------------------------------------------
# Run a test query to confirm the DB was created correctly.
#
# TODO: Re-open the SQLite DB
# TODO: Run: SELECT * FROM restaurants LIMIT 5
# TODO: Print the results
# TODO: Run: SELECT COUNT(*) FROM restaurants
# TODO: Print the total count so you know how many restaurants are in the DB

conn = sqlite3.connect(output_db)

print("\n--- RESTAURANTS TABLE ---")
result = pd.read_sql("SELECT * FROM restaurants LIMIT 5", conn)
print(result)

print("\n--- TOTAL RESTAURANTS ---")
count = pd.read_sql("SELECT COUNT(*) FROM restaurants", conn)
print(count)

conn.close()
print("\nDONE! Share malatang.db with your teammates")


# -----------------------------------------------------------------------------
# DONE!
# Let the team know:
#   - The DB is ready at data/processed/malatang.db
#   - Share the table names and column names in the group chat
#   - Person 2 and Person 3 can now start using real data
# -----------------------------------------------------------------------------

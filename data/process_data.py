import pandas as pd 
import sqlite3 
import os 
import json
import duckdb


# -----------------------------------------------------------------------------
# STEP 1: Define file paths
# -----------------------------------------------------------------------------

directory = os.path.dirname(os.path.abspath(__file__))
bus_set = os.path.join(directory, "raw", "yelp_academic_dataset_business.json")
rev_set = os.path.join(directory, "raw", "yelp_academic_dataset_review.json")
output_db = os.path.join(directory, "processed", "malatang.db")



# -----------------------------------------------------------------------------
# STEP 2: Load the Yelp business data
# -----------------------------------------------------------------------------

df = pd.read_json(bus_set, lines= True)
print(df.columns.tolist()) #columns
print(df.head(10))
print(df.shape)



# -----------------------------------------------------------------------------
# STEP 3: Filter for malatang / hot pot restaurants
# -----------------------------------------------------------------------------

mala_df = df[df["categories"].str.contains('Hot Pot|Hotpot|Sichuan|Malatang', case = False, na = False)]
mala_df = mala_df[mala_df["business_id"] != "iksVwRfpWymIUUFqw0tXpw"]
print(f"Found {len(mala_df)} malatang/hotpot Restaruants! ")



# -----------------------------------------------------------------------------
# STEP 4: Keep only the columns you need
# -----------------------------------------------------------------------------

mala_df = mala_df[['business_id', 'name', 'stars', 'review_count']]
mala_df = mala_df.rename(columns={ 'stars': 'avg_rating', 
'review_count': 'num_reviews'}
)

mala_df = mala_df.dropna(subset=['name', 'business_id'])

print(f"Restaurants after cleaning: {len(mala_df)}")
print(mala_df.head())
print('\n')


# -----------------------------------------------------------------------------
# STEP 5: (Optional but helpful) Load and join review data
# -----------------------------------------------------------------------------


connect = duckdb.connect()
connect.register("restaurant", mala_df)
# bus_id = mala_df["business_id"].tolist()
review_df = connect.execute(f"""SELECT review_id, business_id, stars, text FROM read_json_auto('{rev_set}') WHERE business_id IN (SELECT business_id FROM restaurant)""").df()

print(f"Found {len(review_df)} reviews!")


# -----------------------------------------------------------------------------
# STEP 6: Save to SQLite
# -----------------------------------------------------------------------------


print("Saving to database...")
conn = sqlite3.connect(output_db)

mala_df.to_sql('restaurants', conn, if_exists='replace', index=False)
review_df.to_sql('reviews', conn, if_exists='replace', index=False)

conn.close()
print(f"Saved to {output_db}")


# -----------------------------------------------------------------------------
# STEP 7: Verify the output
# -----------------------------------------------------------------------------

conn = sqlite3.connect(output_db)

print("\n--- RESTAURANTS TABLE ---")
result = pd.read_sql("SELECT * FROM restaurants LIMIT 5", conn)
print(result)

print("\n--- TOTAL RESTAURANTS ---")
count = pd.read_sql("SELECT COUNT(*) FROM restaurants", conn)
print(count)

print("\n--- REVIEWS TABLE ---")
rev_result = pd.read_sql("SELECT * FROM reviews LIMIT 5", conn)
print(rev_result)

print("\n--- TOTAL REVIEWS ---")
rev_count = pd.read_sql("SELECT COUNT(*) FROM reviews", conn)
print(rev_count)

conn.close()

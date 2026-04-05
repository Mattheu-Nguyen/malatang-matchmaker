import duckdb
import pandas as pd

df = pd.read_json('/Users/alvinsky/Documents/Data@UCI WS/datathon-malatang/data/raw/yelp_academic_dataset_business.json', lines=True)
print("columns:")
print(df.columns.tolist())

print("print5:")
print(df.head())

print("#restaruants")
print(df.shape)

print("\nMISSING VALUES:")
print(df.isnull().sum())

df2 = pd.read_json('/Users/alvinsky/Documents/Data@UCI WS/datathon-malatang/data/raw/yelp_academic_dataset_review.json', lines=True, nrows =5)
print("columns:")
print(df2.columns.tolist())

print("print5:")
print(df2.head())




# connect = duckdb.connect()

# result = connect.execute("""SELECT * FROM read_json_auto("/Users/alvinsky/Documents/Data@UCI WS/datathon-malatang/data/raw/yelp_academic_dataset_business.json") LIMIT 5 """).df()

# print(result) 
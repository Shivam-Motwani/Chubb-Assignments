
import pandas as pd

#1 Create a pandas DataFrame from the CSV and from Python lists/dicts.
df = pd.read_csv("sample.csv")
print(df.head())

df["date"] = pd.to_datetime(df["date"])  #date to datetime

df["promo_code"].fillna("NO_PROMO", inplace=True) #missiing values
df["customer_id"].fillna(-1, inplace=True)

#2 Filter and subset rows/columns (e.g., sales for a store, date ranges, high-value transactions).
#Sales only from Downtown store
downtown_sales = df[df["store_name"] == "Downtown"]
print(downtown_sales)
#Transactions after October 3rd
after_3 = df[df["date"] > "2025-10-03"]
print(after_3)
#High-value transactions ( > Rs.5)
high_value = df[df["total"] > 5]
print(high_value)

import pandas as pd

#1 Create a pandas DataFrame from the CSV and from Python lists/dicts.
df = pd.read_csv("sample.csv")
print(df.head())

df["date"] = pd.to_datetime(df["date"])  #date to datetime

df["promo_code"].fillna("NO_PROMO", inplace=True) #missiing values
df["customer_id"].fillna(-1, inplace=True)

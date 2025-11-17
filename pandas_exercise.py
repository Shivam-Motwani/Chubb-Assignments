
import pandas as pd

#1 Create a pandas DataFrame from the CSV and from Python lists/dicts.
df = pd.read_csv("sample.csv")
print("\nDataFrame head\n", df.head())

df["date"] = pd.to_datetime(df["date"])  #date to datetime

df["promo_code"].fillna("NO_PROMO", inplace=True) #missiing values
df["customer_id"].fillna(-1, inplace=True)

#2 Filter and subset rows/columns (e.g., sales for a store, date ranges, high-value transactions).
#Sales only from Downtown store
downtown_sales = df[df["store_name"] == "Downtown"]
print("\nSales only from Downtown store\n", downtown_sales)
#Transactions after October 3rd
after_3 = df[df["date"] > "2025-10-03"]
print("\nTransactions after October 3rd\n", after_3)
#High-value transactions ( > Rs.5)
high_value = df[df["total"] > 5]
print("\nHigh-value transactions ( > Rs.5)\n", high_value)

#3 Compute descriptive statistics and group summaries (totals by store, average basket).
#Total sales by store
sales_by_store = df.groupby("store_name")["total"].sum()
print("\nSales by store\n",sales_by_store)
#Total quantity sold by product
qty_by_product = df.groupby("product_name")["quantity"].sum()
print("\nTotal quantity sold by product\n",qty_by_product)
#Average transaction amount
avg_transaction = df["total"].mean()
print("\nAverage transaction amount\n",avg_transaction)
#Daily sales
daily_sales = df.groupby("date")["total"].sum()
print("\nDaily sales\n",daily_sales)

#4 Perform simple cleaning (handle missing values, fix data types, drop duplicates).
df["promo_code"].fillna("NO_PROMO", inplace=True) #missiing values
df["customer_id"].fillna(-1, inplace=True)

#Ensure correct numeric types
df["quantity"] = df["quantity"].astype(int)
df["unit_price"] = df["unit_price"].astype(float)
df["total"] = df["total"].astype(float)

#Drop duplicates
df.drop_duplicates(inplace=True)

#5 Build a mini ETL pipeline: read CSV → clean & transform → output JSON.
def sales_etl(df):
    # Clean
    df["date"] = pd.to_datetime(df["date"])
    df["promo_code"].fillna("NO_PROMO", inplace=True)
    df["customer_id"].fillna(-1, inplace=True)
    df.drop_duplicates(inplace=True)

    # Transform
    df["is_weekend"] = df["date"].dt.weekday >= 5

    # Summaries
    store_summary = df.groupby("store_name")["total"].sum().reset_index()
    daily_summary = df.groupby("date")["total"].sum().reset_index()

    # Output JSON
    store_summary.to_json("store_sales.json", orient="records", indent=4)
    daily_summary.to_json("daily_sales.json", orient="records", indent=4)

    return store_summary, daily_summary

store_summary, daily_summary = sales_etl(df)

print("\nStore Summary\n",store_summary)
print("\nDaily Summary\n",daily_summary)


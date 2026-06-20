import pandas as pd
import sqlite3

# CSV Load
df = pd.read_csv("data/reconciliation_results.csv")

# Database Connect
conn = sqlite3.connect("database/reconciliation.db")

# Table Create + Insert
df.to_sql("reconciliation_results", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Data Stored Successfully")

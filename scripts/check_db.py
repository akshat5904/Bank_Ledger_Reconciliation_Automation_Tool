import sqlite3
import pandas as pd

conn = sqlite3.connect("database/reconciliation.db")

query = """
SELECT Status, COUNT(*) as Total
FROM reconciliation_results
GROUP BY Status
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()

import pandas as pd

bank_df = pd.read_csv("data/bank_statement.csv")
ledger_df = pd.read_csv("data/company_ledger.csv")

# Duplicate Detection
duplicates = ledger_df[ledger_df.duplicated(subset=["Transaction_ID"], keep=False)]

print("Duplicate Entries:", len(duplicates))

# Merge
merged = pd.merge(
    bank_df,
    ledger_df,
    on="Transaction_ID",
    how="outer",
    suffixes=("_bank", "_ledger"),
    indicator=True,
)

# Missing in Ledger
missing_in_ledger = merged[merged["_merge"] == "left_only"]

# Missing in Bank
missing_in_bank = merged[merged["_merge"] == "right_only"]

# Common Transactions
common = merged[merged["_merge"] == "both"]

# Amount Mismatch
amount_mismatch = common[common["Amount_bank"] != common["Amount_ledger"]]

# Matched
matched = common[common["Amount_bank"] == common["Amount_ledger"]]

print("Matched:", len(matched))
print("Amount Mismatch:", len(amount_mismatch))
print("Missing in Ledger:", len(missing_in_ledger))
print("Missing in Bank:", len(missing_in_bank))

import pandas as pd

bank_df = pd.read_csv("data/bank_statement.csv")
ledger_df = pd.read_csv("data/company_ledger.csv")

results = []

# Duplicate Detection
duplicates = ledger_df[ledger_df.duplicated(subset=["Transaction_ID"], keep=False)]

for txn in duplicates["Transaction_ID"].unique():
    results.append([txn, "Duplicate Entry"])

# Merge
merged = pd.merge(
    bank_df,
    ledger_df,
    on="Transaction_ID",
    how="outer",
    suffixes=("_bank", "_ledger"),
    indicator=True,
)

for _, row in merged.iterrows():

    txn = row["Transaction_ID"]

    if row["_merge"] == "left_only":
        results.append([txn, "Missing in Ledger"])

    elif row["_merge"] == "right_only":
        results.append([txn, "Missing in Bank"])

    else:

        if row["Amount_bank"] != row["Amount_ledger"]:
            results.append([txn, "Amount Mismatch"])

        else:
            results.append([txn, "Matched"])

result_df = pd.DataFrame(results, columns=["Transaction_ID", "Status"])

result_df.to_csv("data/reconciliation_results.csv", index=False)

print("Results Saved")

import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(
    page_title="Bank & Ledger Reconciliation Dashboard", page_icon="🏦", layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
conn = sqlite3.connect("database/reconciliation.db")

df = pd.read_sql("SELECT * FROM reconciliation_results", conn)

conn.close()

# -----------------------------
# Header
# -----------------------------
st.title("Bank & Ledger Reconciliation Dashboard")
st.markdown("---")

# -----------------------------
# Metrics
# -----------------------------
total = len(df)

matched = len(df[df["Status"] == "Matched"])

mismatch = len(df[df["Status"] == "Amount Mismatch"])

missing_ledger = len(df[df["Status"] == "Missing in Ledger"])

missing_bank = len(df[df["Status"] == "Missing in Bank"])

duplicate = len(df[df["Status"] == "Duplicate Entry"])

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Total", total)
col2.metric("Matched", matched)
col3.metric("Mismatch", mismatch)
col4.metric("Missing Ledger", missing_ledger)
col5.metric("Missing Bank", missing_bank)
col6.metric("Duplicate", duplicate)

st.markdown("---")

# -----------------------------
# Status Distribution Chart
# -----------------------------
status_counts = df["Status"].value_counts().reset_index()

status_counts.columns = ["Status", "Count"]

fig = px.bar(
    status_counts,
    x="Status",
    y="Count",
    title="Transaction Status Distribution",
    text="Count",
)

fig.update_layout(xaxis_title="Status", yaxis_title="Count")

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -----------------------------
# Filter Section
# -----------------------------
st.subheader("Filter Transactions")

status_filter = st.selectbox("Select Status", ["All"] + list(df["Status"].unique()))

if status_filter == "All":
    filtered_df = df
else:
    filtered_df = df[df["Status"] == status_filter]

# -----------------------------
# Download Button
# -----------------------------
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Results",
    data=csv,
    file_name="reconciliation_results.csv",
    mime="text/csv",
)

st.markdown("---")

# -----------------------------
# AI Summary
# -----------------------------
st.subheader("Reconciliation Summary")

summary = f"""
Out of {total} reconciled transactions:

{matched} transactions matched successfully.

{mismatch} transactions showed amount mismatches.

{missing_ledger} transactions were present in the bank statement but missing from the company ledger.

{missing_bank} transactions were present in the company ledger but missing from the bank statement.

{duplicate} duplicate transactions were detected and should be reviewed.
"""


st.info(summary)


st.markdown("---")

# -----------------------------
# Detailed Results
# -----------------------------
st.subheader("Detailed Reconciliation Results")

st.dataframe(filtered_df, use_container_width=True, height=500)

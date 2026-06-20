# Bank & Ledger Reconciliation Automation Tool

## Overview

The Bank & Ledger Reconciliation Automation Tool is an end-to-end data reconciliation system developed using Python, SQLite, and Streamlit. The project automates the process of comparing bank statement transactions with company ledger records to identify discrepancies, improve financial accuracy, and reduce manual reconciliation effort.

The system detects transaction mismatches, missing records, and duplicate entries while providing an interactive dashboard for monitoring reconciliation results.

---

## Features

* Automated transaction reconciliation between Bank Statements and Company Ledger records
* Amount mismatch detection
* Missing transaction identification
* Duplicate transaction detection
* SQLite database integration for storing reconciliation results
* Interactive Streamlit dashboard
* Transaction status filtering
* Download reconciliation results as CSV
* Visual analytics and reconciliation reporting

---

## Tech Stack

* Python
* Pandas
* SQLite
* Streamlit
* Plotly
* Git & GitHub

---

## Dashboard Preview

<img width="1783" height="795" alt="Screenshot 2026-06-20 180959" src="https://github.com/user-attachments/assets/02ae0ae0-1a7e-4be5-8676-041973bdb656" />

<img width="1780" height="746" alt="Screenshot 2026-06-20 181010" src="https://github.com/user-attachments/assets/4656d38b-1d4d-436b-9f0e-7367267a73c0" />

<img width="1805" height="777" alt="Screenshot 2026-06-20 181021" src="https://github.com/user-attachments/assets/5eced832-ce76-421d-951b-745b7a566665" />

<img width="1806" height="771" alt="Screenshot 2026-06-20 181030" src="https://github.com/user-attachments/assets/36c520bc-57ea-4b83-8937-9953ee6be969" />


---

## Project Workflow

1. Generate Bank Statement dataset
2. Generate Company Ledger dataset
3. Perform transaction reconciliation
4. Detect discrepancies
5. Store results in SQLite database
6. Visualize results through Streamlit dashboard

---

## Project Structure

```text
Bank_Ledger_Reconciliation_Automation_Tool
│
├── data
│   ├── bank_statement.csv
│   ├── company_ledger.csv
│   └── reconciliation_results.csv
│
├── database
│
├── scripts
│   ├── generate_data.py
│   ├── create_ledger.py
│   ├── reconcile.py
│   ├── save_results.py
│   ├── store_to_db.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Reconciliation Logic

The system categorizes transactions into the following groups:

* Matched Transactions
* Amount Mismatch
* Missing in Ledger
* Missing in Bank
* Duplicate Entries

---

## Dashboard Features

* Total Transactions KPI
* Matched Transactions KPI
* Amount Mismatch KPI
* Missing Ledger KPI
* Missing Bank KPI
* Duplicate Transaction KPI
* Status Distribution Chart
* Transaction Filtering
* CSV Export

---


## Sample Output

The system reconciles more than 5,000 transactions and automatically identifies:

* Amount mismatches
* Missing records
* Duplicate entries
* Successfully matched transactions

---

## Future Enhancements

* MySQL/PostgreSQL Integration
* Automated Email Reporting
* Multi-Bank Support
* LLM-Based Reconciliation Insights
* Cloud Deployment

---

## Author

Akshat Joshi

B.Tech Computer Science Engineering

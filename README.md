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

## How to Run

### Clone Repository

```bash
git clone <repository-url>
cd Bank_Ledger_Reconciliation_Automation_Tool
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Generate Sample Data

```bash
python scripts/generate_data.py
python scripts/create_ledger.py
```

### Run Reconciliation

```bash
python scripts/reconcile.py
python scripts/save_results.py
python scripts/store_to_db.py
```

### Launch Dashboard

```bash
streamlit run app.py
```

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

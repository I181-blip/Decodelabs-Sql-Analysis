# SQL Data Analysis — DecodeLabs/HexSoftwares Internship (Project 3)

## Overview
This project uses SQL queries to extract insights from a sales/orders dataset, covering filtering, sorting, grouping, and aggregation (SELECT, WHERE, ORDER BY, GROUP BY, COUNT, SUM, AVG).

## Tools Used
- Python (`sqlite3`)
- SQLite database (`database.db`)
- VS Code

## Files
- `db.py` — connects to and sets up the database
- `queries.py` — contains the SQL queries used for analysis
- `database.db` — the SQLite database file
- `Project3_Output` — output/results from running the queries
- `DecodeLabs_Project1_Cleaned.xlsx` — cleaned source dataset

## Key Analysis
The final combined query summarizes orders by **Payment Method** and **Order Status**, showing order counts and total sales for each combination — useful for spotting trends like which payment methods have the highest cancellation or return rates.

## How to Run
1. Clone this repository
2. Make sure Python and `sqlite3` are available
3. Run `db.py` to set up/connect to the database
4. Run `queries.py` to execute the analysis queries

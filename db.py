import pandas as pd
import sqlite3
import os

import pandas as pd
import sqlite3
import os

import pandas as pd
import sqlite3
import os

folder = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(folder, "DecodeLabs_Project1_Cleaned.xlsx")
db_path = os.path.join(folder, "database.db")

# Read ALL sheets
all_sheets = pd.read_excel(excel_path, sheet_name=None)

print(f"Found {len(all_sheets)} sheets: {list(all_sheets.keys())}")

conn = sqlite3.connect(db_path)

for sheet_name, df in all_sheets.items():
    # Clean table name
    table_name = sheet_name.replace(" ", "_").lower()
    print(f"Saving sheet '{sheet_name}' -> table '{table_name}' with {len(df)} rows")
    df.to_sql(table_name, conn, if_exists='replace', index=False)

print("\nDone! All sheets saved to database.db")

# Show tables
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables in DB:", tables)

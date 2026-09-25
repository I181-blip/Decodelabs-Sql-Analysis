import pandas as pd
import sqlite3
import pandas as pd

conn = sqlite3.connect('database.db')

cols = pd.read_sql("SELECT * FROM sheet1 LIMIT 1", conn)
print("Columns in sheet1 (1200 rows):", cols.columns.tolist())
print("\n1. SELECT query:")
print(pd.read_sql("SELECT * FROM sheet1 LIMIT 5", conn))

print("\n2. WHERE query (filter):")
print(pd.read_sql('SELECT * FROM sheet1 WHERE TotalPrice > 100 LIMIT 5', conn))

print("\n3. ORDER BY query:")
print(pd.read_sql('SELECT * FROM sheet1 ORDER BY TotalPrice DESC LIMIT 5', conn))

print("\n4. GROUP BY query:")
print(pd.read_sql('SELECT PaymentMethod, COUNT(*) AS total FROM sheet1 GROUP BY PaymentMethod', conn))

print("\n5. COUNT, SUM, AVG:")
print(pd.read_sql('SELECT COUNT(*) AS count, SUM(TotalPrice) AS total_revenue, AVG(TotalPrice) AS avg_order_value FROM sheet1', conn))

print("\n6. FINAL COMBINED QUERY for report:")
print(pd.read_sql('''
    SELECT PaymentMethod, OrderStatus, COUNT(*) AS orders, SUM(TotalPrice) AS total_sales
    FROM sheet1
    GROUP BY PaymentMethod, OrderStatus
    ORDER BY total_sales DESC
''', conn))
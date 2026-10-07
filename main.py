import sqlite3
import pandas as pd

conn = sqlite3.connect("my_sql.sqlite")
cur = conn.cursor()

"""cur.execute('''
    CREATE TABLE Products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price FLOAT);
'''   
)"""

cur.execute(
    """
    INSERT INTO Products(name,price)
    VALUES("Buns", 350.50),("Bread",90.00)
"""
)
conn.commit()

cur.execute(
    """
    SELECT * FROM Products
"""
)
print(cur.fetchall())

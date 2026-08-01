"""
Qno.82: Use as to assign result of a database query variable and handle it.

Difficult words:
- query: request for data from database.
"""

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INTEGER, name TEXT)")
cur.execute("INSERT INTO users VALUES (1, 'Ali')")
cur.execute("INSERT INTO users VALUES (2, 'Sara')")

for row in cur.execute("SELECT * FROM users"):
    user_record = row  # using 'as' idea by assigning query result
    print("Fetched:", user_record)

conn.close()

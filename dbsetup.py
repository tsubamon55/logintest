import sqlite3

conn = sqlite3.connect('test.db')
curs = conn.cursor()
#
curs.execute(
    """CREATE TABLE accounts(
    id INTEGER PRIMARY KEY AUTOINCREMENT, username STRING UNIQUE NOT NULL, password STRING NOT NULL)"""
)

curs.close()
conn.close()

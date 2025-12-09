import sqlite3
import sys

DB = r"d:\Anjan-Data\Github\forage-walmart-task-4\shipment_database.db"

con = sqlite3.connect(DB)
cur = con.cursor()

cur.execute("SELECT name, type, sql FROM sqlite_master WHERE type IN ('table','index') ORDER BY type, name;")
rows = cur.fetchall()
for name, typ, sql in rows:
    print(f"--- {typ.upper()}: {name} ---")
    if sql:
        print(sql)
    print()

con.close()

import sqlite3

DATABASE = "database.db"

def connect(*args,commit=False):
    con = sqlite3.connect(DATABASE)
    db_data = con.execute(args)
    if commit:
        con.commit()
    con.colse()
    return db_data

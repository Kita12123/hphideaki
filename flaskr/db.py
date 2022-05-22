import sqlite3

DATABASE = "database.db"

def connect(sql,commit=False):
    con = sqlite3.connect(DATABASE)
    con.cursor()
    db_data = con.execute(sql)
    if commit:
        con.commit()
    con.close()
    return db_data

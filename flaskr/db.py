import sqlite3

DATABASE = "database.db"

def connect(sql:str, parameter:list=[], commit=False):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    if parameter:
        db_data = cur.execute(sql,parameter)
    else:
        db_data = cur.execute(sql)
    if commit:
        con.commit()
#    con.close()
    return db_data

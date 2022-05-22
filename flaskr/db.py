import sqlite3

DATABASE = "database.db"

def connect(sql:str, parameter:list=[]):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    if parameter:
        db_data = cur.execute(sql,parameter)
        con.commit()
    else:
        db_data = cur.execute(sql)
#    con.close()
    return db_data

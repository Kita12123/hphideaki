"""Craft Flask APP"""

from flask import Flask
app = Flask(__name__)

import os
import psycopg2
DSN = os.environ.get("POSTGRESQL_DSN")
class DB:
    def open(self):
        self.conn = psycopg2.connect(DSN)
        self.cur = self.conn.cursor()
    def close(self):
        self.cur.close()
        self.conn.close()
    def commit(self):
        self.conn.commit()
SQL = DB()
SQL.open()
SQL.cur.execute("CREATE TABLE IF NOT EXISTS history (_date_ TEXT, _title_ TEXT, _document_ TEXT)")
SQL.commit()
SQL.close()

import flaskr.main

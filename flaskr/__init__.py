"""Craft Flask APP"""

from flask import Flask
app = Flask(__name__)


import flaskr.main

from flaskr.db import DB
SQL = DB()
SQL.open()
SQL.cur.execute("CREATE TABLE IF NOT EXISTS history (_date_ TEXT, _title_ TEXT, _document_ TEXT)")
SQL.commit()
SQL.cur.execute("INSERT INTO history VALUES (%s,%s,%s)",["","テスト","説明文"])
SQL.commit()
SQL.close()
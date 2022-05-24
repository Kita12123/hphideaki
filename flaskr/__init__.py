"""Craft Flask APP"""

from flask import Flask
app = Flask(__name__)


import flaskr.main

from flaskr import db
cur = db.open()
cur.execute("CREATE TABLE IF NOT EXISTS history (_date_ TEXT, _title_ TEXT, _document_ TEXT)")
db.commit()
cur.execute("INSERT INTO history VALUES (%s,%s,%s)",["","テスト","説明文"])
db.commit()
db.close()
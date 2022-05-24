"""Craft Flask APP"""

from flask import Flask
app = Flask(__name__)


import flaskr.main

from flaskr import db
db.delete("CREATE TABLE IF NOT EXISTS history (_date_ TEXT, _title_ TEXT, _document_ TEXT)")
db.insert("INSERT INTO history VALUES (%s,%s,%s)",["","テスト","説明文"])
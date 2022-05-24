"""Craft Flask APP"""

from flask import Flask
app = Flask(__name__)


import flaskr.main

from flaskr import db
db.connect("CREATE TABLE IF NOT EXISTS history (_date_ TEXT, _title_ TEXT, _document_ TEXT)",commit=True)
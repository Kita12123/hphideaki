from flask import Flask
app = Flask(__name__)
import flaskr.main

from flaskr import db
db.connect("CREATE TABLE IF NOT EXISTS history (date, title, document)")
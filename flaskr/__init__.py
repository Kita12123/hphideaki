from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
class History(db.Model):
    __tablename__ = "history"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)
    title = db.Column(db.Text)
    document = db.Column(db.Text)
db.create_all()

import flaskr.main


#from flaskr import db
#db.connect("CREATE TABLE IF NOT EXISTS history (date, title, document)")
from flaskr import app
from flask import render_template, url_for, request, redirect

from flaskr.db import DB
SQL = DB()

@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
    SQL.open()
    SQL.cur.execute("SELECT * FROM history ORDER BY _date_ ASC")
    db_data = SQL.cur.fetchall()
    SQL.close()
    return render_template(
        "index.html",
        historys = [
            {"date":row[0], "title":row[1], "document":row[2]}
                for row in db_data
            ]
        )

@app.route("/add-history", methods=["POST"])
def add_history():
    date = request.form.get("date",default="????")
    title = request.form.get("title",default="????")
    document = request.form.get("document",default="")
    SQL.open()
    SQL.cur.execute("INSERT INTO history VALUES (%s,%s,%s)",[date,title,document])
    SQL.commit()
    SQL.close()
    return redirect(url_for("index"))

@app.route("/del-history/<date><title>")
def del_history(date,title):
    SQL.open()
    SQL.cur.execute(f"DELETE FROM history WHERE _date_ = '{date}' AND _title_ = '{title}'")
    SQL.commit()
    SQL.close()
    return redirect(url_for("index"))
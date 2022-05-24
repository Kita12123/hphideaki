from flaskr import app, db
from flask import render_template, url_for, request, redirect


@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
    return render_template(
        "index.html",
        historys = [
            {"date":row[0], "title":row[1], "document":row[2]}
                for row in db.select("SELECT * FROM history ORDER BY _date_ ASC")
            ]
        )

@app.route("/add-history", methods=["POST"])
def add_history():
    date = request.form.get("date",default="????")
    title = request.form.get("title",default="????")
    document = request.form.get("document",default="")
    db.insert("INSERT INTO history VALUES (%s,%s,%s)",[date,title,document])
    return redirect(url_for("index"))

@app.route("/del-history/<date><title>")
def del_history(date,title):
    db.delete(f"DELETE FROM history WHERE _date_ = '{date}' AND _title_ = '{title}'")
    return redirect(url_for("index"))
from flaskr import app, db
from flask import render_template, url_for, request, redirect


@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
    return render_template(
        "index.html",
        historys = [
            {"date":row[0], "title":row[1], "document":row[2]}
                for row in db.connect("SELECT * FROM history ORDER BY date ASC")
                ]
    )

@app.route("/add-history", methods=["POST"])
def add_history():
    date = request.form.get("date",default="????")
    title = request.form.get("title",default="????")
    document = request.form.get("document",default="")
    db.connect("INSERT INTO history VALUES (?,?,?)",[date,title,document],commit=True)
    return redirect(url_for("index"))

@app.route("/del-history/<date><title>")
def del_history(date,title):
    db.connect(f"DELETE FROM history WHERE _date_ = '{date}' AND _title_ = '{title}'",commit=True)
    return redirect(url_for("index"))
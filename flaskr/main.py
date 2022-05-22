from flaskr import app, db
from flask import render_template, url_for, request, redirect

@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
    return render_template(
        "index.html",
        historys = [
            {"date":row[0],"title":row[1],"document":row[2]}
                for row in db.connect("SELECT * FROM history")
                ]
    )

@app.route("/form")
def form():
    return render_template(
        "form.html"
    )

@app.route("/register", methods=["POST"])
def register():
    date = request.form.get("date",default="????")
    title = request.form.get("title",default="????")
    document = request.form.get("document",default="")
    db.connect("INSERT INTO history VALUES (?,?,?)",[date,title,document])
    return redirect(url_for("index"))
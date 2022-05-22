from flaskr import app, History, db
from flask import render_template, url_for, request, redirect


@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
    return render_template(
        "index.html",
#        historys = [
#            {"date":row[0],"title":row[1],"document":row[2]}
#                for row in db.connect("SELECT * FROM history ORDER BY date ASC")
#                ]
        historys = History.query.all()
    )

@app.route("/form")
def form():
    return render_template(
        "form.html"
    )

@app.route("/addhistory", methods=["POST"])
def add_history():
    date = request.form.get("date",default="????")
    title = request.form.get("title",default="????")
    document = request.form.get("document",default="")
#    db.connect("INSERT INTO history VALUES (?,?,?)",[date,title,document],commit=True)
    history = History(date=date, title=title,document=document)
    db.session.add(history)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delhistory/<id>")
def del_history(date,title):
#    db.connect(f"DELETE FROM history WHERE date = '{date}' AND title = '{title}'",commit=True)
    user = History.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("index"))
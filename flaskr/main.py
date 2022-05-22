from flaskr import app
from flask import render_template

@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
   return render_template(
       "index.html"
   )
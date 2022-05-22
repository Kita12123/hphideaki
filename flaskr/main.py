from flaskr import app

@app.route("/")    # [現在のURL+"/"]と通信時、実行
def index():
   return "Hello World!"    # 画面表示
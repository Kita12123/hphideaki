import flaskr
import os
if __name__ == "__main__":
   port = int(os.getenv("PORT",5000))    # ポート指定(デフォルト:5000)
   flaskr.app.run(    # flask起動
       host="0.0.0.0",    # ipアドレス指定(localhost)
       port=port,
       debug=True    # デバッグをする
       )
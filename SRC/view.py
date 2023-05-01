# coding: utf-8

from flask import Flask, render_template

# Flaskをインスタンス化
app = Flask(__name__)

# ------ view側の設定--------
# ルートディレクトリにアクセスした場合の挙動
@app.route("/")
# def以下がアクセス後の動作
def index():
    #return "Hello World!"
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

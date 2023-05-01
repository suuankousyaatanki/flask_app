# 必要なモジュールをインポート
from flask import Flask

# Flaskをインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあったときの処理
@app.route("/")
def hello():
    return "Hello World!"


# エントリーポイント
if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
from Watcher import watcher
import pathlib
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload')
def upload():
    input_dir = "./static/input_dir"
    images = list(pathlib.Path(input_dir).glob('**/*.png'))
    return render_template("upload_list.html",images=images)

if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    watcher()
    app.run(debug=True)

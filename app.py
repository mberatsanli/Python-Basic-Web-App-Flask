from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to python server!"

@app.route('/404')
def page404():
    return render_template('/404.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
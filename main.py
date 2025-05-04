from flask import Flask, render_template, send_file
from waitress import serve

app = Flask(__name__, template_folder=".")

@app.route("/")
def index():
     return render_template('index.html')

@app.route("/zeitgeist")
def company():
     return render_template('static/html/zeitgeist.html')

@app.route("/pgp")
def encrypt():
    return send_file('pgp.txt')

if __name__ == "__main__":
    print("Starting server!")
    #serve(app, host="0.0.0.0", port=85)
    app.run(host="127.0.0.1", port=8080, debug=True)#
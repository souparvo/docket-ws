from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return """<h1>Hello World</h1>"""

@app.route("/bah")
def bah():
  return """<h4>Boo</h4>"""

@app.route("/templates")
def complicated():
  return render_template('example.html')
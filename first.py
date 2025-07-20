from flask import Fkask

app= Flask(__name__)

@app.route("/home")
def home():
  return "this is my information"

@app.route("/phone")
def phone():
  return "266431313246"

app.run(host="0.0.0.0")
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def password():
    return render_template("password.html")

@app.route("/propuesta")
def home():
    name = "Nat"
    return render_template("index.html", name=name)

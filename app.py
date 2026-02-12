from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Nat"
    return render_template("index.html", name=name)

@app.route("/yes")
def yes():
    name = "Nat"
    return render_template("yes.html", name=name)

if __name__ == "__main__":
    app.run()

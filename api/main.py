from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/workbook")
def workbook():
    if session.get("username", False):
        return render_template("workboook.html")
    return redirect("/")
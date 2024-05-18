from flask import Flask, render_template, redirect, request, session

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

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if (email, password) == ("mihai@gmail.com", "Password"):
            session["username"] = "Mihai"
            return redirect("/")
    return render_template("login.html")

@app.route("/workbook")
def workbook():
    if session.get("username", False):
        return render_template("workbook.html")
    return redirect("/")
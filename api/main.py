from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "secret"
app.config["MAINTENANCE"] = False

@app.before_request
def maintenance():
    if app.config["MAINTENANCE"] and request.path == "/":
        return render_template("maintenance.html")
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if (email, password) == ("mihai@gmail.com", "Password"):
            session["username"] = "Mihai"
            return redirect("/")
        elif (email, password) == ("admin@gmail.com", "Admin"):
            session["admin"] = "admin"
            return redirect("/")
    return render_template("login.html")

@app.route("/workbook")
def workbook():
    if session.get("username", False):
        return render_template("workbook.html")
    return redirect("/")

@app.route("/admin")
def admin():
    if session.get("admin", False):
        return render_template("admin.html", maintenance_status=app.config["MAINTENANCE"])
    return redirect("/")

@app.route("/admin/change-maintenance")
def admin_maintenance():
    if session.get("admin", False):
        app.config["MAINTENANCE"] = True if not app.config["MAINTENANCE"] else False
        return redirect("/admin")
    return redirect("/")

@app.errorhandler(404)
def page404(error):
    return render_template("page404.html")

@app.errorhandler(500)
def page500(error):
    return render_template("page500.html")

from flask import Flask, redirect

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    return redirect("https://mihai-ciorobitca.vercel.app/")
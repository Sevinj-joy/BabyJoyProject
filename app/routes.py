# app/routes

from flask import render_template
from run import app

@app.route("/")
def index():
    return render_template("app/index.html")

@app.route("/products")
def products():
    return render_template("app/Products.html")
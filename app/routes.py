# app/routes

from flask import render_template
from run import app

@app.route("/")
def index():
    return render_template("app/index.html")


@app.route("/products")
def app_products():
    from models import Products
    return render_template("app/Products.html")
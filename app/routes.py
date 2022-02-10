from run import app
from flask import render_template


@app.route("/")
def app_index():
    return render_template("app/Index.html")


@app.route("/products")
def app_products():
    return render_template("app/Products.html")

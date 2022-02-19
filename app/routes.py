# app/routes
from itertools import product
from flask import render_template, request,url_for,redirect
from run import app,db
import os

@app.route("/")
def index():
    return render_template("app/index.html")

@app.route("/login")
def login():
    return render_template("app/form.html")

@app.route("/products")
def products():
    return render_template("app/products.html")


@app.route("/aproduct")
def a_product():
    return render_template("admin/a_product.html")

@app.route("/admin")
def admin():
    return render_template("admin/Admin_panel.html")
             
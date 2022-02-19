# app/routes

from flask import render_template, request,url_for,redirect
from flask_login import login_user
from models import *
from run import app,db
import os
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt(app)
@app.route("/")
def index():
    return render_template("app/index.html")

@app.route("/register" , methods=['GET','POST'])
def register():

    form =RegisterForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data)
        new_user= User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('register'))
    return render_template("app/form.html", form=form)


@app.route("/aproduct")
def a_product():
    return render_template("admin/a_product.html")

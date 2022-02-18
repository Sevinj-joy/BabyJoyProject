from fileinput import filename
from run import app, db
from flask import render_template, request, url_for,redirect
import os
from models import *

@app.route("/admin", method=['GET', 'POST'] )
def app_admin():
    return render_template("admin/Admin_panel.html")


@app.route("/admin/products" , method=['GET', 'POST'])
def admin_products():
    from models import Products
    products =Products.query.all()
    if request.method=='POST':
        file=request.files['products_img']
        file.save(os.path.join('static/uploads',filename))
        product_categ=request.form["products_category"]
        product_price=request.form["product_price"]
        product=Products(
           product_categ=product_categ,
           product_price=product_price,
           product_image=filename
        )
        db.session.add(product)
        db.session.commit()
        return redirect("/admin/products")
    return render_template("admin/products.html", products=products)

    
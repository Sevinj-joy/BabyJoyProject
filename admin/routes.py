from run import app,db
from flask import render_template,redirect,request
import os
from fileinput import filename

@app.route("/products")
def app_products():
    from models import Products
    products=Products.query.all()
    return render_template("app/products.html")

# Products

@app.route("/admin/products",method=['GET', 'POST'])
def admin_products():
    from models import Products
    products =Products.query.all()
    if request.method=='POST':
        file=request.files['products_img']
        filename=file.filename
        file.save(os.path.join('static/uploads',filename))
        product_categ=request.form["products_category"]
        product_price=request.form["products_price"]
        product=Products(
           product_categ=product_categ,
           product_price=product_price,
           product_image=filename
        )
        db.session.add(product)
        db.session.commit()
        return redirect("/admin/products")
    return render_template("admin/a_product.html", products=products)

# Products delete
@app.route("/admin/products/delete/<int:id>")
def admin_products_delete(id):
    from  models import Products
    products=Products.query.filter_by(id=id).first()
    db.session.delete(products)
    db.session.commit()
    return redirect("/admin/products")

# Products update
@app.route("/admin/products/update/<int:id>", methods=['GET', 'POST'])
def admin_products_update(id):
    from models import Products
    newProducts = Products.query.filter_by(id=id).first()
    if request.method=='POST':
        products = Products.query.filter_by(id=id).first()
        products.product_categ=request.form["products_category"]
        products.product_price=request.form["products_price"]
        db.session.commit()
        return redirect("/admin/products")
    return render_template("admin/update_products.html", newProducts=newProducts)
from flask import Flask ,redirect, url_for, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myproducts.db'
db = SQLAlchemy(app)

class products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product_categ=db.Column(db.String(70), unique=True, nullable=False)
    product_price=db.Column(db.Integer,unique=True, nullable=False)
    product_image=db.Column(db.String(50))

from app.routes import *


from admin.routes import *

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
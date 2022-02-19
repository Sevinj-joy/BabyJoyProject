from flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myproducts.db'
app.config['SECRET KEY'] ='HFHFJHDJJDIJ'
bcrypt=Bcrypt(app)

db = SQLAlchemy(app)

from models import *

from app.routes import *

from admin.routes import *

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask ,redirect, url_for, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myproducts.db'
db = SQLAlchemy(app)



from app.routes import *


from admin.routes import *

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)
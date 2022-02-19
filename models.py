from run import db

# Products

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product_categ=db.Column(db.String(70), unique=True, nullable=False)
    product_price=db.Column(db.String(100),unique=True, nullable=False)
    product_image=db.Column(db.String(50))
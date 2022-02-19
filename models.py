import email
from enum import unique
import flask_login
from run import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField,StringField, EmailField
from wtforms.validators import ValidationError, Length, EqualTo, InputRequired
from flask_bcrypt import Bcrypt
# Products

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product_categ=db.Column(db.String(70), unique=True, nullable=False)
    product_price=db.Column(db.String(100),unique=True, nullable=False)
    product_image=db.Column(db.String(50))


class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), nullable=False, unique=True)
    email=db.Column(db.String(50), nullable=False, unique=True)
    password=db.Column(db.String(80), nullable=False)
    repeat_password=db.Column(db.String(80), nullable=False)
db.create_all()

# class LoginForm(FlaskForm):
#     username=StringField(validators=[InputRequired(), Length(min=4 , max= 80)
#     ], render_kw={'placeholder' :'Username'})

#     email=EmailField(validators=[InputRequired(), Length(min=5 , max= 50)
#     ], render_kw={'placeholder': 'Email'})

#     password=PasswordField(validators=[InputRequired(), Length(min=7 , max= 20)
#     ], render_kw={'placeholder' :'Password'})

#     repeat_password=PasswordField(validators=[InputRequired(), Length(min=7 , max= 20)
#     ], render_kw={'placeholder' :'Repeat Password'})

#     submit=SubmitField("login")


class RegisterForm(FlaskForm):
    username=StringField(validators=[InputRequired(), Length(min=4 , max= 80)
    ], render_kw={'placeholder' :'Username'})

    email=EmailField(validators=[InputRequired(), Length(min=5 , max= 50)
    ], render_kw={'placeholder': 'Email'})

    password=PasswordField(validators=[InputRequired(), Length(min=7 , max= 20)
    ], render_kw={'placeholder' :'Password'})

    submit=SubmitField("register")

def validate_username(self, username):
    existing_user_username=User.query.filter_by(username=username.data).first()
    if existing_user_username:
       raise ValidationError
       ("Bu istifadeci adi artiq movcuddur")


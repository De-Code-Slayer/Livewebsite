
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Blog website --------------------------------------------
class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    articles = db.Column(db.String(10000))
    articletitle = db.Column(db.String(250))
    author = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    time = db.Column(db.DateTime)
    file_path = db.Column(db.String(250))
# ---------- Student--------------------------------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150))
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    nationality = db.Column(db.String(250))
    age = db.Column(db.Integer())
    school = db.Column(db.String(100))
    course = db.Column(db.String(250))
    degree = db.Column(db.String(250))
    university = db.Column(db.String(250))
    admission_status = db.Column(db.String(250))
    email = db.Column(db.String(250))
    phone = db.Column(db.String(250))
    occupation = db.Column(db.String(250))
    password = db.Column(db.String(250))
    conditional_acceptance = db.Column(db.Integer())
    admission = db.Column(db.Integer())
    visa = db.Column(db.Integer())
    flight = db.Column(db.Integer())
    arrival = db.Column(db.Integer())
    admin = db.Column(db.Boolean, default=False)
    business_signed_up = db.Column(db.Boolean, default=False)
#-------------------------------  end of database for blog -------------------------------------


class Whatsapp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    link = db.Column(db.String(250))
    institute = db.Column(db.String(100))



class Howto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    content = db.Column(db.String(10000))


# ---------- students section---------


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(250))
    country = db.Column(db.String(250)) 
    region = db.Column(db.String(250)) 
    fee = db.Column(db.String(250)) 
    schorlarship = db.Column(db.String(250))  
    website = db.Column(db.String(250)) 




class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    category = db.Column(db.String(250))
    percentage = db.Column(db.Integer)
    image = db.Column(db.String(250))

   
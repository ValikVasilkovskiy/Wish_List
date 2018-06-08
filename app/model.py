from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    birthday = db.Column(db.Date, unique=False, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return '<User: id: {} username: {} email: {}>'.format(self.id, self.username, self.email)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, product_name):
        self.product_name = product_name

class Holiday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    holiday_name = db.Column(db.String(120), unique=True, nullable=False)
    holiday_date = db.Column(db.Date, unique=False, nullable=False)

    def __init__(self, holiday_name, holiday_date):
        self.holiday_date = holiday_date
        self.holiday_name = holiday_name

class Wish_Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    holiday_id = db.Column(db.Integer, db.ForeignKey('holiday.id'), nullable=False)










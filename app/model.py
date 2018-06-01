from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Database configurations
app = Flask(__name__)




DB_USER = 'flask'
DB_PASS = 'Pa$$w0rd'
DB_HOST = 'db'
DB_PORT = '3306'
DATABASE = 'wish_list'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'\
    .format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User: {}>'.format(self.username)

import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)


# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(os.environ["MYSQL_USER"], os.environ["MYSQL_PASSWORD"], os.environ["MYSQL_HOST"], os.environ["MYSQL_DATABASE"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(app.config['SQLALCHEMY_DATABASE_URI'])
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


@app.route('/')
def index():
    db.drop_all()
    db.create_all()
    User.query.all()  # if no error, it means it connected to mysql server successfully
    return 'Docker-Compose for Flask & MySQL'


@app.route('/test')
def test():
    return jsonify({"users": [user.username for user in User.query.all()]})


@app.route('/create_table')
def createUserTable():
    try:
        db.create_all()
        return jsonify({'status': True})
    except IntegrityError:
        return jsonify({'status': False})


@app.route('/test')
def insert_user():
    try:
        user = User(username='Arch', email='arch.mail@gmail.com')
        db.session.add(user)
        db.session.commit()
        return jsonify({'status': True})
    except IntegrityError:
        return jsonify({'status': False})

@app.route('/user')
def show_users():
    try:
        users = User.query.all()
        users_dict = {}
        for user in users:
            users_dict[user.username] = {'email': user.email}
        return jsonify(users_dict)
    except IntegrityError:
        return jsonify({'Table User is empty': True})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


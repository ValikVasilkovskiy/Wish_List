from flask import Flask
from model import db
from model import User


from sqlalchemy.exc import IntegrityError



from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Docker-Compose for Flask & MySQL'


@app.route('/test')
def test():
    return jsonify(User.query.all())


@app.route('/create_table')
def createUserTable():
    try:
        db.create_all()
        return jsonify({'status': True})
    except IntegrityError:
        return jsonify({'status': False})


@app.route('/insert_user')
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


import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from sqlalchemy.exc import IntegrityError

from views import IndexView, PrepareModel
from model import User

app = Flask(__name__)


# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(os.environ["MYSQL_USER"], os.environ["MYSQL_PASSWORD"], os.environ["MYSQL_HOST"], os.environ["MYSQL_DATABASE"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

print(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)



app.add_url_rule('/index',
                 view_func=
                 IndexView.as_view('index'))

app.add_url_rule('/',
                 view_func=
                 PrepareModel.as_view('preparemodel'))


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


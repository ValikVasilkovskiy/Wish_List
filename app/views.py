from app import db
from model import User, Product, Holiday, Wish_Object
from flask import request, Response, jsonify, render_template, redirect, url_for
from flask.views import MethodView

class PrepareModel(MethodView):
    def create_data(self):
        db.drop_all()
        db.create_all()
        users = User.query.all()  # if no error, it means it connected to mysql server successfully
        return render_template(
            'preparemodel.html',
            context ={
                'users': users,
            }
        )

class IndexView(MethodView):
    def index(self):
        return render_template(
            'index.html'
        )


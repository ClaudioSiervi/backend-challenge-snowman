import os
from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource, reqparse

from resources.tourist_spot import TouristSpot, TouristFilter
from resources.category import Category, CategoryFinder, CategoryModel
from resources.picture import Picture
from resources.comment import Comment
from resources.favorite import Favorite
from security import authenticate, identity
from resources.user import UserRegister, UserList,UserModel
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_EXCEPTIONS'] = True

app.secret_key = "snowman"

api = Api(app)

@app.before_first_request
def create_tables():

    db.create_all()

    # add required categories into new db's
    try:
        # verify whether there is a registered category
        category = CategoryModel.find_category_by_id(_id=1)
        print(category.id)
    except:
        # id_user = 1 --> admin
        us = UserModel(username='claudio', password='snowlabs')
        db.session.add(us)

        me = CategoryModel('Park', id_user=1)
        db.session.add(me)
        me = CategoryModel('Museum', id_user=1)
        db.session.add(me)
        me = CategoryModel('Theater', id_user=1)
        db.session.add(me)
        me = CategoryModel('Monument', id_user=1)
        db.session.add(me)

        db.session.commit()



jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Category,       "/categories")
api.add_resource(CategoryFinder, "/categories/<string:name>")

api.add_resource(TouristSpot,   "/tourist-spots")
api.add_resource(TouristFilter, "/tourist-spots/<string:name>")

api.add_resource(Picture,       "/tourist-spots/<int:id_tourist_spot>/pictures")

api.add_resource(Comment,       "/tourist-spots/<int:id_tourist_spot>/comments")

api.add_resource(UserList,      "/users")
api.add_resource(UserRegister,  "/users/register")
api.add_resource(Favorite,      "/users/<int:id_user>/favorites")


# prevent to run the app when import source
if __name__ == "__main__":

    db.init_app(app)
    app.run(debug=True, port=4999)
from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource, reqparse

from resources.tourist_spot import TouristSpot, TouristFilter
from resources.category import Category, CategoryFinder
from security import authenticate, identity
from resources.user import UserRegister, UserList
from db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "snowman"

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # create a new endpoint /auth

api.add_resource(Category, "/category")
api.add_resource(CategoryFinder, "/category/<string:name>")

api.add_resource(TouristFilter, "/tourist-spot/<string:name>")
api.add_resource(TouristSpot, "/tourist-spot")

api.add_resource(UserRegister, "/user/register")
api.add_resource(UserList, "/users")

# prevent to run the app when import source
if __name__ == "__main__":

    db.init_app(app)
    app.run(debug=True, port=4999)
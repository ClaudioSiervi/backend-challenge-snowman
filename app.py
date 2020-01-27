from flask import Flask, request
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource, reqparse

from resources.tourist_spot import TouristSpot, TouristSpotList
from resources.category import Category, CategoryList
from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.secret_key = "snowman"
api = Api(app)



jwt = JWT(app, authenticate, identity)  # create a new endpoint /auth

api.add_resource(Category, "/category/<string:name>")
api.add_resource(CategoryList, "/category")
api.add_resource(TouristSpot, "/tourist-spot/<string:name>")
api.add_resource(TouristSpotList, "/tourist-spot")
api.add_resource(UserRegister, "/register")


app.run(debug=True, port=4999)
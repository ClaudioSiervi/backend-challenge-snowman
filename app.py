from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "snowman"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # create a new endpoint /auth

tourist_spots = []
categories = [
        {"name": "Park", "user_id":"0"},
        {"name": "Museum", "user_id":"0"}, 
        {"name": "Theater", "user_id":"0"},
        {"name": "Monument", "user_id":"0"}
    ]

class Category(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=int, help="This field cannot be left blank!")

    def get(self, name):
        for category in categories:
            if category['name'] == name:
                return {"category": category}
        return {'messege': "category not found"}

    @jwt_required()   # force authentication
    def post(self, name):
        request_data = Category.parser.parse_args() # prevent parsing errors
        new_category = {
            "name": name,
            "user_id": request_data['user_id']
        }
        categories.append(new_category)
        return {"new_category": new_category}


class CategoryList(Resource):
    def get(self):
        return {"categories": categories}


class TouristSpot(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('gps', type=dict, help='This field cannot be left blank!')
    parser.add_argument('category', type=str, required=True, help='This field cannot be left blank!')
    parser.add_argument('pictures', type=dict, help='This field cannot be left blank!')

    # GET /tourist-spot/<string:name>
    def get(self, name):
        for tourist_spot in tourist_spots:
            if tourist_spot['name'] == name:
                return {"tourist_spot": tourist_spot}
        return {'messege': "tourist spot not found"}
    
    # POST /tourist-spot {name:}
    def post(self, name):
        
        request_data = TouristSpot.parser.parse_args()  # prevent parsing errors
        new_tourist_spot = {
                "name": name,
                "gps": request_data['gps'],
                "category": request_data['category'],
                "pictures": request_data['pictures'] 
                }
        tourist_spots.append(new_tourist_spot)   
        return {"new_tourist_spot": new_tourist_spot}


class TouristSpotList(Resource):
    # GET /tourist-spots
    def get(self):
        return {"tourist_spots": tourist_spots}


api.add_resource(Category, "/category/<string:name>")
api.add_resource(CategoryList, "/category")
api.add_resource(TouristSpot, "/tourist-spot/<string:name>")
api.add_resource(TouristSpotList, "/tourist-spot")


app.run(debug=True, port=4999)
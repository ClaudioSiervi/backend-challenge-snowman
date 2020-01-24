from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tourist_spots = []
categories = [
        {"name": "Park", "user_id":"0"},
        {"name": "Museum", "user_id":"0"}, 
        {"name": "Theater", "user_id":"0"},
        {"name": "Monument", "user_id":"0"}
    ]

class Category(Resource):
    def get(self, name):
        for category in categories:
            if category['name'] == name:
                return {"category": category}
        return {'messege': "category not found"}

    def post(self, name):
        data_requested = request.get_json()
        new_category = {
            "name": name,
            "user_id": data_requested['user_id']
        }
        categories.append(new_category)
        return {"new_category": new_category}


class TouristSpot(Resource):
   
    # GET /tourist-spot/<string:name>
    def get(self, name):
        for tourist_spot in tourist_spots:
            if tourist_spot['name'] == name:
                return {"tourist_spot": tourist_spot}
        return {'messege': "tourist spot not found"}
    
    # POST /tourist-spot {name:}
    def post(self, name):
        request_data = request.get_json()
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
api.add_resource(TouristSpot, "/tourist-spot/<string:name>")
api.add_resource(TouristSpotList, "/tourist-spot")


app.run(debug=True, port=4999)
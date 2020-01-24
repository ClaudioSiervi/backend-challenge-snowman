from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

tourist_spots = []

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


# GET /tourist-spots
class TouristSpotList(Resource):
    def get(self):
        return {"tourist_spots": tourist_spots}


api.add_resource(TouristSpot, "/tourist-spot/<string:name>")
api.add_resource(TouristSpotList, "/tourist-spot")


app.run(debug=True, port=4999)
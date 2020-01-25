from flask_restful import Resource, reqparse

tourist_spots = []

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

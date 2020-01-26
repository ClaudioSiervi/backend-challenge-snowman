from flask_restful import Resource, reqparse
import sqlite3

from models.tourist_spot import TouristSpotModel


class TouristSpotRegister(Resource):
    
    parser = reqparse.RequestParser()
    
    parser.add_argument('name', 
                type=str, 
                required=True,
                help='This field cannot be left blank!')
    parser.add_argument('gps', 
                type=str, 
                required=False,
                help='This field cannot be left blank!')
    parser.add_argument('id_category', 
                type=str, 
                required=True, 
                help='This field cannot be left blank!')

 # POST /tourist-spot
    def post(cls):

        data = cls.parser.parse_args()  

        tourist_spot = TouristSpotModel(**data) # parse by position

        try:
            tourist_spot.save_to_db()
        except:
             return {"Messege": "An error occured inserting the tourist spot."}, 500
        return tourist_spot.json(), 201



# select a specific tourist spot
class TouristSpot(Resource):
    # GET /tourist-spot/<string:name>
    def get(cls, name):

        try:
            tourist_spot = TouristSpotModel.find_spots_by_name(name)
        except: 
            return {'Messege': "Tourist spot not found."} 
        return {"tourist_spot_name": list(map(lambda x: x.json(), tourist_spot))}
   

class TouristSpotList(Resource):
    # GET /tourist-spots
    def get(self):
        return {"tourist_spot_list": list(map(lambda x: x.json(), TouristSpotModel.query.all()))}

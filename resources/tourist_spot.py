from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.tourist_spot import TouristSpotModel


class TouristSpot(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('name', 
                type=str, 
                # required=True,
                help='The "name" cannot be left blank!')
    parser.add_argument('gps', 
                type=str, 
                # required=False,
                help='The field "gps" cannot be left blank!')
    parser.add_argument('id_category', 
                type=str, 
                # required=True, 
                help='The field "id_category" cannot be left blank!')

    # GET /tourist-spot
    def get(self):
            return {"tourist_spot_list": list(map(lambda x: x.json(), TouristSpotModel.query.all()))}

    # POST /tourist-spot
    @jwt_required() # activate only after refactory user model and resource
    def post(cls):

        data = cls.parser.parse_args()  

        tourist_spot = TouristSpotModel(**data) # parse by position
        try:
            tourist_spot.save_to_db()
        except:
             return {"Messege": "An error occured inserting the tourist spot."}, 500
        return tourist_spot.json(), 201


class TouristFilter(Resource):
    # GET /tourist-spot/<string:name>
    def get(cls, name):
        try:
            tourist_spot = TouristSpotModel.find_spots_by_name(name)
        except: 
            return {'Messege': "Tourist spot not found."} 
        return {"tourist_spot_name": list(map(lambda x: x.json(), tourist_spot))}

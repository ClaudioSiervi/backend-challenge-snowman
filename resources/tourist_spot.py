from flask_restful import Resource, reqparse
import sqlite3

from models.tourist_spot import TrouristSpot


class TouristSpotRegister(Resource):
    
    parser = reqparse.RequestParser()

    parser.add_argument('gps', 
                type=str, 
                help='This field cannot be left blank!')
    parser.add_argument('id_category', 
                type=str, 
                required=False, 
                help='This field cannot be left blank!')
    parser.add_argument('id_user', 
                type=str, 
                help='This field cannot be left blank!')

 # POST /tourist-spot {name:}
    def post(cls, name):

        request_data = cls.parser.parse_args()  
        # if TrouristSpot.find_by_name(name) is not None:
        #     return {"messege ": "This tourist spot already registred."}
        new_spot = {
                "name": name,
                "gps": request_data['gps'],
                "id_category": request_data['id_category'],
                "id_user": request_data['id_user'] 
                }
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO tourist_spots VALUES (NULL, ?, ?, ?, ?)'
        cursor.execute(query, (new_spot['name'], new_spot['gps'], new_spot['id_category'], new_spot['id_user']))

        connection.commit()
        connection.close()

        return new_spot, 201


# select a specific tourist spot
class TouristSpot(Resource):
    # GET /tourist-spot/<string:name>
    def get(self, name):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT name FROM tourist_spots'
        cursor.execute(query)
        tourist_spots = cursor.fetchall()
        
        connection.commit()
        connection.close()

        for tourist_spot in tourist_spots:
            if tourist_spot[0] == name:
                return {"tourist_spot": tourist_spot[0]}

        return {'messege': "tourist spot not found"}
    
   

class TouristSpotList(Resource):
    # GET /tourist-spots
    def get(self):
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'SELECT name FROM tourist_spots'
        cursor.execute(query)

        tourist_spot_list = cursor.fetchall()

        connection.commit()
        connection.close()

        return {"tourist_spot_list": tourist_spot_list}

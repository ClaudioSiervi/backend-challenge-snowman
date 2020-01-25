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
                required=True, 
                help='This field cannot be left blank!')
    parser.add_argument('id_user', 
                type=str, 
                help='This field cannot be left blank!')

 # POST /tourist-spot {name:}
    def post(self, name):

        request_data = TouristSpotRegister.parser.parse_args()  

        new_spot = {
                "name": name,
                "gps": request_data['gps'],
                "id_category": request_data['id_category'],
                "id_user": request_data['id_user'] 
        }

        try:
            TrouristSpot.insert(new_spot)
        except:
            return {"Messege": "An error occured inserting the tourist spot."}, 500
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

        query = 'SELECT * FROM tourist_spots'
        result = cursor.execute(query)
        
        tourist_spot_list = []
        for row in result:
            tourist_spot_list.append({ "id": row[0],
                            "name": row[1],
                            "gps": row[2],
                            "id_category": row[3],
                            "id_user": row[4] 
            })

        connection.commit()
        connection.close()

        return {"tourist_spot_list": tourist_spot_list}
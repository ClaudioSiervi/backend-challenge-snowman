
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.picture import PictureModel


class Picture(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("name", 
                    type=str, 
                    help="The field 'name' cannot be left blank!")
    parser.add_argument("img_link", 
                    type=str, 
                    help="The field 'img_link' cannot be left blank!")
    parser.add_argument("id_tourist_spot", 
                    type=int, 
                    help="The field 'id_tourist_spot' cannot be left blank!")
   
    def get(self, id_tourist_spot):
        # GET /tourist-spot/<id>/picture
        return {"picture_list": list(map(lambda x: x.json(), PictureModel.find_pictures_by_tourist_spot_id(id_tourist_spot)))}


    def post(cls, id_tourist_spot):
        # POST /tourist-spot/<id>/picture
        data = cls.parser.parse_args()  

        picture = PictureModel(**data)
        try:
            picture.save_to_db()
        except:
             return {"Messege": "An error occured inserting the picture."}, 500
        return picture.json(), 201
        
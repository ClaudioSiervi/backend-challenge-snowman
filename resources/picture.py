
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
        # GET /picture
        return {"category_list": list(map(lambda x: x.json(), CategoryModel.query.all()))}

    
    def post(cls, id_tourist_spot):
        # POST /picture
        data = cls.parser.parse_args()  

        category = PictureModel(**data)
        try:
            category.save_to_db()
        except:
             return {"Messege": "An error occured inserting the picture."}, 500
        return category.json(), 201
        
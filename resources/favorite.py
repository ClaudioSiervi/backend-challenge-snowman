
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.favorite import FavoriteModel


class Favorite(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("id_tourist_spot", 
                    type=int, 
                    help="The field 'id_tourist_spot' cannot be left blank!")
    parser.add_argument("id_user", 
                    type=int, 
                    help="The field 'id_tourist_spot' cannot be left blank!")
    
    @jwt_required()
    def get(self, id_user):
        # GET /tourist-spot/<id>/picture
        return {"favorite_list": list(map(lambda x: x.json(), FavoriteModel.find_favorite_by_id_user(id_user)))}

    @jwt_required() 
    def post(cls, id_user):
        # POST /tourist-spot/<id>/picture
        data = cls.parser.parse_args()  

        favorite = FavoriteModel(**data)
        try:
            favorite.save_to_db()
        except:
             return {"Messege": "An error occured inserting the comment."}, 500
        return favorite.json(), 201
        
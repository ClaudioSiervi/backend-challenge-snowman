
from flask_restful import Resource, reqparse

from models.comment import CommentModel


class Comment(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("comment", 
                    type=str, 
                    help="The field 'name' cannot be left blank!")
    parser.add_argument("id_tourist_spot", 
                    type=int, 
                    help="The field 'id_tourist_spot' cannot be left blank!")
    parser.add_argument("id_user", 
                    type=int, 
                    help="The field 'id_tourist_spot' cannot be left blank!")

    def get(self, id_tourist_spot):
        # GET /tourist-spot/<id>/picture
        return {"commentary_list": list(map(lambda x: x.json(), CommentModel.find_comment_by_id_tourist_spot(id_tourist_spot)))}


    def post(cls, id_tourist_spot):
        # POST /tourist-spot/<id>/picture
        data = cls.parser.parse_args()  

        picture = CommentModel(**data)
        try:
            picture.save_to_db()
        except:
             return {"Messege": "An error occured inserting the comment."}, 500
        return picture.json(), 201
        
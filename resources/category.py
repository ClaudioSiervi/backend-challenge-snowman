
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

categories = [
        {"name": "Park", "user_id":"0"},
        {"name": "Museum", "user_id":"0"}, 
        {"name": "Theater", "user_id":"0"},
        {"name": "Monument", "user_id":"0"}
    ]

class Category(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("user_id", type=int, help="This field cannot be left blank!")

    def get(self, name):
        for category in categories:
            if category['name'] == name:
                return {"category": category}
        return {'messege': "category not found"}

    @jwt_required()   # force authentication
    def post(self, name):
        request_data = Category.parser.parse_args() # prevent parsing errors
        new_category = {
            "name": name,
            "user_id": request_data['user_id']
        }
        categories.append(new_category)
        return {"new_category": new_category}


class CategoryList(Resource):
    def get(self):
        return {"categories": categories}
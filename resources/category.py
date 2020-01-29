
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.category import CategoryModel
from db import db

class Category(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("name", 
                    type=str, 
                    help="The field 'name' cannot be left blank!")

    parser.add_argument("id_user", 
                type=str, 
                help="The field 'user_id' cannot be left blank!")

    def get(self):
        # GET /category
        return {"category_list": list(map(lambda x: x.json(), CategoryModel.query.all()))}

    @jwt_required()
    def post(cls):
        # POST /category
        data = cls.parser.parse_args()  

        category = CategoryModel(**data)
        try:
            category.save_to_db()
        except:
             return {"Messege": "An error occured inserting the category."}, 500
        return category.json(), 201
        

class CategoryFinder(Resource):
    
    def get(self, name):
        # GET /category/<string:name>
        category = CategoryModel.find_category_by_name(name)
        return {"category_list": list(map(lambda x: x.json(), category))}
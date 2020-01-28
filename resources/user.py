from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                type=str,
                required=True,
                help='This field cannot be black.'
    )
    parser.add_argument('password',
                type=str,
                required=True,
                help='This field cannot be blank.'
    )
    
    def post(cls):
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data['username']) is not None:
            return {"messege ": "This username already exists."}, 400

        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
             return {"Messege": "An error occured inserting the username."}, 500
        return ({"messege ": "User created."}), 201


class UserList(Resource):
    pass
    def get(self):
            return {"username_list": list(map(lambda x: x.json(), UserModel.query.all()))}
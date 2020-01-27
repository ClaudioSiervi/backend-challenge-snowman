from flask_restful import Resource, reqparse


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
    
    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']) is not None:
            return {"messege ": "This username already exists."}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password'],))

        connection.commit()
        connection.close()

        return ({"messege ": "User created."})
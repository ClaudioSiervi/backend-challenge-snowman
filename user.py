import sqlite3

from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
    

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() # collecting data from here

        query = "SELECT * FROM users WHERE username=?" # search user
        result = cursor.execute(query, (username,))  # apply a tuple to the query
        row = result.fetchone()  # return the first row found

        if row is not None:
            user = cls(*row) # parse a set of positional arguments
        else:
            user = None  # user not found

        connection.close()
        return user


    @classmethod
    def find_by_user_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 

        query = "SELECT * FROM users WHERE id=?" # search id
        result = cursor.execute(query, (_id, ))  
        row = result.fetchone() 

        if row is not None:
            user = cls(*row)
        else:
            user = None  

        connection.close()
        return user


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
import sqlite3


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
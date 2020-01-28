from db import db

class UserModel(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))

    category = db.relationship('CategoryModel')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            "username" : self.username,
            "password" : self.password
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_user_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self): 
        db.session.add(self)
        db.session.commit()
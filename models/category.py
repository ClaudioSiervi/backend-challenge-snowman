from flask_restful import Resource, reqparse

from db import db


class CategoryModel(db.Model):
    __tablename__= 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('UserModel')
    tourist_spot = db.relationship('TouristSpotModel')


    def __init__(self, name, id_user):
        self.name = name
        self.id_user = id_user


    def json(self):
        return {
            "id"   : self.id,
            "name" : self.name,
            "id_user": self.id_user
        }

    @classmethod
    def find_category_by_name(cls, name):
        return cls.query.filter_by(name=name)

    
    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()
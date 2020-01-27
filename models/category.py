from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from db import db


class CategoryModel(db.Model):
    __tablename__= 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    tourist_spot = db.relationship('TouristSpotModel')

    def __init__(self, name):
        self.name = name


    def json(self):
        return {
            "name" : self.name
        }

    @classmethod
    def find_category_by_name(cls, name):
        return cls.query.filter_by(name=name)

    
    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()
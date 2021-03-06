
from db import db


class PictureModel(db.Model):
    __tablename__= 'pictures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    img_link = db.Column(db.String(100))  # url picture 
    id_tourist_spot = db.Column(db.Integer, db.ForeignKey('tourist_spots.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    tourist_spot = db.relationship('TouristSpotModel')
    user = db.relationship('UserModel')


    def __init__(self, name, img_link, id_tourist_spot, id_user):
        self.name = name
        self.img_link = img_link
        self.id_tourist_spot = id_tourist_spot
        self.id_user = id_user


    def json(self):
        return {
                "id"   : self.id,
                "name" : self.name,
                "img_link" : self.img_link,
                "id_tourist_spot" : self.id_tourist_spot,
                "id_user" : self.id_user
        }
    
    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_pictures_by_tourist_spot_id(cls, id_tourist_spot):
        return cls.query.filter_by(id_tourist_spot=id_tourist_spot)
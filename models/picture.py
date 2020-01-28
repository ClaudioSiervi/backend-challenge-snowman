
from db import db


class PictureModel(db.Model):
    __tablename__= 'pictures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    img_link = db.Column(db.String(100))  # url 

    id_tourist_spot = db.Column(db.Integer, db.ForeignKey('tourist_spots.id'))
    tourist_spot = db.relationship('TouristSpotModel')

    def __init__(self, name, img_link, id_tourist_spot):
        self.name = name
        self.img_link = img_link
        self.id_tourist_spot = id_tourist_spot



    def json(self):
        return {
                "id"   : self.id,
                "name" : self.name,
                "img_link" : self.img_link,
                "id_tourist_spot" : id_tourist_spot
        }
    
    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()
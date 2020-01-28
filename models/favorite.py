from db import db


class FavoriteModel(db.Model):
    __tablename__= 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    id_tourist_spot = db.Column(db.Integer, db.ForeignKey('tourist_spots.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    tourist_spot = db.relationship('TouristSpotModel')
    user = db.relationship('UserModel')


    def __init__(self, id_tourist_spot, id_user):
        self.id_tourist_spot = id_tourist_spot
        self.id_user = id_user


    def json(self):
        return {
            "id"   : self.id,
            "id_tourist_spot": self.id_tourist_spot,
            "id_user": self.id_user
        }

    @classmethod
    def find_favorite_by_id_user(cls, id_user):
        return cls.query.filter_by(id_user=id_user)

    
    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()

        
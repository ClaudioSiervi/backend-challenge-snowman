from db import db


class CommentModel(db.Model):
    __tablename__= 'commentaries'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500))
    id_tourist_spot = db.Column(db.Integer, db.ForeignKey('tourist_spots.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))

    tourist_spot = db.relationship('TouristSpotModel')
    user = db.relationship('UserModel')


    def __init__(self, comment, id_tourist_spot, id_user):
        self.comment = comment
        self.id_tourist_spot = id_tourist_spot
        self.id_user = id_user


    def json(self):
        return {
            "id"   : self.id,
            "comment" : self.comment,
            "id_tourist_spot": self.id_tourist_spot,
            "id_user": self.id_user
        }

    @classmethod
    def find_comment_by_id_tourist_spot(cls, id_tourist_spot):
        return cls.query.filter_by(id_tourist_spot=id_tourist_spot)

    
    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()
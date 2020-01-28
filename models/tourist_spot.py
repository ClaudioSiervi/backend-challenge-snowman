from db import db

class TouristSpotModel(db.Model):
    __tablename__='tourist_spots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gps = db.Column(db.String(50))
    id_category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    category = db.relationship('CategoryModel')
    picture = db.relationship('PictureModel')

    def __init__(self, name, gps, id_category):
        self.name = name
        self.gps = gps
        self.id_category = id_category

    def json(self):
        return {
            "id": self.id,
            "name" : self.name,
            "gps" : self.gps,
            "id_category" : self.id_category
        }

    @classmethod
    def find_spots_by_name(cls, name):
        return cls.query.filter_by(name=name)
     
    @classmethod
    def find_spots_by_user(self, username):
        #return TouristSpotModel.query.filter_by(username=username)
        pass
    
    @classmethod
    def find_nearest_spots(self, gps):
        pass


    def save_to_db(self):   # insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        pass

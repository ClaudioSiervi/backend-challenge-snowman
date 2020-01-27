from app import app
from db import db
from resources.category import CategoryModel

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

    me = CategoryModel('Park')
    db.session.add(me)
    me = CategoryModel('Museum')
    db.session.add(me)
    me = CategoryModel('Theater')
    db.session.add(me)
    me = CategoryModel('Monument')
    #"Park", "Museum", "Theater", "Monument" 
    db.session.add(me)
    db.session.commit()
from app import app
from db import db
from resources.category import CategoryModel

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
    
    # id_user = 0 --> admin
    me = CategoryModel('Park', id_user=1)
    db.session.add(me)
    me = CategoryModel('Museum', id_user=1)
    db.session.add(me)
    me = CategoryModel('Theater', id_user=1)
    db.session.add(me)
    me = CategoryModel('Monument', id_user=1)

    db.session.add(me)
    db.session.commit()
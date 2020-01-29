from app import app
from db import db
from resources.category import CategoryModel
from resources.user import UserModel


db.init_app(app)


@app.before_first_request
def create_tables():

    db.create_all()

    try:
        # verify whether there is any registered category
        category = CategoryModel.find_category_by_id(_id=1)
        print(category.id)
    except:
        # id_user = 1 --> admin
        us = UserModel(username='claudio', password='snowlabs')
        db.session.add(us)

        me = CategoryModel('Park', id_user=1)
        db.session.add(me)
        me = CategoryModel('Museum', id_user=1)
        db.session.add(me)
        me = CategoryModel('Theater', id_user=1)
        db.session.add(me)
        me = CategoryModel('Monument', id_user=1)
        db.session.add(me)

        db.session.commit()
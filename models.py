from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# --------- App Config ---------

db = SQLAlchemy()

def config_database(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    db.create_all()
    add_init_data()
    migrate = Migrate(app, db)


def add_init_data():
    cuisine_1 = Cuisine("Arab")
    cuisine_2 = Cuisine("Chinese")
    cuisine_3 = Cuisine("Indian")

    cuisine_1.insert()
    cuisine_2.insert()
    cuisine_3.insert()

    product_1 = Product("Hummus","The standard garnish in the Middle East includes olive oil",33,1)
    product_2 = Product("Kofta", "Koftas consist of balls of ground meat - usually beef, chicken, lamb or mutton, or a mixture", 44, 1)

    product_1.insert()
    product_2.insert()



# --------- Models ---------


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(5000))
    price = db.Column(db.Integer())
    image_url = db.Column(db.String(500))
    date_created = db.Column(db.DateTime(timezone=True))
    last_updated = db.Column(db.DateTime(timezone=True))
    cuisine_id = db.Column(db.Integer())

    # model methods:

    def __init__(self, name, description, price, cuisine_id):
        self.name = name
        self.description = description
        self.price = price
        self.cuisine_id = cuisine_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format_data(self):
        return ({
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
            "cuisine_id": self.cuisine_id,
            "date_created": self.date_created,
        })



class Cuisine(db.Model):
    __tablename__ = 'cuisine'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120))

    # model methods:

    def __init__(self, name):
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format_data(self):
        return ({
            "id": self.id,
            "name": self.name,
        })

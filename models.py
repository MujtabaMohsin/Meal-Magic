from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import os

# --------- App Config ---------


db = SQLAlchemy()

database = os.getenv('SQLALCHEMY_DATABASE_URI')


def setup_db(app):
    db2 = SQLAlchemy()
    app.config.from_object('config')
    db2.app = app
    db2.init_app(app)
    migrate = Migrate(app, db2)
    db.create_all()


# --------- models ---------


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

    def _init__(self, name, description, price, cuisine_id):
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

    def __repr__(self):
        return f'<Product: id: {self.id} name: {self.name}>'


class Cuisine(db.Model):
    __tablename__ = 'cuisine'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120))

    # model methods:

    def _init__(self, name):
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

    def __repr__(self):
        return f'<Cuisine: id: {self.id} name: {self.name}>'

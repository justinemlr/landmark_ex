from app import *


class Product(db.Model):
    name = db.Column(db.String(64), primary_key=True)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer)
    updated = db.Column(db.Date)

    def __repr__(self):
        return '<Product name: {name}, Price: {price>, Stock: {stock}, Lasr pdated: {updated} \n'\
            .format(name=self.name, price=self.price, stock=self.stock, updated=self.updated)

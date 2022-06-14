from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://data.db"

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    productrel = db.relationship('ProductOrder', backref= 'product')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depo = db.Column(db.String(10), nullable=False)
    orderrel = db.relationship('ProductOrder', backref= 'order')

class ProductOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    fk_order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

if __name__=='__main__':
    app.run(debug=True, host= '0.0.0.0')
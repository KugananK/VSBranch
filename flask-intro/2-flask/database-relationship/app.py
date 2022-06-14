from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cities = db.relationship('Cities', backref='country') 

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
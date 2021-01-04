from application import db
from datetime import datetime

class Cars(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    reg = db.Column(db.String(7), nullable=False)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    colour = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    reviews = db.relationship('Reviews', backref='car', cascade='all, delete')

class Reviews(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    raiting = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.car_id'), nullable=False)
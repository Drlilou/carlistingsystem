from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price_per_day = db.Column(db.Integer, nullable=False)
    seats = db.Column(db.Integer)
    fuel = db.Column(db.String(50))
    car_type = db.Column(db.String(50))
    description = db.Column(db.Text)

    images = db.relationship('CarImage', backref='car', lazy=True)

class CarImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500), nullable=False)  # Can't be null to ensure we have an image
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)  # Ensure a car is always linked
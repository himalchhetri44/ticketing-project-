from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    bookings = db.relationship('Booking', backref='user', lazy=True)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(10), default='🎟️')
    date = db.Column(db.String(50), nullable=False)
    venue = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    total_seats = db.Column(db.Integer, default=100)
    booked_seats = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, default='')
    bookings = db.relationship('Booking', backref='event', lazy=True)

    @property
    def available(self):
        return self.booked_seats < self.total_seats

    @property
    def seats_left(self):
        return self.total_seats - self.booked_seats


class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    ticket_type = db.Column(db.String(50), default='General Admission')
    seat_preference = db.Column(db.String(50), default='No preference')
    quantity = db.Column(db.Integer, default=1)
    total_amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='confirmed')
    scanned = db.Column(db.Boolean, default=False)
    booked_at = db.Column(db.DateTime, default=datetime.utcnow)

from app import db
from app.models import User, Event, Booking
from werkzeug.security import generate_password_hash, check_password_hash
import random
import string
from datetime import datetime


# ---------- User helpers ----------

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(name, email, password):
    hashed = generate_password_hash(password)
    user = User(name=name, email=email, password=hashed)
    db.session.add(user)
    db.session.commit()
    return user

def verify_password(user, password):
    return check_password_hash(user.password, password)


# ---------- Event helpers ----------

def get_all_events():
    return Event.query.all()

def get_event_by_id(event_id):
    return Event.query.get(event_id)

def search_events(query='', category=''):
    q = Event.query
    if query:
        q = q.filter(Event.name.ilike(f'%{query}%'))
    if category:
        q = q.filter_by(category=category)
    return q.all()


# ---------- Booking helpers ----------

def generate_ticket_id():
    suffix = ''.join(random.choices(string.digits, k=6))
    return f'TKT-{suffix}'

def has_available_seats(event, quantity):
    return event.available and quantity <= event.seats_left

def create_booking(user_id, event_id, ticket_type, seat_pref, quantity, total):
    ticket_id = generate_ticket_id()
    booking = Booking(
        ticket_id=ticket_id,
        user_id=user_id,
        event_id=event_id,
        ticket_type=ticket_type,
        seat_preference=seat_pref,
        quantity=quantity,
        total_amount=total,
    )
    event = get_event_by_id(event_id)
    event.booked_seats += quantity
    db.session.add(booking)
    db.session.commit()
    return booking

def get_bookings_by_user(user_id):
    return Booking.query.filter_by(user_id=user_id).order_by(Booking.booked_at.desc()).all()

def get_booking_by_ticket_id(ticket_id):
    return Booking.query.filter_by(ticket_id=ticket_id).first()

def get_all_bookings():
    return Booking.query.order_by(Booking.booked_at.desc()).all()

def mark_ticket_scanned(ticket_id):
    booking = get_booking_by_ticket_id(ticket_id)
    if booking:
        booking.scanned = True
        db.session.commit()
    return booking


# ---------- Seed data ----------

def seed_events():
    if Event.query.count() == 0:
        events = [
            Event(name='Arijit Singh Live', category='music', icon='🎵',
                  date='Jul 12, 2026', venue='Tribhuvan Arena, KTM', price=1800,
                  total_seats=200, description='An unforgettable evening with Bollywood\'s most beloved voice.'),
            Event(name='Nepal vs India ODI', category='sport', icon='🏏',
                  date='Jul 18, 2026', venue='TU Ground, KTM', price=600,
                  total_seats=500, description='International cricket — Nepal takes on India in a thrilling ODI clash.'),
            Event(name='Kathmandu Art Fest', category='art', icon='🎨',
                  date='Jul 20, 2026', venue='Patan Museum', price=400,
                  total_seats=150, description='A celebration of contemporary and traditional Nepali art.'),
            Event(name='Street Food Carnival', category='food', icon='🍜',
                  date='Jul 25, 2026', venue='Durbar Marg', price=200,
                  total_seats=300, description='Taste the best street food from across Nepal in one place.'),
            Event(name='DJ Ritz Night', category='music', icon='🎧',
                  date='Aug 2, 2026', venue='Club Platinum', price=1200,
                  total_seats=120, booked_seats=120, description='An electrifying night with DJ Ritz. Fully booked!'),
            Event(name='Yoga & Wellness Expo', category='art', icon='🧘',
                  date='Aug 5, 2026', venue='Bhrikuti Mandap', price=300,
                  total_seats=200, description='Reconnect with your mind and body at this wellness festival.'),
        ]
        db.session.add_all(events)
        db.session.commit()
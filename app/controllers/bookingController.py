from app.repository.user_repo import (
    get_event_by_id, create_booking, get_bookings_by_user, get_booking_by_ticket_id
)
from app.controllers.authController import current_user_id
import qrcode
import io
import base64


SERVICE_FEE_RATE = 0.05


def calculate_total(price, quantity):
    subtotal = price * quantity
    fee = round(subtotal * SERVICE_FEE_RATE, 2)
    total = subtotal + fee
    return fee, total


def book_ticket(event_id, ticket_type, seat_pref, quantity):
    user_id = current_user_id()
    if not user_id:
        return False, None, 'Please log in to book tickets.'

    event = get_event_by_id(event_id)
    if not event:
        return False, None, 'Event not found.'
    if not event.available:
        return False, None, 'This event is sold out.'
    if quantity > event.seats_left:
        return False, None, f'Only {event.seats_left} seats left.'
    if quantity < 1 or quantity > 10:
        return False, None, 'Quantity must be between 1 and 10.'

    fee, total = calculate_total(event.price, quantity)
    booking = create_booking(user_id, event_id, ticket_type, seat_pref, quantity, total)
    return True, booking, 'Booking confirmed!'


def get_my_tickets():
    user_id = current_user_id()
    if not user_id:
        return []
    return get_bookings_by_user(user_id)


def generate_qr_code(ticket_id):
    qr = qrcode.QRCode(box_size=4, border=2)
    qr.add_data(ticket_id)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return base64.b64encode(buffer.getvalue()).decode()


def get_booking_detail(ticket_id):
    return get_booking_by_ticket_id(ticket_id)
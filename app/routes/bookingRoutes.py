from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.controllers.bookingController import (
    book_ticket, get_my_tickets, generate_qr_code,
    get_booking_detail, calculate_total
)
from app.controllers.authController import is_logged_in
from app.repository.user_repo import get_event_by_id

booking_bp = Blueprint('booking', __name__)


def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_logged_in():
            flash('Please log in to continue.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@booking_bp.route('/new/<int:event_id>', methods=['GET', 'POST'])
@login_required
def new(event_id):
    event = get_event_by_id(event_id)
    if not event:
        abort(404)

    if request.method == 'POST':
        ticket_type = request.form.get('ticket_type', 'General Admission')
        seat_pref = request.form.get('seat_pref', 'No preference')
        quantity = int(request.form.get('quantity', 1))
        success, booking, msg = book_ticket(event_id, ticket_type, seat_pref, quantity)
        flash(msg, 'success' if success else 'error')
        if success:
            return redirect(url_for('booking.confirm', ticket_id=booking.ticket_id))

    return render_template('booking/new.html', event=event)


@booking_bp.route('/confirm/<ticket_id>')
@login_required
def confirm(ticket_id):
    booking = get_booking_detail(ticket_id)
    if not booking:
        abort(404)
    qr_code = generate_qr_code(ticket_id)
    return render_template('booking/confirm.html', booking=booking, qr_code=qr_code)


@booking_bp.route('/my-tickets')
@login_required
def my_tickets():
    tickets = get_my_tickets()
    return render_template('booking/my_tickets.html', tickets=tickets)

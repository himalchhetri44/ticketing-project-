from app.repository.user_repo import get_booking_by_ticket_id, mark_ticket_scanned


def scan_ticket(ticket_id):
    if not ticket_id:
        return False, None, 'No ticket ID provided.'

    booking = get_booking_by_ticket_id(ticket_id.strip().upper())
    if not booking:
        return False, None, f'Ticket {ticket_id} not found.'
    if booking.scanned:
        return False, booking, 'Ticket already scanned — entry denied.'

    mark_ticket_scanned(ticket_id.strip().upper())
    return True, booking, 'Valid ticket — entry granted!'

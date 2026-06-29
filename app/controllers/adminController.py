from app.repository.user_repo import get_all_bookings, get_all_events
from app.models import User
from app import db


def get_dashboard_stats():
    bookings = get_all_bookings()
    total_sold = sum(b.quantity for b in bookings)
    total_revenue = sum(b.total_amount for b in bookings)
    total_events = len(get_all_events())
    total_users = User.query.count()
    return {
        'total_sold': total_sold,
        'total_revenue': total_revenue,
        'total_events': total_events,
        'total_users': total_users,
    }


def get_all_bookings_admin():
    return get_all_bookings()


def get_all_events_admin():
    return get_all_events()

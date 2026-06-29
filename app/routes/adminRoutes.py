from flask import Blueprint, render_template, redirect, url_for, flash
from app.controllers.adminController import get_dashboard_stats, get_all_bookings_admin, get_all_events_admin
from app.controllers.authController import is_logged_in, is_admin

admin_bp = Blueprint('admin', __name__)


def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_logged_in():
            flash('Please log in.', 'error')
            return redirect(url_for('auth.login'))
        if not is_admin():
            flash('Admin access required.', 'error')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/')
@admin_required
def dashboard():
    stats = get_dashboard_stats()
    bookings = get_all_bookings_admin()
    events = get_all_events_admin()
    return render_template('admin/dashboard.html', stats=stats, bookings=bookings, events=events)

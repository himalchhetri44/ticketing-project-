from flask import Blueprint, render_template, abort
from app.repository.user_repo import get_event_by_id

event_bp = Blueprint('event', __name__)


@event_bp.route('/<int:event_id>')
def detail(event_id):
    event = get_event_by_id(event_id)
    if not event:
        abort(404)
    return render_template('event_detail.html', event=event)

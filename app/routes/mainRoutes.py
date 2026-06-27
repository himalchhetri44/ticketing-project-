from flask import Blueprint, render_template, request
from app.controllers.mainController import get_home_events

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    query = request.args.get('q', '')
    category = request.args.get('cat', '')
    events = get_home_events(query, category)
    return render_template('index.html', events=events, query=query, category=category)

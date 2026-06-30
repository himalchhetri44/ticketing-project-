from flask import Blueprint, render_template, request
from app.controllers.scanController import scan_ticket
from app.controllers.authController import is_admin

scan_bp = Blueprint('scan', __name__)


@scan_bp.route('/', methods=['GET', 'POST'])
def scanner():
    result = None
    booking = None
    if request.method == 'POST':
        ticket_id = request.form.get('ticket_id', '').strip()
        success, booking, msg = scan_ticket(ticket_id)
        result = {'success': success, 'message': msg}
    return render_template('scan/scanner.html', result=result, booking=booking)

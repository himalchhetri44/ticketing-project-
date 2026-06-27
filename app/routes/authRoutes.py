from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.controllers.authController import register_user, login_user, logout_user, is_logged_in

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if is_logged_in():
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')
        success, msg = register_user(name, email, password, confirm)
        flash(msg, 'success' if success else 'error')
        if success:
            return redirect(url_for('main.index'))
    return render_template('auth/register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if is_logged_in():
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        success, msg = login_user(email, password)
        flash(msg, 'success' if success else 'error')
        if success:
            return redirect(url_for('main.index'))
    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))

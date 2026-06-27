from flask import session, flash
from app.repository.user_repo import get_user_by_email, create_user, verify_password


def register_user(name, email, password, confirm):
    if not name or not email or not password:
        return False, 'All fields are required.'
    if password != confirm:
        return False, 'Passwords do not match.'
    if len(password) < 6:
        return False, 'Password must be at least 6 characters.'
    if get_user_by_email(email):
        return False, 'An account with this email already exists.'
    user = create_user(name, email, password)
    session['user_id'] = user.id
    session['user_name'] = user.name
    session['is_admin'] = user.is_admin
    return True, 'Account created successfully!'


def login_user(email, password):
    if not email or not password:
        return False, 'Email and password are required.'
    user = get_user_by_email(email)
    if not user or not verify_password(user, password):
        return False, 'Invalid email or password.'
    session['user_id'] = user.id
    session['user_name'] = user.name
    session['is_admin'] = user.is_admin
    return True, f'Welcome back, {user.name}!'


def logout_user():
    session.clear()


def current_user_id():
    return session.get('user_id')


def is_logged_in():
    return 'user_id' in session


def is_admin():
    return session.get('is_admin', False)

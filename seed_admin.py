"""
Run ONCE after setting up MySQL to create the admin account:
    python seed_admin.py
"""
from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    existing = User.query.filter_by(email='admin@ticketflow.com').first()
    if not existing:
        admin = User(
            name='Admin',
            email='admin@ticketflow.com',
            password=generate_password_hash('admin123'),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print('✅ Admin created: admin@ticketflow.com / admin123')
    else:
        print('ℹ️  Admin already exists.')

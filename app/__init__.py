from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)   # loads MySQL settings from config.py

    db.init_app(app)

    # Register blueprints
    from app.routes.mainRoutes    import main_bp
    from app.routes.authRoutes    import auth_bp
    from app.routes.eventRoutes   import event_bp
    from app.routes.bookingRoutes import booking_bp
    from app.routes.adminRoutes   import admin_bp
    from app.routes.scanRoutes    import scan_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp,    url_prefix='/auth')
    app.register_blueprint(event_bp,   url_prefix='/events')
    app.register_blueprint(booking_bp, url_prefix='/booking')
    app.register_blueprint(admin_bp,   url_prefix='/admin')
    app.register_blueprint(scan_bp,    url_prefix='/scan')

    with app.app_context():
        db.create_all()                         # creates tables in MySQL
        from app.repository.user_repo import seed_events
        seed_events()

    return app

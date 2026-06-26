class Config:
    SECRET_KEY = 'ticketflow-secret-2026'

    SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://root:himal%409879@localhost:3306/ticketflow_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 280,
        'pool_pre_ping': True,
    }
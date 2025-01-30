from flask import Flask
from flask_cors import CORS
from .db import db, ma

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Load configuration
    if config_name:
        app.config.from_object(f'server.config.{config_name}')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/flask_api_app'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    CORS(app)  # Enable CORS

    db.init_app(app)  # Initialize the database with the app

    # Ensure that the db object is properly set in app.extensions
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    if 'sqlalchemy' not in app.extensions:
        app.extensions['sqlalchemy'] = {'db': db}

    ma.init_app(app)  # Initialize Marshmallow with the app

    from .blueprints import register_blueprints
    register_blueprints(app)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    return app
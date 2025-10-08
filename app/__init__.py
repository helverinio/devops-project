from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restful import Api
from app.config import Config

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    
    # Initialize API
    api = Api(app)
    
    # Register blueprints and resources
    from app.api.resources import BlacklistResource, BlacklistCheckResource
    from app.api.auth import AuthResource
    api.add_resource(AuthResource, '/auth/token')
    api.add_resource(BlacklistResource, '/blacklists')
    api.add_resource(BlacklistCheckResource, '/blacklists/<string:email>')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

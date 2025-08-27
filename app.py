from flask import Flask
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from flask_smorest import Api
from db import db
import models
import os

def create_app(db_url=None):
    app = Flask(__name__) # Creates Flask application instance, name must be the same as file name

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Flask Example API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db") # if not set, use SQLite
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app) # Initialize SQLAlchemy with the Flask app
    
    api = Api(app)
    
    with app.app_context():
        db.create_all()
        
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(ItemBlueprint)
    
    return app

# Expose app for Flask CLI
app = create_app()
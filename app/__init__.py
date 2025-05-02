from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # Ensures app uses config

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app

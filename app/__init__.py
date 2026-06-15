from flask import Flask
from dotenv import load_dotenv

load_dotenv()

from app.config import Config
from app.extensions import (
    db,
    bcrypt,
    login_manager,
    migrate
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    return app
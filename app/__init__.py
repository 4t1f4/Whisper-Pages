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


    from app.auth import auth_bp
    from app.diary import diary_bp
    from app.profile import profile_bp
    
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(diary_bp)
    app.register_blueprint(profile_bp)



    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    return app
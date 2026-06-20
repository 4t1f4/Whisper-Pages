from flask import Flask, render_template, redirect, url_for, flash
from flask_login import current_user
from dotenv import load_dotenv

load_dotenv()

from app.config import Config
from app.extensions import (
    db,
    bcrypt,
    login_manager,
    migrate
)

from app.models import User, Entry


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Flask-Login Configuration
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # Register Blueprints
    from app.auth import auth_bp
    from app.diary import diary_bp
    from app.profile import profile_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(diary_bp)
    app.register_blueprint(profile_bp)


    @app.route("/")
    @app.route("/index")
    def index():
        
        if current_user.is_authenticated:
            flash("Please log out to go to homepage.")
            return redirect(url_for("profile.profile"))
        
        return render_template("index.html")

    return app
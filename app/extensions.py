from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()

bcrypt = Bcrypt()

login_manager = LoginManager()

migrate = Migrate()


login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"
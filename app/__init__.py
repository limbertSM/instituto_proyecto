from flask import Flask
from .config import Config
from .models.usuario import db
from flask_login import LoginManager
from .auth import auth_bp

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(auth_bp)

    return app

from .models.usuario import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

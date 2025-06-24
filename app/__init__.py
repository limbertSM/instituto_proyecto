from flask import Flask
from flask_login import LoginManager
from .config import Config
from .models.usuario import db, Usuario

# Inicializar LoginManager afuera para evitar problemas circulares
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Endpoint para login (con blueprint auth)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)

    # Importar blueprints dentro de la función para evitar importaciones circulares
    from .auth import auth_bp
    from .admin import admin_bp
    from .docente import docente_bp
    from .estudiante import estudiante_bp

    # Registrar blueprints con prefijos URL para organizar rutas
    app.register_blueprint(auth_bp)              # sin prefijo para rutas como /login, /register, etc.
    app.register_blueprint(admin_bp)
    app.register_blueprint(docente_bp, url_prefix='/docente')
    app.register_blueprint(estudiante_bp, url_prefix='/estudiante')

    # Opcional: imprimir rutas para depurar
    # for rule in app.url_map.iter_rules():
    #     print(f"{rule.endpoint}: {rule}")

    return app

# Función para cargar usuario - necesario para Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

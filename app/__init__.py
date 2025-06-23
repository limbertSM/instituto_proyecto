from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    mysql.init_app(app)

    # Importar e registrar los Blueprints
    from .auth import routes as auth_routes
    app.register_blueprint(auth_routes.bp)

    return app

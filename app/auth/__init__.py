from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates')

from . import routes  # Esto importa tus rutas y las conecta con el Blueprint

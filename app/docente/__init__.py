from flask import Blueprint

docente_bp = Blueprint('docente', __name__, template_folder='templates')

from . import routes

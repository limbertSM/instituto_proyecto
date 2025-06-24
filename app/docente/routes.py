from flask import Blueprint, render_template
from flask_login import login_required
from . import docente_bp  # Importa el blueprint ya definido
#from ..models.docente import Docente
from flask_login import current_user



@docente_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('docente/dashboard.html')


"""@docente_bp.route('/docente')
@login_required
def cursos_docente():
    docente = Docente.query.filter_by(usuario_id=current_user.id).first()
    if not docente:
        flash("No se encontró información del docente.", "danger")
        return redirect(url_for('auth.home'))

    grupos = Grupo.query.filter_by(docente_id=docente.id).all()

    return render_template('docente/crud_docente.html', grupos=grupos)"""
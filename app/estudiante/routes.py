from flask import Blueprint, render_template
from flask_login import login_required
from . import estudiante_bp

# Asegúrate de nombrar esto exactamente así:

@estudiante_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('estudiante/dashboard.html')

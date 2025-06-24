from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth_bp
from .forms import LoginForm
from ..models.usuario import Usuario
from werkzeug.security import check_password_hash

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(correo=form.correo.data).first()
        if usuario and check_password_hash(usuario.contraseña, form.contraseña.data):
            login_user(usuario)
            # Redirección según rol
            if usuario.rol.nombre == 'admin':
                return redirect(url_for('admin.dashboard'))
            elif usuario.rol.nombre == 'docente':
                return redirect(url_for('docente.dashboard'))
            elif usuario.rol.nombre == 'estudiante':
                return redirect(url_for('estudiante.dashboard'))
        else:
            flash('Correo o contraseña incorrectos', 'danger')
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

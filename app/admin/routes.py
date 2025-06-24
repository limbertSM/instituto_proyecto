from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from . import admin_bp  # Importa el blueprint ya definido
from ..models.usuario import db, Usuario



"""# 🔧 Declarar primero el blueprint
admin_bp = Blueprint('admin', __name__, template_folder='templates')
"""
# ✅ Registrar la ruta con el blueprint
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')


@admin_bp.route('/crud')
@login_required
def crud_admin():
    usuarios = Usuario.query.all()
    return render_template('admin/crud_admin.html', usuarios=usuarios)

@admin_bp.route('/listar')
@login_required
def listar_admin():
    usuarios = Usuario.query.all()
    return render_template('admin/listar_admin.html', usuarios=usuarios)


@admin_bp.route('/usuarios')
@login_required
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('admin/listar_admin.html', usuarios=usuarios)

@admin_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        rol_id = int(request.form['rol'].split()[0])  # ✅ ya es un número
        contraseña = request.form['contraseña']

        # 👇 Asegúrate que Usuario tenga campo rol_id, no rol (si estás usando claves foráneas)
        nuevo = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            contraseña=contraseña,
            rol_id=rol_id  # ✅ guarda el número, no un objeto ni string
        )

        db.session.add(nuevo)
        db.session.commit()
        flash('✅ Usuario creado con éxito', 'success')
        return redirect(url_for('admin.listar_admin'))

    return render_template('admin/nuevo_usuario.html')

@admin_bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.apellido = request.form['apellido']
        usuario.correo = request.form['correo']
        usuario.rol_id = int(request.form['rol'])
        db.session.commit()
        flash('Usuario actualizado con éxito', 'success')
        return redirect(url_for('admin.listar_admin'))
    return render_template('admin/editar_usuario.html', usuario=usuario)

@admin_bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
@login_required
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado con éxito', 'success')
    return redirect(url_for('admin.listar_admin'))

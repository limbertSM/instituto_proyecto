"""from app import db
from sqlalchemy.orm import relationship

class Docente(db.Model):
    __tablename__ = 'docentes'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    titulo = db.Column(db.String(100), nullable=True)  # Ej: Lic., M.Sc., etc.
    especialidad = db.Column(db.String(100), nullable=True)

    usuario = relationship('Usuario', backref='docente', uselist=False)"""


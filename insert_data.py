import MySQLdb

# Conexión a la BD
conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="instituto_sis"
)
cursor = conn.cursor()

# Insertar roles
cursor.execute("INSERT INTO roles (nombre) VALUES ('admin'), ('docente'), ('estudiante')")

# Insertar usuarios
cursor.execute("INSERT INTO usuarios (nombre, apellido, correo, contraseña, rol_id) VALUES "
               "('Juan', 'Pérez', 'juan@correo.com', '123456', 1),"
               "('Laura', 'Gómez', 'laura@correo.com', '123456', 2),"
               "('Carlos', 'Rojas', 'carlos@correo.com', '123456', 3)")

# Insertar carreras
cursor.execute("INSERT INTO carreras (nombre, descripcion) VALUES "
               "('Ingeniería de Sistemas', 'Carrera tecnológica'),"
               "('Administración', 'Carrera empresarial')")

# Insertar materias
cursor.execute("INSERT INTO materias (nombre, descripcion, carrera_id) VALUES "
               "('Programación I', 'Fundamentos de programación', 1),"
               "('Matemática I', 'Matemáticas básicas', 1)")

# Insertar cursos
cursor.execute("INSERT INTO cursos (materia_id, docente_id, periodo) VALUES "
               "(1, 2, '2025-I'),"
               "(2, 2, '2025-I')")

# Insertar estudiantes
cursor.execute("INSERT INTO estudiantes (usuario_id, carrera_id, semestre) VALUES "
               "(3, 1, 1)")

# Insertar inscripciones
cursor.execute("INSERT INTO inscripciones (estudiante_id, curso_id) VALUES "
               "(1, 1),"
               "(1, 2)")

# Insertar calificaciones
cursor.execute("INSERT INTO calificaciones (inscripcion_id, nota, observaciones) VALUES "
               "(1, 85.5, 'Buen rendimiento'),"
               "(2, 90, 'Excelente')")

# Insertar horarios
cursor.execute("INSERT INTO horarios (curso_id, dia_semana, hora_inicio, hora_fin, aula) VALUES "
               "(1, 'Lunes', '08:00:00', '10:00:00', 'Aula 101'),"
               "(2, 'Martes', '10:00:00', '12:00:00', 'Aula 102')")

# Insertar noticias
cursor.execute("INSERT INTO noticias (titulo, contenido, autor_id) VALUES "
               "('Inicio de clases', 'El semestre comienza el 1 de agosto.', 1)")

conn.commit()
cursor.close()
conn.close()

print("✔️ Datos insertados correctamente.")

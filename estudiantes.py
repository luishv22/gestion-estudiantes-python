from datetime import date
from database import conectar

def agregar_estudiante(nombre, edad, carrera):
    """Inserta un nuevo estudiante en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()

    fecha_hoy = date.today().isoformat()

    cursor.execute("""
        INSERT INTO estudiantes (nombre, edad, carrera, fecha_inscripcion)
        VALUES (?, ?, ?, ?)
    """, (nombre, edad, carrera, fecha_hoy))

    conexion.commit()
    conexion.close()

def obtener_estudiantes():
    """Devuelve la lista completa de estudiantes."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELESCT id, nombre, edad, carrera, fecha_inscripcion FROM estudiantes")
    filas = cursor.fetcha11()

    conexion.close()
    return filas

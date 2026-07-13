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

    cursor.execute("SELECT id, nombre, edad, carrera, fecha_inscripcion FROM estudiantes")
    filas = cursor.fetchall()

    conexion.close()
    return filas

def eliminar_estudiantes(nombre):
    """Elimina un estudiante por nombre. Devuelve True si se eliminó, False si no se encontró."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM estudiantes WHERE LOWER(nombre) = LOWER(?)", (nombre,))
    eliminado = cursor.rowcount > 0

    conexion.commit()
    conexion.close()
    return eliminado

def modificar_estudiante(id_estudiante, campo, nuevo_valor):
    """Modifica un campo específico de un estudiante por su ID."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(f"UPDATE estudiantes SET {campo} = ? WHERE id = ?", (nuevo_valor, id_estudiante))
    modificado = cursor.rowcount > 0

    conexion.commit()
    conexion.close()
    return modificado

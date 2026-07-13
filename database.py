import sqlite3

NOMBRE_D8 = "Estudiantes.db"

def conectar():
    """Crea y duevuelve una conexión a la base de datos."""
    return sqlite3.connect(NOMBRE_D8)

def crear_tabla():
    """Crea la tabla de estudiantes si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            carrera TEXT NOT NULL,
            fecha_inscripcion TEXT NOT NULL
        )
""")

    conexion.commit()
    conexion.close()

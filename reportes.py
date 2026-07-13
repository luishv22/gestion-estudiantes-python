from database import conectar

def total_estudiantes():
    """Devuelve el número total de estudiantes registrados."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM estudiantes")
    total = cursor.fetchone()[0]

    conexion.close()
    return total

def promedio_edad():
    """Devuelve el promedio de edad de todos los estudiantes."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT AVG(edad) FROM estudiantes")
    promedio = cursor.fetchone()[0]

    conexion.close()
    return promedio

def estudiante_mayor():
    """Devuelve el estudiante con mayor edad."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, edad FROM estudiantes ORDER BY edad DESC LIMIT 1")
    resultado = cursor.fetchone()

    conexion.close()
    return resultado

def estudiante_menor():
    """Devuelve el estudiante con menor edad."""
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre, edad FROM estudiantes ORDER BY edad ASC LIMIT 1")
    resultado = cursor.fetchone()

    conexion.close()
    return resultado
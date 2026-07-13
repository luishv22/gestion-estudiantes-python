from database import crear_tabla
from estudiantes import (
    agregar_estudiante,
    obtener_estudiantes,
    eliminar_estudiante,
    modificar_estudiante,
    buscar_por_carrera,
)
from reportes import total_estudiantes, promedio_edad, estudiante_mayor, estudiante_menor

def mostrar_lista():
    """Muestra todos los estudiantes registrados."""
    estudiantes = obtener_estudiantes()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    for est in estudiantes:
        id_est, nombre, edad, carrera, fecha = est
        print(f"ID: {id_est} | Nombre: {nombre}, Edad: {edad}, Carrera: {carrera}, Inscrito: {fecha}")

def solicitar_nuevo_estudiante():
    """Pide los datos al usuario y agrega un estudiante."""
    try:
        print("\n--- Ingrese los datos del estudiante que desea guardar ---")
        nombre = input("Ingrese el nombre: ").strip()
        edad = int(input("Ingrese la edad: "))  
        carrera = input("Ingrese la carrera: ")

        agregar_estudiante(nombre, edad, carrera)
        print("Estudiante agregado correctamente")
    except ValueError:
        print("Entrada inválida, intenta de nuevo")


def solicitar_eliminar_estudiante():
    """Pide el nombre y elimina al estudiante correspondiente."""
    nombre = input("Ingrese el nombre del estudiante que quiere eliminar: ").strip()
    if eliminar_estudiante(nombre):
        print("Estudiante eliminado")
    else:
        print("Estudiante no encontrado")


def solicitar_modificar_estudiante():
    """Pide el ID y el campo a modificar."""
    mostrar_lista()
    try:
        id_estudiante = int(input("\nIngrese el ID del estudiante que quiere modificar: "))
    except ValueError:
        print("ID inválido")
        return

    print("¿Qué deseas modificar?")
    print("1. Nombre")
    print("2. Edad")
    print("3. Carrera")
    opcion_mod = input("Elija una opción: ")

    campos = {"1": "nombre", "2": "edad", "3": "carrera"}
    campo = campos.get(opcion_mod)

    if not campo:
        print("Opción inválida, intenta de nuevo")
        return

    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")

    if campo == "edad":
        try:
            nuevo_valor = int(nuevo_valor)
        except ValueError:
            print("Edad inválida")
            return

    if modificar_estudiante(id_estudiante, campo, nuevo_valor):
        print("Cambios realizados correctamente")
    else:
        print("Estudiante no encontrado")


def solicitar_busqueda_carrera():
    """Pide una carrera y muestra los estudiantes encontrados."""
    carrera = input("Ingresa la carrera: ")
    resultados = buscar_por_carrera(carrera)

    if not resultados:
        print("No se encontró la carrera")
        return

    print("\n--- Estudiantes registrados ---")
    for nombre, edad in resultados:
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")


def mostrar_reporte():
    """Muestra el reporte general de estudiantes."""
    total = total_estudiantes()
    if total == 0:
        print("No hay estudiantes registrados para generar un reporte.")
        return

    print("\n=== Reporte de estudiantes ===")
    print(f"Total de estudiantes: {total}")
    print(f"Promedio de edad: {promedio_edad():.2f}")

    mayor_nombre, mayor_edad = estudiante_mayor()
    menor_nombre, menor_edad = estudiante_menor()

    print(f"Estudiante mayor: {mayor_nombre} ({mayor_edad} años)")
    print(f"Estudiante menor: {menor_nombre} ({menor_edad} años)")


def menu_principal():
    crear_tabla()

    while True:
        print("\n--- Gestión de estudiantes ---")
        print("1. Mostrar todos los estudiantes")
        print("2. Agregar un estudiante")
        print("3. Eliminar un estudiante por nombre")
        print("4. Modificar un estudiante")
        print("5. Buscar por carrera")
        print("6. Reporte de estudiantes")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- Lista de estudiantes ---")
            mostrar_lista()
        elif opcion == "2":
            solicitar_nuevo_estudiante()
        elif opcion == "3":
            solicitar_eliminar_estudiante()
        elif opcion == "4":
            solicitar_modificar_estudiante()
        elif opcion == "5":
            solicitar_busqueda_carrera()
        elif opcion == "6":
            mostrar_reporte()
        elif opcion == "7":
            print("Saliendo del programa. . . .")
            break
        else:
            print("Opción inválida, intenta de nuevo")


menu_principal()
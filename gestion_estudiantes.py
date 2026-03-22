import json
# Función para cargar datos de archivo
def cargar_estudiantes():
    # Verificar si ya hay un archivo guardado para cargarlo
    try:
        with open("estudiantes.json", "r") as archivo:
            return json.load(archivo)

    # Si no existe ningún archivo guarda uno nuevo       
    except FileNotFoundError:
        return []

# Función para guardar estudiantes
def guardar_estudiantes(estudiantes):
    # Guardar datos en archivo JSON
    with open("estudiantes.json", "w") as archivo:
        json.dump(estudiantes, archivo, indent=4)

# Función para mostrar la lista de estudiantes
def mostrar_lista(estudiantes):
    for estudiante in estudiantes: 
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Carrera: {estudiante['carrera']}")

# Función para agregar estudiante
def agregar_estudiante(estudiantes):
    # Verificar que los datos ingresados sean los correctos
    try:
        print("\n--- Ingrese los datos del estudiante que desea guardar ---")
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        carrera =input("Ingrese la carrera: ")
                    
        # Guardar los datos en un nuevo diccionario
        estudiantes.append({
            "nombre": nombre, 
            "edad": edad, 
            "carrera": carrera
            })
        
        # Guadar los datos del estudiante al archivo
        guardar_estudiantes(estudiantes)
        print("Estudiante agregado correctamente")
        
    except ValueError:
        print("Entrada inválida, intenta de nuevo")

# Función para eliminar estudiante
def eliminar_estudiante(estudiantes):
    eliminar = input("Ingrese el nombre del estudiante que quiere eliminar: ")
    encontrado = False
    # Buscar al estudiante por nombre
    for estudiante in estudiantes[:]:
        if estudiante["nombre"].lower() == eliminar.lower():
            # Eliminar al estudiante encontrado
            estudiantes.remove(estudiante)
            encontrado = True
            print("Estudiante eliminado")
            # Guarda la lista actualizada
            guardar_estudiantes(estudiantes)
            break

    if not encontrado:
        print("Estudiante no encontrado")

# Función para modificar estudiante
def modificar_estudiante(estudiantes):
    modificar = input("Ingrese el nombre del estudiante que quiere modificar: ")
    encontrado = False
    # Buscar al estudiante por nombre
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == modificar.lower():
            encontrado = True
            # Menú para modificar los datos del estudiante encontrado
            print("¿Que deseas modificar?: ")
            print("1. Nombre")
            print("2. Edad")
            print("3. Carrera")
            # Solicitar opción 
            opcion_mod = input("Elija una opción: ")

            # Opción 1: Modificar nombre
            if opcion_mod == "1":
                nuevo = input("Ingrese el nuevo nombre: ")
                # Aplicar la modificación de nombre
                estudiante["nombre"] = nuevo

            # Opción 2: Modificar edad
            elif opcion_mod == "2":
                # Verificar que se ingrese el dato solicitado
                try:
                    nuevo = int(input("Ingrese la nueva edad: "))
                    # Aplicar la modificación de edad
                    estudiante["edad"] = nuevo
                except ValueError:
                    print("Edad inválida")
                    break

            # Opción 3: Modificar carrera
            elif opcion_mod == "3":
                nuevo = input("Ingrese la nueva carrera: ")
                # Aplicar la modificación de carrera
                estudiante["carrera"] = nuevo

            else:
                print("Opción inválida, intenta de nuevo")
                break

            # Guardar el archivo con los datos del estudiante modificado
            guardar_estudiantes(estudiantes)
            print("Cambios realizados correctamente")
            break
            
    if not encontrado:
                print("Estudiante no encontrado")

# Función para buscar estudiante por carrera
def buscar_por_carrera(estudiantes):
    buscar_carrera = input("Ingresa la carrera: ")
    encontrado = False
    # Buscar carrera
    for estudiante in estudiantes:
        if estudiante["carrera"].lower() == buscar_carrera.lower():
            # Mostrar los datos de los estudiantes registrados 
            if not encontrado:
                print("\n--- Estudiantes registrados ---")
            print(f"Nombre: {estudiante['nombre']}")
            print(f"Edad: {estudiante['edad']}")
            encontrado = True
                  
    if not encontrado:
        print("No se encontro la carrera")

# Función reporte de estudiante
def reporte_estudiantes(estudiantes):
    # Función para mostrar la cantidad de estudiantes
    def total_estudiantes(estudiantes):
        return len(estudiantes)
    # Función para mostrar el promedio de edad
    def promedio_edad(estudiantes):
        return sum(estudiante['edad'] for estudiante in estudiantes) / len(estudiantes)
    
    print("\n=== Reporte de estudiantes ===")
    print(f"Total de estudiantes: {total_estudiantes(estudiantes)}")
    print(f"Promedio de edad:  {promedio_edad(estudiantes):.2f}")
    
    # Mostrar al estudiante mayor y menor
    mayor = max(estudiantes, key=lambda e: e['edad'])
    menor = min(estudiantes, key=lambda e: e['edad'])

    print(f"Estudiante mayor: {mayor['nombre']} ({mayor['edad']} años)")
    print(f"Estudiante menor: {menor['nombre']} ({menor['edad']} años)")

# Menú principal de programa
def menu_principal():
    estudiantes = cargar_estudiantes()

    if not estudiantes:
        estudiantes = [
            {
                "nombre": "Axel",
                "edad": 25,
                "carrera": "Ingenieria Industrial"
            },
            {
                "nombre": "Daniel",
                "edad": 23,
                "carrera": "Ingenieria en Software"
            },
            {
                "nombre": "Berenice",
                "edad": 19,
                "carrera": "Licenciatura en Gastronomia"
            },
            {
                "nombre": "Julio",
                "edad": 20,
                "carrera": "Ingenieria Civil"
            }
        ]
        guardar_estudiantes(estudiantes)
    # Bucle principal del menú
    while True:
        print("\n--- Gestión de estudiantes ---")
        print("1. Mostrar todos los estudiantes")
        print("2. Agregar un estudiante")
        print("3. Eliminar un estudiante por nombre")
        print("4. Modificar un estudiante")
        print("5. Buscar por carrera")
        print("6. Reporte de estudiantes")
        print("7. Salir")
        # Solicitar opción
        opcion = input("Elige una opción: ")

        # Opción 1: Mostrar lista de estudiantes
        if opcion == "1":
            print("\n--- Lista de estudiantes ---")
            mostrar_lista(estudiantes)

        # Opción 2: Agregar un estudiante nuevo        
        elif opcion == "2":
            agregar_estudiante(estudiantes)
            
        # Opción 3: Eliminar estudiante
        elif opcion == "3":
            eliminar_estudiante(estudiantes)

        # Opción 4: Modificar estudiante
        elif opcion == "4":
            modificar_estudiante(estudiantes)

        # Opción 5: Buscar por carrera
        elif opcion == "5":
            buscar_por_carrera(estudiantes)

        # Opción 6: Reporte de estudiantes
        elif opcion == "6":
            reporte_estudiantes(estudiantes)

        # Opción 7: Salir del programa
        elif opcion == "7":
            print("Saliendo del programa. . . .")
            break

        else:
            print("Opción inválida, intenta de nuevo")
# Llamar a la función principal
menu_principal()

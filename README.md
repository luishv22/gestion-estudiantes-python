# Gestión de estudiantes en Python

Programa en consola hecho en Python para guardar y administrar estudiantes, usando una base de datos SQLite y una arquitectura modular.

Originalmente usaba un archivo JSON para persistencia; fue migrado a SQLite como práctica de bases de datos y buenas prácticas de organización de código.

## Funciones

* Agregar estudiantes (con ID único y fecha de inscripción automática)
* Mostrar lista completa
* Modificar datos por ID
* Eliminar estudiantes por nombre
* Buscar por carrera
* Ver un reporte con total de estudiantes, promedio de edad, estudiante mayor y menor

## Tecnologías utilizadas

* Python
* SQLite3

## Estructura del proyecto

```
gestion-estudiantes-python/
├── database.py      # Conexión y creación de la tabla en SQLite
├── estudiantes.py    # Lógica CRUD (agregar, obtener, eliminar, modificar, buscar)
├── reportes.py         # Estadísticas usando funciones agregadas de SQL
├── main.py              # Menú interactivo (punto de entrada del programa)
└── README.md
```

El proyecto separa la lógica de negocio (`estudiantes.py`, `reportes.py`, `database.py`) de la interfaz de usuario (`main.py`), facilitando su mantenimiento y reutilización.

## Cómo ejecutar

```bash
python main.py
```

La base de datos (`estudiantes.db`) se crea automáticamente en la primera ejecución.

## Ejemplo de uso

```text
--- Gestión de estudiantes ---
1. Mostrar todos los estudiantes
2. Agregar un estudiante
3. Eliminar un estudiante por nombre
4. Modificar un estudiante
5. Buscar por carrera
6. Reporte de estudiantes
7. Salir
Elige una opción: 6

=== Reporte de estudiantes ===
Total de estudiantes: 3
Promedio de edad: 23.67
Estudiante mayor: Carlos (27 años)
Estudiante menor: Maria (20 años)
```

## Seguridad

Todas las consultas SQL usan parámetros (`?`) en lugar de concatenar texto directamente, para prevenir inyección SQL.

## Objetivo del proyecto

Practicar conceptos de bases de datos y buenas prácticas de desarrollo:

* Persistencia de datos con SQLite
* Consultas SQL (INSERT, SELECT, UPDATE, DELETE, funciones agregadas)
* Arquitectura modular (separación de responsabilidades)
* Prevención de inyección SQL con consultas parametrizadas
* Manejo de excepciones
* Control de versiones con Git: ramas, commits organizados y Pull Requests

## Nota

Lo hice como práctica para mejorar mi lógica, el manejo de bases de datos en Python, y el flujo de trabajo profesional con Git y GitHub.

## Autor

Luis Hernández
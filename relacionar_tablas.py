'''Para este ejemplo vamos a relacionar dos tablas.
La tabla Telefono tiene un atributo que indica la clave primaria del registro con el
que esta relacionado de la tabla Fabricante, la clave foranea'''

# Importamos la libreria SQLite3
import sqlite3

# Hacemos la conexion a la base de datos Telefonos.db
database = sqlite3.connect('Telefonos.db')

# Creamos el cursor para interactuar con la base de datos.
cursor = database.cursor()

# Ejecutamos una consulta SQL para seleccionar todos los registros de la tabla Fabricante.
cursor.execute("select * from Fabricante")

# Iteramos sobre los resultados de la consulta a la tabla Fabricante.
for registro in cursor:
        # registro[1] se refiere al nombre del fabricante (suponiendo que es la segunda columna de la tabla).
    print(f"Mostrando todos los teléfonos del fabricante {registro[1]}") 
    
    # Creamos otro cursor para trabajar con la tabla Telefono                                                             
    cursortelefonos = database.cursor()

    # Preparamos un parámetro para la consulta. registro[0] se refiere al ID del fabricante (suponiendo que es la primera columna de la tabla).
    parametro = (registro[0],)

    # Ejecutamos una consulta SQL para seleccionar ciertos campos de la tabla Telefono donde FabricanteId coincide con el ID del fabricante actual.
    # Esta consulta devolvera los valores de las columnas especificadas
    cursortelefonos.execute("select NombreModelo, Capacidad, MemoriaRAM, CamaraMPixeles, VersionSO from Telefono where FabricanteId = ?", parametro)

    # Iteramos sobre los resultados de la consulta a la tabla Telefono.
    for registrotelefono in cursortelefonos:

        # Imprimimos los detalles del teléfono. Cada campo se corresponde con una columna seleccionada en la consulta SQL.
        print(f"{registrotelefono[0]}, {registrotelefono[1]}, {registrotelefono[2]}, {registrotelefono[3]}, {registrotelefono[4]}")

# Cerramos la conexión a la base de datos para liberar los recursos.
cursor.close()
database.close()



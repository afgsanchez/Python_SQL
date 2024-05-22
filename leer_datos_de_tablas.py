# Importamos la libreria SQLite3
import sqlite3

# Hacemos la conexion a la base de datos Telefonos.db
database = sqlite3.connect('Telefonos.db')

# Creamos el cursor para interactual con la base de datos.
cursor = database.cursor()

# Cargamos la consulta SQL al cursor y este la ejecuta
# Le pedimos que nos muestre los registros de la tabla Fabricante que en la 
# columna Nombre tengan el valor Apple.
cursor.execute("SELECT * FROM Fabricante WHERE Nombre = 'Apple'")
print()
# Los datos de a consulta ahora estan en la variable cursos. Los leemos con un bucle for
for registro in cursor:
    print(registro)
print()
# Ahora le vamos a pedir que nos devuelva todos los registros de la tabla Fabricante.
cursor.execute("select * from Fabricante")
for registro in cursor:
    print(registro)
print()
print("###############################################")
print()

# Ahora vamos a mostrar todos lo datos de la tabla Telefono
cursor.execute("select * from Telefono")
for registro in cursor:
    print(registro)
print()

# Cerramos la base de datos
database.close()

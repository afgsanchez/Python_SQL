import sqlite3
# Hacemos la conexion a la base de datos Telefonos.db
database = sqlite3.connect('Telefonos.db')

# Creamos el cursor para interactuar con la base de datos.
cursor = database.cursor()

# Obtenemos la estructura de la tabla Telefono
cursor.execute("PRAGMA table_info(Telefono)")

# Imprimimos la estructura de la tabla
print("Estructura de la tabla Telefono:")
for column in cursor.fetchall():
    print(column)

database.close()

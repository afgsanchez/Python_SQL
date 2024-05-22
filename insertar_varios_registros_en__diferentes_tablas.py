# Importamos la libreria SQLite3
import sqlite3

# Hacemos la conexion a la base de datos Telefonos.db
database = sqlite3.connect('Telefonos.db')

# Preparamos los datos del registro que vamos a insertar en la Tabla Fabricante
fabricante = (2, 'Xiaomi', '666423859', 'Centro Comercia La Gavina, planta 2, local 34, Valencia', 'tienda@xiaomi.es')
# Lo mostramos en pantalla
print("Fabfricante a instertar: ", fabricante)

# Inciamos un cursor() para que nos haga la insercion de datos en la base de datos
# que tenemos en la variable database.
cursor = database.cursor()

# Le indicamos al cursor que ejecute la sentencia SQL para insertar los datos de la 
# variable fabricante en la tabla que tenemos en la variable cursor.
# Sentencia SQL parametrizada para insertar datos en la tabla Fabricante
# Los '?' son marcadores de posición que serán reemplazados por los valores de la tupla fabricante
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", fabricante), esto evita inyeccion SQL

# Hacemos un commit para confirmar que se graben los datos en la base de datos
database.commit()
# Imprimimos una confirmacion
print("Fabricante insertado!")


# Preparamos los datos para insertar en la misma base de datos pero
# en la tabla Telefono
telefono1 = (1, 1, 'iPhone 12', 128, 4, 20, 'iOS 14')
print("Telefono a insertar: ", telefono1)
telefono2 = (2, 1, 'iPhone XR', 512, 6, 30, 'iOS 14')
print("Telefono a insertar: ", telefono2)
telefono3 = (3, 2, 'Red Mi Note 9', 128, 4, 20, 'Android 9')
print("Telefono a insertar: ", telefono3)
telefono4 = (4, 2, 'Mi 9se', 128, 6, 48, 'Android 11')
print("Telefono a insertar: ", telefono4)

# Configuramos los cursores con las sentencias SQL, uno para cada registro a insertar
cursor.execute("INSERT INTO Telefono VALUES(?,?,?,?,?,?,?)", telefono1)
cursor.execute("INSERT INTO Telefono VALUES(?,?,?,?,?,?,?)", telefono2)
cursor.execute("INSERT INTO Telefono VALUES(?,?,?,?,?,?,?)", telefono3)
cursor.execute("INSERT INTO Telefono VALUES(?,?,?,?,?,?,?)", telefono4)

# Hacemos el commit para confirmar los cambios en la base de datos
database.commit()
print("Telefonos insertados!")
print()

# Cerramos el cursor() para liberar recursos.
cursor.close()
# Cerramos la conexion con la base de datos
database.close()

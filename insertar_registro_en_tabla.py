# Importamos la libreria SQLite3
import sqlite3

# Hacemos la conexion a la base de datos Telefonos.db
database = sqlite3.connect('Telefonos.db')

# Preparamos los datos del registro que vamos a insertar en la Tabla Fabricante
fabricante = (1, 'Apple', '654321987', 'Puerta del Sol 1, Madrid', 'info@apple.es')
# Lo mostramos en pantalla
print("Registro a instertar: ", fabricante)

# Inciamos un cursor() para que nos haga la insercion de datos en la base de datos
# que tenemos en la variable database.
cursor = database.cursor()

# Le indicamos al cursor que ejecute la sentencia SQL para insertar los datos de la 
# variable fabricante en la tabla que tenemos en la variable cursor.
# Sentencia SQL parametrizada para insertar datos en la tabla Fabricante
# Los '?' son marcadores de posición que serán reemplazados por los valores de la tupla fabricante
cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", fabricante)

# Hacemos un commit para confirmar que se graben los datos en la base de datos
database.commit()
# Imprimimos una confirmacion
print("Registro insertado!")

# Cerramos el cursor() para liberar recursos.
cursor.close()

# Cerramos la conexion con la base de datos
database.close()

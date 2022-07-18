import mysql.connector
import crudfunctions.functions as crud


conection = mysql.connector.connect(
host='localhost',
user='root',
password='',
database='bullshit'
)

cursor = conection.cursor()

# CRUD

# CREATE

#### crud.create(cursor, conection)

# READ

#### crud.select(cursor)

# UPDATE

crud.update(cursor, conection)

# DELETE
cursor.close()
conection.close()
  
# resultado = cursor.fetchall() # read database







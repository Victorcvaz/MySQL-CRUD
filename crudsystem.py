import mysql.connector
import crudfunctions.functions as crud


conection = mysql.connector.connect(
host='localhost',
user='root',
password='',
database='bullshit'
)

cursor = conection.cursor()

# SQL comands #

# Init #

while True:
    init = crud.init()
    if init == 0:
        print("\033[1;32mCheck back often!\033[m")
        break
# CREATE

    if init == 1:
        crud.create(cursor, conection)

# READ
    if init == 2:
        crud.select(cursor)

# UPDATE
    if init == 3:
        crud.update(cursor, conection)

# DELETE
    if init == 4:
        crud.delete(cursor, conection)

# Ending #
cursor.close()
conection.close()
  
# resultado = cursor.fetchall() # read database







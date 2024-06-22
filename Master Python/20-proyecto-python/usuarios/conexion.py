# Es mejor guardar la base de datos en un modulo
import mysql.connector


def conectar():

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306
    )

    #print(database)


    # Cursor para hacer las CONSULTAS

    cursor = database.cursor(buffered=True)

    return [database,cursor]
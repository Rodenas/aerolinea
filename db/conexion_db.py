import mysql.connector

# devuelve la conexion de la base de datos
def get_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_aerolinea"
    )
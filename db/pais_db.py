from db.conexion_db import get_conexion;

# lista todos los paises
def pais_listar():
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta para obtener todos los paises
    cursor.execute(f"SELECT * FROM pais;")

    # obtiene el resultado
    resultado = cursor.fetchall()
    
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return resultado
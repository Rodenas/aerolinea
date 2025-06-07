from db.conexion_db import get_conexion;

# lista todos los ciudades
def ciudad_listar_por_pais(pais: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta para obtener todas las ciudades
    cursor.execute(f"SELECT id_ciudad, ciudad FROM ciudad WHERE id_pais = {pais};")

    # obtiene el resultado
    resultado = cursor.fetchall()
    
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return resultado
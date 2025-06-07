from db.conexion_db import get_conexion;

# comprobar si el destino existe
def destino_existe(id_destino: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que comprueba si existe el destino
    cursor.execute(f"SELECT IF( COUNT(*)>0, TRUE, FALSE) FROM destino WHERE id_destino = '{id_destino}' AND anulado = 0;")

    # obtiene el resultado
    existe = cursor.fetchone()  # trae solo un resultado
    
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return existe[0]

# lista todos los destinos
def destino_listar():
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta para obtener todas los destinos
    cursor.execute("""SELECT destino.id_destino,
                            ciudad.ciudad, 
                            pais.pais,
                            destino.costo
                    FROM destino
                        LEFT JOIN ciudad ON ciudad.id_ciudad = destino.id_ciudad
                        LEFT JOIN pais ON pais.id_pais = ciudad.id_pais
                    WHERE anulado = 0;""")

    # obtiene el resultado
    resultado = cursor.fetchall()
    
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return resultado

# crear destino
def destino_crear(id_ciudad: int, costo: float):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que inserta al destino
    cursor.execute(f"INSERT INTO destino (id_ciudad, costo) VALUES ('{id_ciudad}', '{costo}');")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

# actualizar destino
def destino_actualizar(id_destino: int, id_ciudad: str, costo: str):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que actualiza al cliente
    cursor.execute(f"UPDATE destino SET id_ciudad = '{id_ciudad}', costo = '{costo}' WHERE id_destino = {id_destino};")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

# anular destino
def destino_anular(id_destino: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que anula al destino
    cursor.execute(f"UPDATE destino SET anulado = 1 WHERE id_destino = {id_destino};")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()
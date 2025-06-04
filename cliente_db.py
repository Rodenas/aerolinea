from conexion_db import get_conexion;

# comprobar si el cliente existe
def cliente_existe(cuit_cliente: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que actualiza al cliente en anulado
    cursor.execute(f"SELECT IF( COUNT(*)>0, TRUE, FALSE) FROM cliente where cuit = '{cuit_cliente}';")

    # obtiene el resultado
    existe = cursor.fetchone()  # trae solo un resultado

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return existe[0]

# crear cliente
def cliente_crear(cuit: int, razon_social: str, correo: str):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que inserta al cliente
    cursor.execute(f"INSERT INTO cliente (cuit, razon_social, correo) VALUES ({cuit}, '{razon_social}', '{correo}');")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

# actualizar cliente
def cliente_actualizar(cuit_editar: int, cuit: int, razon_social: str, correo: str):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que actualiza al cliente
    cursor.execute(f"UPDATE cliente SET cuit = {cuit}, razon_social = '{razon_social}', correo = '{correo}' WHERE cuit = {cuit_editar};")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

# anular cliente
def cliente_anular(id_cliente: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que anula al cliente
    cursor.execute(f"UPDATE cliente SET anulado = 1 WHERE cuit = {id_cliente};")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()
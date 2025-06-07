from db.conexion_db import get_conexion;
import datetime;

# comprobar si la venta existe
def venta_existe(id_venta: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que comprueba si existe el venta
    cursor.execute(f"SELECT IF( COUNT(*)>0, TRUE, FALSE) FROM venta WHERE id_venta = '{id_venta} AND anulado = 0';")

    # obtiene el resultado
    existe = cursor.fetchone()  # trae solo un resultado
    
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return existe[0]

# lista todos las ventas
def venta_listar():
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta para obtener todas las ventas
    cursor.execute("""SELECT venta.id_venta,
                             cliente.cuit,
                             cliente.razon_social,
                             DATE_FORMAT(venta.fecha, "%d-%m-%Y %H:%i:%S"),
                             venta.costo,
                             ciudad.ciudad,
                             pais.pais,
                             venta.fecha_anulado,
                             venta.anulado
                      FROM venta
                          LEFT JOIN cliente ON cliente.id_cliente = venta.id_cliente
                          LEFT JOIN destino ON destino.id_destino = venta.id_destino
                          LEFT JOIN ciudad ON ciudad.id_ciudad = destino.id_ciudad
                          LEFT JOIN pais ON pais.id_pais = ciudad.id_pais;""")

    # obtiene el resultado
    resultado = cursor.fetchall()
    
    # cerrar conexion
    cursor.close()
    conexion.close()

    # retorna el resultado
    return resultado

# crear venta
def venta_crear(id_destino: int, cuit_cliente: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # asignamos el valor de la fecha
    fecha = datetime.datetime.now()

    # obtener el id del cliente
    cursor.execute(f"SELECT id_cliente FROM cliente WHERE cuit = '{cuit_cliente}';")
    # obtiene el resultado
    id_cliente = cursor.fetchone()[0]  # trae solo un resultado

    # obtener el costo del destino
    cursor.execute(f"SELECT costo FROM destino WHERE id_destino = '{id_destino}';")
    # obtiene el resultado
    costo = cursor.fetchone()[0]  # trae solo un resultado

    # ejecutar la consulta que inserta la venta
    cursor.execute(f"INSERT INTO venta (id_destino, id_cliente, fecha, costo) VALUES ('{id_destino}', '{id_cliente}', '{fecha}', '{costo}');")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

# comprobar si puede anular venta
def venta_anular_comprobar(id_venta: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # comprobar si puede anular la venta segun la fecha de la venta
    cursor.execute(f"SELECT fecha FROM venta WHERE id_venta = '{id_venta}';")
    # obtiene el resultado
    fecha = cursor.fetchone()  # trae solo un resultado

    # tiempo permitido para eliminar la venta despues de la compra - expresado en segundo
    tiempo_permitido = 30

    resultado = fecha + datetime.timedelta(seconds = tiempo_permitido) < datetime.datetime.now()

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

    return resultado

# anular venta
def venta_anular(id_venta: int):
    # obtiene la conexion de la base de datos
    conexion = get_conexion()
    # crea un cursor para poder hacer las consultas a la base de datos
    cursor = conexion.cursor()

    # ejecutar la consulta que anula al venta
    cursor.execute(f"UPDATE venta SET anulado = 1 WHERE id_venta = {id_venta};")

    # confirmar los cambios
    conexion.commit()
    # cerrar conexion
    cursor.close()
    conexion.close()

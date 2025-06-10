from db import cliente_db;
from db import destino_db;
from db import pais_db;
from db import ciudad_db;
from db import venta_db;

# indica el nombre del sistema
nombre_sistema = 'AirHappy'

print('-----------------------------')
print(f'Bienvenido al sistema {nombre_sistema} - Sistema de Gestión de Pasajes')

continuar_programa = 'si' # indica si el programa tiene que finalizar
opcion_escogida = 0 # indica la opcion escogida por el usuario

while continuar_programa == 'si':
    ##########################
    # mostrar menu principal #
    ##########################
    print('##################')
    print('# Menú Principal #')
    print('##################')
    print('1 - Gestionar Clientes')
    print('2 - Gestionar Destinos')
    print('3 - Gestionar Ventas')
    print('4 - Acerca del Sistema')
    print('5 - Finalizar Programa')
    print('-----------------------------')
    # se le pide al usuario que ingresa una opcion del menu
    opcion_escogida = int(input('Seleccione una opción: '))
    print('-----------------------------\n' * 3)

    # mostrar menu Gestionar Clientes
    if opcion_escogida == 1:
        while True:
            # mostrar menu gestion de clientes #
            print('###########################')
            print('# Menú Gestionar Clientes #')
            print('###########################')
            print('1 - Listar clientes')
            print('2 - Dar de alta cliente')
            print('3 - Modificar cliente')
            print('4 - Dar de baja cliente')
            print('5 - Volver al menú principal')
            print('-----------------------------')
            # se le pide al usuario que ingresa una opcion del menu
            opcion_escogida = int(input('Seleccione una opción: '))
            print('-----------------------------\n' * 3)

            # mostrar listar clientes #
            if opcion_escogida == 1:
                print('#####################')
                print('# Lista de Clientes #')
                print('#####################')
                # listar clientes
                clientes = cliente_db.cliente_listar()
                for i_cliente in clientes:
                    print(i_cliente)
                print('-----------------------------')
                input("Presione Enter para volver al menú de cliente...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar alta de cliente #
            if opcion_escogida == 2:
                print('###################')
                print('# Alta de Cliente #')
                print('###################')
                print('Ingrese los datos del cliente nuevo:')
                # se le pide al usuario que ingrese la razon social del cliente
                razon_social = input('Ingrese razón social: ')
                # se le pide al usuario que ingrese el CUIT del cliente
                cuit = int(input('Ingrese CUIT: '))
                # se le pide al usuario que ingrese el correo electronico del cliente
                correo = input('Ingrese correo electrónico: ')
                print('-----------------------------\n' * 3)
                # se le muestra al usuario que datos se cargaron
                print('Los datos del cliente cargado son:')
                print(f'Razón social: {razon_social}')
                print(f'CUIT: {cuit}')
                print(f'Correo electrónico: {correo}')
                print('-----------------------------')
                # comprueba si el cuit ya eta cargado
                if cliente_db.cliente_existe(cuit):
                    print('El cliente ya existe')
                    print('-----------------------------')
                    print('Los datos no fueron cargados')
                else:
                    # guarda los datos del cliente en la base de datos
                    cliente_db.cliente_crear(cuit, razon_social, correo)                        
                    print('Cliente guardado correctamente')

                print('-----------------------------')
                input("Presione Enter para volver al menú de cliente...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar modificar cliente #
            if opcion_escogida == 3:
                print('#####################')
                print('# Modificar Cliente #')
                print('#####################')
                # se le pide al usuario que ingrese el nombre del usuario que quiere modificar
                cliente_modificar = int(input('Ingrese el cuit del cliente a modificar: '))
                # comprueba si el cliente existe
                if cliente_db.cliente_existe(cliente_modificar):
                    # se le indica al usuario que el cliente que quiere modificar fue encontrado
                    print(f'Cliente {cliente_modificar} encontrado')
                    input("Presione Enter para continuar...")
                    print('-----------------------------')
                    # se le pide al usuario que ingrese la razon social del cliente
                    razon_social = input('Ingrese razón social: ')
                    # se le pide al usuario que ingrese el cuit del cliente
                    cuit = int(input('Ingrese CUIT: '))
                    # se le pide al usuario que ingrese el correo electronico del cliente
                    correo = input('Ingrese correo electrónico: ')
                    print('-----------------------------\n' * 3)
                    # se le muestra al usuario que datos se cargaron
                    print('Los datos del cliente cargado son:')
                    print(f'Razón social: {razon_social}')
                    print(f'CUIT: {cuit}')
                    print(f'Correo electrónico: {correo}')
                    print('-----------------------------')

                    # comprueba si el cuit ya eta cargado
                    if cliente_modificar != cuit and cliente_db.cliente_existe(cuit):
                        print('Ya existe un cliente con ese cuit')
                        print('-----------------------------')
                        print('Los datos del cliente no se actualizaron')
                    else:
                        # actualiza los datos del cliente en la base de datos
                        cliente_db.cliente_actualizar(cliente_modificar, cuit, razon_social, correo)
                        print('Cliente guardado correctamente')
                else:
                    print('-----------------------------')
                    print('Cliente no encontrado')

                print('-----------------------------')
                input("Presione Enter para volver al menú de cliente...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar dar de baja cliente #
            if opcion_escogida == 4:
                print('#######################')
                print('# Dar de Baja Cliente #')
                print('#######################')
                # se le pide al usuario que ingrese el cuit del usuario que quiere dar de baja
                cliente_baja = int(input('Ingrese el cuit del cliente a dar de baja: '))
                print('-----------------------------')
                # comprueba si el cuit ya eta cargado
                if cliente_db.cliente_existe(cliente_baja):
                    print(f'Cliente {cliente_baja} encontrado')
                    print('-----------------------------')
                    input("Presione Enter para continuar...")
                    print('-----------------------------')
                    # actualiza los datos del cliente en la base de datos
                    cliente_db.cliente_anular(cliente_baja)
                    # se le indica al usuario que el cliente ingresado fue dado de baja
                    print(f'El cliente {cliente_baja} fue dado de baja')
                else:
                    print(f'El cliente {cliente_baja} no existe')
                print('-----------------------------')
                input("Presione Enter para volver al menú de cliente...")
                print('-----------------------------\n' * 3)
                continue

            # volver al menu principal #
            if opcion_escogida == 5:
                print('-----------------------------')
                print('Volver al menú principal')
                print('-----------------------------\n' * 3)
                opcion_escogida = 0
                break

    # mostrar menu Gestionar Destinos
    if opcion_escogida == 2:
        while True:
            # mostrar menu gestion de destinos #
            print('###########################')
            print('# Menú Gestionar Destinos #')
            print('###########################')
            print('1 - Listar destinos')
            print('2 - Dar de alta destino')
            print('3 - Modificar destino')
            print('4 - Dar de baja destino')
            print('5 - Volver al menú principal')
            print('-----------------------------')
            # se le pide al usuario que ingresa una opcion del menu
            opcion_escogida = int(input('Seleccione una opción: '))
            print('-----------------------------\n' * 3)

            # listar destinos #
            if opcion_escogida == 1:
                print('#####################')
                print('# Lista de Destinos #')
                print('#####################')
                # listar destinos
                destinos = destino_db.destino_listar()
                for i_destino in destinos:
                    print(i_destino)
                print('-----------------------------')
                input("Presione Enter para volver al menú de destino...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar alta de destino #
            if opcion_escogida == 2:
                print('###################')
                print('# Alta de Destino #')
                print('###################')
                print('Ingrese los datos del destino nuevo:')
                print('Paises disponibles:')
                # lista los paises
                paises = pais_db.pais_listar()
                for i_pais in paises:
                    print(i_pais)
                # se le pide al usuario que ingrese el pais
                pais = int(input('Seleccione país: '))
                print('Ciudades disponibles:')
                # lista las ciudades
                ciudades = ciudad_db.ciudad_listar_por_pais(pais)
                for i_ciudad in ciudades:
                    print(i_ciudad)
                # se le pide al usuario que ingrese la ciudad
                ciudad = int(input('Seleccione ciudad: '))
                # se le pide al usuario que ingrese el costo
                costo = float(input('Ingrese el costo: '))
                print('-----------------------------\n' * 3)
                # guardar destino en la base de datos
                destino_db.destino_crear(ciudad, costo)
                print('Destino guardado correctamente')

                print('-----------------------------')
                input("Presione Enter para volver al menú de destino...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar modificar destino #
            if opcion_escogida == 3:
                print('#####################')
                print('# Modificar Destino #')
                print('#####################')
                destino = int(input('Ingrese id del destino a modificar: '))
                if destino_db.destino_existe(destino):
                    print('-----------------------------')
                    print('El destino ingresado fue encontrado')
                    print('-----------------------------')
                    input("Presione Enter para continuar...")
                    print('-----------------------------')
                    print('Paises disponibles:')
                    # lista los paises
                    paises = pais_db.pais_listar()
                    for i_pais in paises:
                        print(i_pais)
                    # se le pide al usuario que ingrese el pais
                    pais = int(input('Seleccione país: '))
                    print('Ciudades disponibles:')
                    # lista las ciudades
                    ciudades = ciudad_db.ciudad_listar_por_pais(pais)
                    for i_ciudad in ciudades:
                        print(i_ciudad)
                    # se le pide al usuario que ingrese la ciudad
                    ciudad = int(input('Seleccione ciudad: '))
                    # se le pide al usuario que ingrese el costo
                    costo = float(input('Ingrese el costo: '))
                    print('-----------------------------\n' * 3)
                    # guardar destino en la base de datos
                    destino_db.destino_actualizar(destino, ciudad, costo)
                    print('Destino guardado correctamente')
                else:
                    print('-----------------------------')
                    print('El destino ingresado no existe')

                print('-----------------------------')
                input("Presione Enter para volver al menú de destino...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar dar de baja destino #
            if opcion_escogida == 4:
                print('#######################')
                print('# Dar de Baja Destino #')
                print('#######################')
                # se le pide al usuario que ingrese el id del destino que quiere dar de baja
                destino_baja = int(input('Ingrese el id del destino a dar de baja: '))
                print('-----------------------------')
                # comprueba si el cuit ya eta cargado
                if destino_db.destino_existe(destino_baja):
                    print(f'Destino {destino_baja} encontrado')
                    print('-----------------------------')
                    input("Presione Enter para continuar...")
                    print('-----------------------------')
                    # actualiza los datos del destino en la base de datos
                    destino_db.destino_anular(destino_baja)
                    # se le indica al usuario que el destino ingresado fue dado de baja
                    print(f'El destino {destino_baja} fue dado de baja')
                else:
                    print(f'El destino {destino_baja} no existe')
                print('-----------------------------')
                input("Presione Enter para volver al menú de destino...")
                print('-----------------------------\n' * 3)
                continue

            # volver al menu principal #
            if opcion_escogida == 5:
                print('-----------------------------')
                print('Volver al menú principal')
                print('-----------------------------\n' * 3)
                opcion_escogida = 0
                break

    # mostrar menu Gestionar Ventas
    if opcion_escogida == 3:
        while True:
            # mostrar menu gestion de clientes #
            print('#########################')
            print('# Menú Gestionar Ventas #')
            print('#########################')
            print('1 - Listar ventas')
            print('2 - Dar de alta venta')
            print('3 - Dar de baja venta (Arrepentimiento)')
            print('4 - Volver al menú principal')
            print('-----------------------------')
            # se le pide al usuario que ingresa una opcion del menu
            opcion_escogida = int(input('Seleccione una opción: '))
            print('-----------------------------\n' * 3)

            # mostrar listar venta #
            if opcion_escogida == 1:
                print('###################')
                print('# Lista de Ventas #')
                print('###################')
                # listar clientes
                ventas = venta_db.venta_listar()
                for i_venta in ventas:
                    print(i_venta)
                print('-----------------------------')
                input("Presione Enter para volver al menú de venta...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar alta de venta #
            if opcion_escogida == 2:
                print('#################')
                print('# Alta de Venta #')
                print('#################')
                print('Ingrese los datos de la venta nuevo:')
                # se le pide al usuario que ingrese el cuit del cliente
                cuit_cliente = int(input('Ingrese cuit del cliente: '))
                # comprueba si el cliente existe
                if cliente_db.cliente_existe(cuit_cliente):
                    # se le pide al usuario que ingrese el id del destino
                    id_destino = int(input('Ingrese id del destino: '))
                    print('-----------------------------\n' * 3)
                    # comprueba si el destino existe
                    if destino_db.destino_existe(id_destino):
                        # guarda los datos de la venta en la base de datos
                        venta_db.venta_crear(id_destino, cuit_cliente)
                        print('Venta guardado correctamente')
                    else:
                        print('El destino no existe')
                        print('-----------------------------')
                        print('Los datos no fueron cargados')
                else:
                    print('El cliente no existe')
                    print('-----------------------------')
                    print('Los datos no fueron cargados')

                print('-----------------------------')
                input("Presione Enter para volver al menú de venta...")
                print('-----------------------------\n' * 3)
                continue

            # mostrar dar de baja venta #
            if opcion_escogida == 3:
                print('#######################################')
                print('# Dar de Baja Venta (Arrepentimiento) #')
                print('#######################################')
                # se le pide al usuario que ingrese el id de la venta que quiere dar de baja
                id_venta = int(input('Ingrese el id de la venta a dar de baja: '))
                print('-----------------------------')
                # comprueba si la venta existe
                if venta_db.venta_existe(id_venta):
                    print(f'Venta {id_venta} encontrado')
                    print('-----------------------------')
                    input("Presione Enter para continuar...")
                    print('-----------------------------')
                    # comprueba si la venta puede darse de baja
                    if venta_db.venta_anular_comprobar(id_venta):
                        # anular la venta
                        venta_db.venta_anular(id_venta)
                        # se le indica al usuario que la venta ingresado fue dado de baja
                        print(f'La venta {id_venta} fue dada de baja bajo el reglamente que dispone la Ley N° Ley 24.240.')
                    else:
                        print(f'La venta {id_venta} no puede darse de baja por que ya paso la fecha limite segun la Ley N° 24.240. Deberá concurrir a ventanilla para anular la venta de manera presencial.')
                else:
                    print(f'La venta {id_venta} no existe o ya esta anulada')
                print('-----------------------------')
                input("Presione Enter para volver al menú de venta...")
                print('-----------------------------\n' * 3)
                continue

            # volver al menu principal #
            if opcion_escogida == 4:
                print('-----------------------------')
                print('Volver al menú principal')
                print('-----------------------------\n' * 3)
                opcion_escogida = 0
                break

    # mostrar menu Acerca del Sistema
    if opcion_escogida == 4:
        ######################
        # acerca del sistema #
        ######################
        print('######################')
        print('# Acerca del Sistema #')
        print('######################')
        print('-----------------------------')
        print('Datos de la aplicación')
        print('-----------------------------')
        print(f'Nombre: {nombre_sistema}')
        print('Version: 1.0')
        print('Licencia: licencia comercial')
        print('-----------------------------')
        print('Desarrolladores')
        print('--------------------------------------------')
        print('| Apellido | Nombre           | DNI        |')
        print('--------------------------------------------')
        print('| Barilla  | Mauricio         | 36.357.667 |')
        print('| Carranza | Nazarena         | 43.693.498 |')
        print('| Peredo   | Jennifer         | 40.572.933 |')
        print('| Galvagno | María Laura      | 23.778.620 |')
        print('| Rodenas  | Gabriel Elías    | 36.356.976 |')
        print('| Tissera  | Guillermo Adrián | 35.260.232 |')
        print('--------------------------------------------')
        input("Presione Enter para volver al menú principal...")
        continue

    # mostrar menu Finalizar Programa
    if opcion_escogida == 5:
        # Finalizar Programa #
        finalizar_programa = input('Escriba "si" para finalizar el programa o cualquier otra cosa para continuar: ')
        if finalizar_programa == 'si':
            # se le consulta al usuario si quiere finalizar el programa
            print('-----------------------------')
            print('Finalizando programa')
            for i in range(10):
                print('.')
            continuar_programa = 'no'
        continue


print("Programa finalizado")

import cliente_db;

"""
Propósito del sistema:
El objetivo es realizar un sistema que permita gestionar las ventas de pasajes de una aerolínea registrando los clientes, destinos y ventas realizadas.
"""

"""
Cómo instalar y ejecutar el programa:
Para ejecutar el programa es necesario abrir el archivo main.py con Visual Studio Code y ejecutar el codigo.
"""

"""
Datos de los integrantes del grupo:
--------------------------------------------
| Apellido | Nombre           | DNI        |
--------------------------------------------
| Barilla  | Mauricio         | 36.357.667 |
| Carranza | Nazarena         | 43.693.498 |
| Peredo   | Jennifer         | 40.572.933 |
| Perez    | María Laura      | 23.778.620 |
| Rodenas  | Gabriel Elías    | 36.356.976 |
| Tissera  | Guillermo Adrián | 35.260.232 |
--------------------------------------------
"""




# indica el nombre del sistema
nombre_sistema = 'AirHappy'

print('-----------------------------')
print(f'Vienvenido al sistema {nombre_sistema} - Sistema de Gestión de Pasajes')

fin_programa = 'no' # indica si el programa tiene que finalizar
continuar_abm_cliente = 'no' # indica si tiene que seguir mostrando el menu de 'Gestionar Clientes'
opcion_escogida = 0 # indica la opcion escogida por el usuario

while fin_programa == 'no':
    ##########################
    # mostrar menu principal #
    ##########################
    print('##################')
    print('# Menú Principal #')
    print('##################')
    print('1 - Gestionar Clientes')
    print('2 - Gestionar Destinos')
    print('3 - Gestionar Ventas')
    print('4 - Consultar Ventas')
    print('5 - Botón de Arrepentimiento')
    print('6 - Ver Reporte General')
    print('7 - Acerca del Sistema')
    print('8 - Finalizar Programa')
    print('-----------------------------')
    # se le pide al usuario que ingresa una opcion del menu
    opcion_escogida = int(input('Seleccione una opción: '))
    print('-----------------------------\n' * 3)

    # mostrar menu Gestionar Clientes
    if opcion_escogida == 1:
           continuar_abm_cliente = 'si'
           while continuar_abm_cliente == 'si':
                ####################################
                # mostrar menu gestion de clientes #
                ####################################
                print('###########################')
                print('# Menú Gestionar Clientes #')
                print('###########################')
                print('1 - Dar de alta cliente')
                print('2 - Modificar cliente')
                print('3 - Dar de baja cliente')
                print('4 - Volver al menú principal')
                print('-----------------------------')
                # se le pide al usuario que ingresa una opcion del menu
                opcion_escogida = int(input('Seleccione una opción: '))
                print('-----------------------------\n' * 3)

                # mostrar alta de cliente #
                if opcion_escogida == 1:
                    print('###################')
                    print('# Alta de cliente #')
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
                if opcion_escogida == 2:
                    print('#####################')
                    print('# Modificar cliente #')
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
                if opcion_escogida == 3:
                    print('#######################')
                    print('# Dar de baja cliente #')
                    print('#######################')
                    # se le pide al usuario que ingrese el nombre del usuario que quiere dar de baja
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
                if opcion_escogida == 4:
                    print('-----------------------------')
                    print('Volver al menú principal')
                    print('-----------------------------\n' * 3)
                    continuar_abm_cliente = 'no'
                    opcion_escogida = 0
                    continue

    # mostrar menu Gestionar Destinos
    if opcion_escogida == 2:
        print('Muestra menú "Gestionar Destinos"')
        input("Presione Enter para volver al menú principal...")
        print('-----------------------------\n' * 3)
        continue

    # mostrar menu Gestionar Ventas
    if opcion_escogida == 3:
        print('Muestra menú "Gestionar Ventas"')
        input("Presione Enter para volver al menú principal...")
        print('-----------------------------\n' * 3)
        continue

    # mostrar menu Consultar Ventas
    if opcion_escogida == 4:
        print('Muestra menú "Consultar Ventas"')
        input("Presione Enter para volver al menú principal...")
        print('-----------------------------\n' * 3)
        continue

    # mostrar menu Botón de Arrepentimiento
    if opcion_escogida == 5:
        print('Muestra menú "Botón de Arrepentimiento"')
        input("Presione Enter para volver al menú principal...")
        print('-----------------------------\n' * 3)
        continue
       
    # mostrar menu Ver Reporte General
    if opcion_escogida == 6:
        print('Muestra menú "Ver Reporte General"')
        input("Presione Enter para volver al menú principal...")
        print('-----------------------------\n' * 3)
        continue

    # mostrar menu Acerca del sistema
    if opcion_escogida == 7:
        ######################
        # acerca del sistema #
        ######################
        print('#######################')
        print('# Acerca del sistema #')
        print('#######################')
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
        print('| Perez    | María Laura      | 23.778.620 |')
        print('| Rodenas  | Gabriel Elías    | 36.356.976 |')
        print('| Tissera  | Guillermo Adrián | 35.260.232 |')
        print('--------------------------------------------')
        input("Presione Enter para volver al menú principal...")
        continue

    # mostrar menu Finalizar Programa
    if opcion_escogida == 8:
        ######################
        # Finalizar Programa #
        ######################
        finalizar_programa = input('Escriba "si" para finalizar el programa o cualquier otra cosa para continuar: ')
        if finalizar_programa == 'si':
            # se le consulta al usuario si quiere finalizar el programa
            print('-----------------------------')
            print('Finalizando programa')
            for i in range(10):
                print('.')
            fin_programa = 'si'
        continue


print("Programa finalizado")
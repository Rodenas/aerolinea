- Nombre del proyecto:
AirHappy

- Breve descripción:
El objetivo es realizar un sistema que permita gestionar las ventas de pasajes de una aerolínea registrando los clientes, destinos y ventas realizadas.

- Integrantes del grupo:
--------------------------------------------
| Apellido | Nombre           | DNI        |
--------------------------------------------
| Barilla  | Mauricio         | 36.357.667 |
| Carranza | Nazarena         | 43.693.498 |
| Peredo   | Jennifer         | 40.572.933 |
| Galvagno | María Laura      | 23.778.620 |
| Rodenas  | Gabriel Elías    | 36.356.976 |
| Tissera  | Guillermo Adrián | 35.260.232 |
--------------------------------------------

- Instrucciones básicas de ejecución del proyecto:
1) Ejecutar el archivo db.sql en mysql para generar la base de datos.
2) Abrir el archivo main.py con Visual Studio Code y ejecutar el codigo.

- Detalle completo de todo lo que hay en el repositorio:
DER.PNG : imagen de la representacion de la base de datos en un DER (Diagramas de Entidad-Relación)
db.sql : contiene los DDL y DML para la generacion de la base de datos
README.md : contiene una breve descripcion del proyecto
main.py : contiene el codigo principal de la aplicacion, es el que se usa para ejecutar el programa.
db: carpeta que contiene los siguientes archivos:
 - conexion_db.py : crea la conexion entre visual studio code y la base de datos.
 - cliente_db.py : contiene los DML para la tabla cliente de la base de datos
 - ciudad_db.py : contiene los DML para la tabla ciudad de la base de datos
 - destino_db.py : contiene los DML para la tabla destino de la base de datos
 - pais_db.py : contiene los DML para la tabla pais de la base de datos
 - venta_db.py : contiene los DML para la tabla venta de la base de datos
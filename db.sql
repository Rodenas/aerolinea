-- creacion del esquema db_aerolinea
CREATE SCHEMA IF NOT EXISTS `db_aerolinea` DEFAULT CHARACTER SET utf8mb3 ;
USE `db_aerolinea` ;

-- creacion de la tabla cliente
CREATE TABLE IF NOT EXISTS cliente (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `cuit` VARCHAR(11) NOT NULL,
  `razon_social` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NULL DEFAULT '',
  `anulado` TINYINT(1) NULL DEFAULT false,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `cuit_UNIQUE` (`cuit` ASC) VISIBLE)
ENGINE = InnoDB;

-- creacion dela tabla pais
CREATE TABLE IF NOT EXISTS pais (
  `id_pais` INT NOT NULL AUTO_INCREMENT,
  `pais` VARCHAR(45) NULL,
  PRIMARY KEY (`id_pais`))
ENGINE = InnoDB;

-- cracion de la tabla ciudad
CREATE TABLE IF NOT EXISTS ciudad (
  `id_ciudad` INT NOT NULL AUTO_INCREMENT,
  `id_pais` INT NOT NULL,
  `ciudad` VARCHAR(45) NULL,
  PRIMARY KEY (`id_ciudad`),
  CONSTRAINT `fk_destino_pais`
    FOREIGN KEY (`id_pais`)
    REFERENCES pais (`id_pais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- creacion de la tabla destino
CREATE TABLE IF NOT EXISTS destino (
  `id_destino` INT NOT NULL AUTO_INCREMENT,
  `id_ciudad` INT NOT NULL,
  `costo` FLOAT(10,2) NULL,
  `anulado` TINYINT(1) NULL DEFAULT '0',
  PRIMARY KEY (`id_destino`),
  CONSTRAINT `fk_destino_ciudad`
    FOREIGN KEY (`id_ciudad`)
    REFERENCES ciudad (`id_ciudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- creacion de la tabla venta
CREATE TABLE IF NOT EXISTS venta (
  `id_venta` INT NOT NULL AUTO_INCREMENT,
  `id_destino` INT NOT NULL,
  `id_cliente` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  `costo` FLOAT(10,2) NOT NULL,
  `fecha_anulado` DATETIME NULL DEFAULT NULL,
  `anulado` TINYINT(1) NULL DEFAULT false,
  PRIMARY KEY (`id_venta`),
  CONSTRAINT `fk_venta_destino`
    FOREIGN KEY (`id_destino`)
    REFERENCES destino (`id_destino`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_cliente`
    FOREIGN KEY (`id_cliente`)
    REFERENCES cliente (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- insertar clientes
INSERT INTO cliente (`cuit`, `razon_social`, `correo`) VALUES ('27331664435', 'Macro', 'macro@gmail.com');
INSERT INTO cliente (`cuit`, `razon_social`, `correo`) VALUES ('30429514939', 'Mami', 'mami@gmail.com');
INSERT INTO cliente (`cuit`, `razon_social`, `correo`) VALUES ('34883396857', 'Carrefour', 'carrefour@gmail.com');

-- insertar pais
INSERT INTO pais (`pais`) VALUES ('Argentina');
INSERT INTO pais (`pais`) VALUES ('Estados Unidos');
INSERT INTO pais (`pais`) VALUES ('España');
INSERT INTO pais (`pais`) VALUES ('Italia');
INSERT INTO pais (`pais`) VALUES ('Mexico');
INSERT INTO pais (`pais`) VALUES ('Inglaterra');
INSERT INTO pais (`pais`) VALUES ('Rusia');
INSERT INTO pais (`pais`) VALUES ('China');

-- insertar ciudad
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('1', 'Buenos Aires');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('1', 'Córdoba');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('1', 'Salta');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('2', 'Nueva York');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('2', 'San Francisco');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('2', 'Los Ángeles');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('3', 'Barcelona');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('3', 'Madrid');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('3', 'Sevilla');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('4', 'Roma');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('4', 'Venecia');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('4', 'Florencia');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('5', 'Ciudad de México');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('5', 'Cancún');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('5', 'Cabo San Lucas');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('6', 'Londres');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('6', 'Mánchester');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('6', 'Britol');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('7', 'Moscú');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('7', 'San Petersburgo');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('7', 'Lago Baikal');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('8', 'Shanghái');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('8', 'Pekin');
INSERT INTO ciudad (`id_pais`, `ciudad`) VALUES ('8', 'Cantón');

-- insertar destino
INSERT INTO destino (`id_ciudad`, `costo`) VALUES ('2', '100000');
INSERT INTO destino (`id_ciudad`, `costo`) VALUES ('6', '200000');
INSERT INTO destino (`id_ciudad`, `costo`) VALUES ('7', '300000');
INSERT INTO destino (`id_ciudad`, `costo`) VALUES ('1', '400000');
INSERT INTO destino (`id_ciudad`, `costo`) VALUES ('24', '500000');

-- insertar venta
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('1', '1', '2025-01-25 14:27:42', '100000');
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('2', '1', '2025-02-05 10:02:15', '200000');
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('3', '1', '2025-02-05 10:10:05', '300000');
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('4', '3', '2025-03-15 18:35:32', '400000');

-- listar todos los clientes
SELECT *
FROM cliente;

-- muestra las ventas realizadas posteriores o igual a la fecha 01-02-2025
SELECT venta.id_venta,
	   cliente.cuit,
       cliente.razon_social,
       venta.fecha,
       venta.costo,
       ciudad.ciudad,
       pais.pais,
       venta.fecha_anulado,
       venta.anulado
FROM venta
	LEFT JOIN cliente ON cliente.id_cliente = venta.id_cliente
    LEFT JOIN destino ON destino.id_destino = venta.id_destino
    LEFT JOIN ciudad ON ciudad.id_ciudad = destino.id_ciudad
    LEFT JOIN pais ON pais.id_pais = ciudad.id_pais
WHERE fecha >= '2025-02-01';

-- obtiene la venta de cada cliente
SELECT cliente.id_cliente, 
       cliente.razon_social,
       venta.fecha,
       venta.id_venta,
       ciudad.ciudad,
       pais.pais,
       venta.anulado
FROM cliente
	LEFT JOIN venta ON venta.id_cliente = cliente.id_cliente
    LEFT JOIN destino ON destino.id_destino = venta.id_destino
    LEFT JOIN ciudad ON ciudad.id_ciudad = destino.id_ciudad
    LEFT JOIN pais ON pais.id_pais = ciudad.id_pais;
    
-- listar todos los destinos que su ciudad o pais empiecen con 'C'
SELECT destino.id_destino,
	   ciudad.ciudad,
       pais.pais
FROM destino
	LEFT JOIN ciudad ON ciudad.id_ciudad = destino.id_ciudad
    LEFT JOIN pais ON pais.id_pais = ciudad.id_pais
WHERE ciudad.ciudad LIKE 'C%'
OR pais.pais LIKE 'C%'
;

-- mostrar cuantas ventas se realizaron por país
SELECT pais.pais ,
 	   COUNT(venta.id_venta) AS 'ventas realizadas'
FROM pais 
	LEFT JOIN ciudad ON ciudad.id_pais = pais.id_pais
    LEFT JOIN destino ON destino.id_ciudad = ciudad.id_ciudad
	LEFT JOIN venta ON venta.id_destino = destino.id_destino
GROUP BY pais.id_pais;
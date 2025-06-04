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


-- cracion de la tabla ciudad
CREATE TABLE IF NOT EXISTS ciudad (
  `id_ciudad` INT NOT NULL AUTO_INCREMENT,
  `ciudad` VARCHAR(45) NULL,
  PRIMARY KEY (`id_ciudad`))
ENGINE = InnoDB;


-- creacion dela tabla ciudad
CREATE TABLE IF NOT EXISTS pais (
  `id_pais` INT NOT NULL AUTO_INCREMENT,
  `pais` VARCHAR(45) NULL,
  PRIMARY KEY (`id_pais`))
ENGINE = InnoDB;


-- creacion de la tabla destino
CREATE TABLE IF NOT EXISTS destino (
  `id_destino` INT NOT NULL AUTO_INCREMENT,
  `id_pais` INT NOT NULL,
  `id_ciudad` INT NOT NULL,
  `costo` DECIMAL(10,2) NULL,
  PRIMARY KEY (`id_destino`),
  INDEX `fk_destino_ciudad1_idx` (`id_ciudad` ASC) VISIBLE,
  INDEX `fk_destino_pais1_idx` (`id_pais` ASC) VISIBLE,
  CONSTRAINT `fk_destino_ciudad1`
    FOREIGN KEY (`id_ciudad`)
    REFERENCES ciudad (`id_ciudad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_destino_pais1`
    FOREIGN KEY (`id_pais`)
    REFERENCES pais (`id_pais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- creacion de la tabla venta
CREATE TABLE IF NOT EXISTS venta (
  `id_venta` INT NOT NULL AUTO_INCREMENT,
  `id_destino` INT NOT NULL,
  `id_cliente` INT NOT NULL,
  `fecha` DATETIME NOT NULL,
  `costo` DECIMAL(10,2) NOT NULL,
  `fecha_anulado` DATETIME NULL DEFAULT NULL,
  `anulado` TINYINT(1) NULL DEFAULT false,
  PRIMARY KEY (`id_venta`),
  INDEX `fk_venta_destino_idx` (`id_destino` ASC) VISIBLE,
  INDEX `fk_venta_cliente1_idx` (`id_cliente` ASC) VISIBLE,
  CONSTRAINT `fk_venta_destino`
    FOREIGN KEY (`id_destino`)
    REFERENCES destino (`id_destino`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_cliente1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES cliente (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- insertar clientes
INSERT INTO cliente (`cuit`, `razon_social`, `correo`) VALUES ('27331664435', 'Macro', 'macro@gmail.com');
INSERT INTO cliente (`cuit`, `razon_social`, `correo`) VALUES ('30429514939', 'Mami', 'mami@gmail.com');
INSERT INTO cliente (`cuit`, `razon_social`, `correo`) VALUES ('34883396857', 'Carrefour', 'carrefour@gmail.com');

-- insertar ciudad
INSERT INTO ciudad (`ciudad`) VALUES ('Córdoba');
INSERT INTO ciudad (`ciudad`) VALUES ('Madrid');
INSERT INTO ciudad (`ciudad`) VALUES ('Roma');

-- insertar pais
INSERT INTO pais (`pais`) VALUES ('Argentina');
INSERT INTO pais (`pais`) VALUES ('España');
INSERT INTO pais (`pais`) VALUES ('Italia');

-- insertar destino
INSERT INTO destino (`id_pais`, `id_ciudad`, `costo`) VALUES ('1', '1', '100000');
INSERT INTO destino (`id_pais`, `id_ciudad`, `costo`) VALUES ('2', '2', '200000');
INSERT INTO destino (`id_pais`, `id_ciudad`, `costo`) VALUES ('3', '3', '300000');

-- insertar venta
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('2', '1', '2025-01-25 14:27:42', '200000');
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('2', '2', '2025-02-05 10:02:15', '200000');
INSERT INTO venta (`id_destino`, `id_cliente`, `fecha`, `costo`) VALUES ('3', '3', '2025-03-15 18:35:32', '300000');

-- listar todos los clientes
SELECT *
FROM cliente;

-- muestra las ventas realizadas posteriores o igual a la fecha 01-02-2025
SELECT *
FROM venta
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
    LEFT JOIN pais ON pais.id_pais = destino.id_pais;
    
-- listar todos los destinos que su ciudad o pais empiecen con 'C'
SELECT destino.id_destino,
	   ciudad.ciudad,
       pais.pais
FROM destino
	LEFT JOIN ciudad ON ciudad.id_ciudad = destino.id_ciudad
    LEFT JOIN pais ON pais.id_pais = destino.id_pais
WHERE ciudad.ciudad LIKE 'C%'
OR pais.pais LIKE 'C%';

-- mostrar cuántas ventas se realizaron por país
SELECT pais.pais ,
 	   COUNT(venta.id_venta) AS 'ventas realizadas'
FROM pais 
	LEFT JOIN destino ON destino.id_pais = pais.id_pais
	LEFT JOIN venta ON venta.id_destino = destino.id_destino
GROUP BY pais.id_pais;
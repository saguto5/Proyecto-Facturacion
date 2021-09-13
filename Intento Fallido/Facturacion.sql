CREATE DATABASE facturacion;
use facturacion;

CREATE TABLE producto(
	idProducto int (10) NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    precioCrudo int(20) NOT NULL, 
    PRIMARY KEY(idProducto)
);


SELECT * FROM producto;
insert into producto (idProducto, nombre, precioCrudo) values(001,"camisa", 116000);
insert into producto (idProducto, nombre, precioCrudo) values(002,"pantalon", 119000);
DELETE FROM producto WHERE idProducto = 002;





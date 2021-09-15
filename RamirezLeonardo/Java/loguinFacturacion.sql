create database loguinusuarios;

use loguinusuarios;

create table usuarios (
	id INT NOT NULL,
    nickname VARCHAR (50) NOT NULL,
    pass VARCHAR (50) NOT NULL,
    PRIMARY KEY (id)
);

show tables;

insert into usuarios (id, nickname, pass)
values ('1', 'admin', 'admin');

insert into usuarios (id, nickname, pass)
values ('2', 'leonardo', 'l30nardo');

select * from usuarios;
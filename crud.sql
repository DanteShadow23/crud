## Script creador de base de datos 
##fecha_nacimiento date NOT NULL,
##fecha_nacimiento CURRENT_TIME NOT NULL,

CREATE database crud;

\c crud;

CREATE TABLE usuario(
id SERIAL NOT NULL,
nombre VARCHAR(10) NOT NULL,
apellido VARCHAR(12) NOT NULL,
identificacion VARCHAR(12) NOT NULL,
fecha_nacimiento DATE NOT NULL,
hora_nacimiento TIME NOT NULL,
genero CHAR NOT NULL,
primary key(id)
);

insert into usuario(nombre, apellido, identificacion, fecha_nacimiento, hora_nacimiento, genero) 
values('Luis', 'Diaz', '1067853124', '1999-02-10', '16:30:25', 'M');

--select * from usuario where id = '';

--update usuario set valor_atributo_cambiar='valor_nuevo' where id='';

--delete from usuario where id='valor_identificador';

-- Script creador de base de datos 

CREATE database crud;

\c crud;

-- crear un usuario llamado "dante" con contraseña "Snipper77"
-- en caso de querer usar otro usuario puede modificar los parametros de acceso en bd.py
-- pero la tabla deber ser creada en esa por ese usuario o almenos tener permisos del root
-- use un gestor de base de datos PostgreSQL 12.12 en adelante



CREATE TABLE usuario(
id SERIAL NOT NULL,
nombre VARCHAR(10) NOT NULL,
apellido VARCHAR(12) NOT NULL,
identificacion VARCHAR(12) NOT NULL,
fecha_nacimiento DATE NOT NULL,
genero CHAR NOT NULL,
primary key(id)
);

insert into usuario(nombre, apellido, identificacion, fecha_nacimiento, genero) 
values('Luis', 'Diaz', '1067853124', '1999-02-10', 'M');

--select * from usuario where id = '';

--update usuario set valor_atributo_cambiar='valor_nuevo' where id='';

--delete from usuario where id='valor_identificador';

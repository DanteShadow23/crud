#!/usr/bin/python3
"""
Conexion a PostgreSQL con python
@Autor Dante
"""
from datetime import datetime
import psycopg2
from db import conexion


# Listar los usarios
# Para consultar elementos de cada usuario es: usuario[0] para id, usuario[1] para nombre, etc...
# id = 0, nombre = 1, apellido = 2, identificacion = 3, fecha_nacimiento = 4, hora_nacimiento = 5, genero = 6
def consultarLista():
    try:
        with conexion.cursor() as cursor:
            # En este caso no se necesita limpiar el dato
            cursor.execute("SELECT * FROM usuario;")

            # con fetchall se traen todas las filas
            usuarios = cursor.fetchall()
        
            #for usuario in usuarios:
            #    print(usuario)
        
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar en la Base de Datos: ",e)
    
    finally:
        conexion.close()
    
    return usuarios
    


# Consulta todos los datos de un usuario en particular
# Pueden tomarse uno o dos datos con usuario[0], usuario[1], etc...
# id = 0, nombre = 1, apellido = 2, identificacion = 3, fecha_nacimiento = 4, hora_nacimiento = 5, genero = 6
def consultarUsuario(id):
    try:
        with conexion.cursor() as cursor:
            # En este caso no se necesita limpiar el dato
            consulta = "SELECT * FROM usuario WHERE id = %s;"
            cursor.execute(consulta, (id,))

            # con fetchall se traen todas las filas
            usuarios = cursor.fetchall()

            for usuario in usuarios:
                print(usuario)
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar en la Base de Datos: ",e)
    finally:
        conexion.close()

#Ingresar los Datos de cada usuarios
#Ejemplo:
#ingresar("Jose", "Serpa", "1076123423", "1997-10-12", "10:20:12", 'M')
def ingresar(nom, ape, id, fecha, hora, gen):
    try:
         with conexion.cursor() as cursor:
            # Establecer la sentencia con datos variables
            consulta = "INSERT INTO usuario(nombre, apellido, identificacion, fecha_nacimiento, hora_nacimiento, genero) VALUES (%s, %s, %s, %s, %s, %s);"

            cursor.execute(consulta, (nom, ape, id, fecha, hora, gen))

            # Es necesario hacer commit o no guarda los cabios
            conexion.commit()

            # Mesaje de confirmación
            print("Los Datos se Agregaron correctamente a la Base de Datos")
    except psycopg2.Error as e:
        print("Ocurrió un error al ingresar la información a la Base de Datos: ",e)
    finally:
        conexion.close()


# Editar los datos de cada usuario en la Base de Datos
# Ejemplo:
# editar("2","Jose", "Serpa", "1076123423", "1997-10-12", "22:20:12", 'M')
def editar(id, nom, ape, iden, fecha, hora, gen):
    try:
        with conexion.cursor() as cursor:
            # En este caso no se necesita limpiar el dato
            consulta = "UPDATE usuario SET nombre = %s, apellido = %s, identificacion = %s, fecha_nacimiento = %s, hora_nacimiento = %s, genero = %s WHERE id = %s;"

            # Comando SQL valores a cambiar y llave primaria al final
            cursor.execute(consulta, (nom, ape, iden, fecha, hora, gen, id))

            # El commit es para guardar los cambios en la Base de Datos
            conexion.commit()

            # Mensaje de confirmación
            print("La información se actualizó exitosamente en la Base de Datos")
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar en la Base de Datos: ",e)
    finally:
        conexion.close()

# Eliminar usuarios de la Base de Datos
# eliminar("2")
def eliminar(id):
    try:
        with conexion.cursor() as cursor:
            # En este caso no se necesita limpiar el dato
            consulta = "DELETE FROM usuario WHERE id = %s;"

            # Comando SQL valores a cambiar y llave primaria al final
            cursor.execute(consulta, (id,))

            # El commit es para guardar los cambios en la Base de Datos
            conexion.commit()

            # Mensaje de confirmación
            print("La información del usuario se eliminó correctamente la Base de Datos")
    except psycopg2.Error as e:
        print("Ocurrió un error al Borrar al usuario de la Base de Datos: ",e)
    finally:
        conexion.close()

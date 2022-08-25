#!/usr/bin/python3
"""
Conexion a PostgreSQL con python
@Autor Dante
"""
import psycopg2
import json

# Leer credenciales de un archivo JSON

with open("credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)

# Como la conexión devuelve un diccionario podemos convertirlo fácilmente
# a "kwargs" o key arguments
try:
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un erro al conectar a PostgrSQL: ", e)

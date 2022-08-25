#!/usr/bin/python3
"""
Conexion a PostgreSQL con python
@Autor Dante
"""

from metodos import consultarLista

datos = consultarLista()

for dato in datos:
       print(dato[2])
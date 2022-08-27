#!/usr/bin/python3
"""
Conexion a PostgreSQL con python
@Autor Dante
"""

from crypt import methods
from metodos import actualizar, consultarLista, consultarUsuario, eliminar, ingresar
from flask import Flask, url_for
from flask import render_template, request,redirect, flash

# datos = consultarLista()

# for dato in datos:
#       print(dato[2])


app = Flask(__name__)
app.secret_key="Sombra"

@app.route("/")
def index():
       datos = consultarLista()

       #for dato in datos:
       #       print(dato[4])

       return render_template('usuarios/index.html', usuarios = datos)

@app.route('/create')
def create():
    return render_template('usuarios/create.html')

@app.route('/store', methods=['POST'])
def storage():
    _nom = request.form['txtNombre']
    _ape = request.form['txtApellido']
    _iden = request.form['txtIden']
    _fecha = request.form['txtFecha']
    

    if _nom == '' or _ape == '' or _iden == '' or _fecha == '':
       flash('Recuerda llenar todos los datos de los campos')  
       return redirect(url_for('create'))
    else:
       _gen = request.form['txtGen']

    ingresar(_nom, _ape, _iden, _fecha, _gen)
    return redirect('/')


@app.route('/destroy/<int:id>')
def destroy(id):
       
       eliminar(id)

       return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):

       datos = consultarUsuario(id)

       return render_template('usuarios/edit.html', usuarios = datos)


@app.route('/update', methods=['POST'])
def update():
       _id = request.form["txtId"]
       _nom = request.form['txtNombre']
       _ape = request.form['txtApellido']
       _iden = request.form['txtIden']
       _fecha = request.form['txtFecha']
       _gen = request.form['txtGen']

       actualizar(_id, _nom, _ape, _iden, _fecha, _gen)

       return redirect('/')

if __name__== '__main__':
       app.run(debug=True)
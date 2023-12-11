from flask import render_template, request, redirect, session, flash, url_for
from app_flask.modelos.modelo_tienda import Tienda
from app_flask.modelos.modelo_usuarios import Usuario
from app_flask.modelos.modelo_ventas import Venta
from app_flask import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    if request.method == 'POST':
        datos = {
            'id_usuario': request.form['id_usuario'],
            'id_producto': request.form['id_producto'],
            'total': request.form['total'],
            'fecha_creacion': request.form['fecha_creacion'],
            'fecha_actualizacion': request.form['fecha_actualizacion']
        }
        Venta.crear_uno(datos)
        return redirect(url_for('ventas'))
    ventas = Venta.obtener_todos()
    return render_template('ventas.html', ventas=ventas)

@app.route('/ventas/<id>', methods=['GET'])
def detalle_venta(id):
    venta = Venta.obtener_por_id({'id': id})
    detalles = Venta.obtener_detalles({'id': id})
    return render_template('detalle_venta.html', venta=venta, detalles=detalles)


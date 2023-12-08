<<<<<<< HEAD
from flask import render_template, redirect, request, flash, session, url_for
from app_flask import app
from app_flask.modelos.modelo_ventas import Venta, DetallesVenta


@app.route('/ventas')
def mostrar_ventas():
    try:
        ventas = Venta.obtener_todos()
        return render_template('ventas.html', ventas=ventas)
    except Exception as e:
        flash(f"Error al obtener las ventas: {str(e)}", 'error')
        return redirect(url_for('pagina_de_error'))

@app.route('/ventas/<int:id_venta>')
def mostrar_detalles_venta(id_venta):
    venta = Venta.obtener_por_id({'id': id_venta})
    detalles_venta = Venta.obtener_detalles({'id': id_venta})
    return render_template('detalles_venta.html', venta=venta, detalles_venta=detalles_venta)

@app.route('/ventas/crear', methods=['POST'])
def crear_venta():
    datos_venta = {
        'id_usuario': request.form['id_usuario'],
        'id_producto': request.form['id_producto'],
        'total': request.form['total'],
        'fecha_creacion': request.form['fecha_creacion'],
        'fecha_actualizacion': request.form['fecha_actualizacion']
    }
    
    nueva_venta = Venta.crear_uno(datos_venta)
    
    flash('¡Venta creada exitosamente!', 'success')
    return redirect('/ventas')

@app.route('/ventas/editar/<int:id_venta>', methods=['GET', 'POST'])
def editar_venta(id_venta):
    if request.method == 'GET':
        venta = Venta.obtener_por_id({'id': id_venta})
        return render_template('editar_venta.html', venta=venta)
    elif request.method == 'POST':
        datos_venta = {
            'id': id_venta,
=======
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
>>>>>>> origin/main
            'id_usuario': request.form['id_usuario'],
            'id_producto': request.form['id_producto'],
            'total': request.form['total'],
            'fecha_creacion': request.form['fecha_creacion'],
            'fecha_actualizacion': request.form['fecha_actualizacion']
        }
<<<<<<< HEAD
        
        Venta.actualizar(datos_venta)
        
        flash('¡Venta actualizada exitosamente!', 'success')
        return redirect('/ventas')

@app.route('/ventas/eliminar/<int:id_venta>')
def eliminar_venta(id_venta):
    datos_venta = {'id': id_venta}
    Venta.eliminar(datos_venta)
    flash('¡Venta eliminada exitosamente!', 'success')
    return redirect('/ventas')

# Otras rutas y funciones relacionadas con ventas según sea necesario

if __name__ == "__main__":
    app.run(debug=True)
=======
        Venta.crear_uno(datos)
        return redirect(url_for('ventas'))
    ventas = Venta.obtener_todos()
    return render_template('ventas.html', ventas=ventas)

@app.route('/ventas/<id>', methods=['GET'])
def detalle_venta(id):
    venta = Venta.obtener_por_id({'id': id})
    detalles = Venta.obtener_detalles({'id': id})
    return render_template('detalle_venta.html', venta=venta, detalles=detalles)
>>>>>>> origin/main

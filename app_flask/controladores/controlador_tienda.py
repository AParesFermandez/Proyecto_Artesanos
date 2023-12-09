from flask import flash, redirect, request
from flask import session
from flask import render_template
from app_flask.modelos.modelo_tienda import Tienda
from app_flask import app
from app_flask.modelos.modelo_tienda import servicios
from app_flask.modelos.modelo_usuarios import Usuario

@app.route('/crear_servicio_form', methods=['POST'])
def crear_servicio_form():
    return render_template('crear_servicios.html')

# Ruta para manejar el envío del formulario
@app.route('/crear_servicio', methods=['POST'])
def crear_servicio():
    if request.method == 'POST':
        id_servicio = request.form['id']
        nombre_servicio = request.form['nombre_servicio']
        descripcion = request.form['descripcion']
        imagenes = request.form['imagenes'].split(',')  # Si las URL de las imágenes están separadas por comas
        valoracion = request.form['valoracion']
    
    datos_servicio = {
            "id_servicio" : id_servicio,
            'nombre_servicio': nombre_servicio,
            'descripcion': descripcion,
            'imagenes': imagenes,
            "valoracion": valoracion
        }
    
    if not servicios.validar_servicios(datos_servicio):
            return redirect(f'/editar/{id}')

@app.route('/servicio_creado/<int:id_producto>')
def mostrar_servicio_creado(id_producto):

    servicio_ficticio = {
        'id': id_producto,
        'nombre': 'Servicio de ejemplo',
        'descripcion': 'Descripción del servicio',
        'imagenes': ['url-imagen-1.jpg', 'url-imagen-2.jpg'],
        'valoracion': 4.5
    }


    return render_template('servicio_creado.html', servicio=servicio_ficticio)



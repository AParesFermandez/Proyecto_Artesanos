from flask import flash, redirect, request
from flask import session
from flask import render_template
from app_flask.modelos.modelo_tienda import Tienda
from app_flask import app
from app_flask.modelos.modelo_tienda import servicios
from app_flask.modelos.modelo_usuarios import Usuario

#render_templates rutas mati
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oficial')
def detalles_vendedor():
    return render_template('oficial.html')

@app.route('/tienda')
def desplegar_tienda():
    return render_template('tienda.html')

@app.route('/sobrenosotros')
def sobrenosotros():
    return render_template('sobrenosotros.html')

@app.route('/publicar')
def publicar():
    return render_template('publicar.html')

#ruta para que muestre mural noticias
@app.route('/noticias')
def desplegar_noticia():
    return render_template('mural-de-noticias.html')

@app.route('/servicios')
def desplegar_servicios():
    return render_template('servicio.html')

@app.route('/index')
def desplegar_index():
    return render_template('index.html')

#aca terminan las rutas del mati quedaron excelente 



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




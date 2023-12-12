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
    # Asegurarse de que el usuario esté en sesión antes de renderizar la plantilla
    if 'id_usuario' in session:
        usuario_actual = Usuario.obtener_uno_por_id(session['id_usuario'])
        return render_template('tienda.html', usuario=usuario_actual)
    else:
        return render_template('tienda.html', usuario=None)

@app.route('/sobrenosotros')
def sobrenosotros():
    return render_template('sobrenosotros.html')

@app.route('/publicar')
def publicar():
    if "id_usuario" not in session:
        return redirect('/')
    return render_template('publicar.html')

#ruta para que muestre mural noticias
@app.route('/noticias')
def desplegar_noticia():
    if 'id_usuario' in session:
        usuario_actual = Usuario.obtener_uno_por_id(session['id_usuario'])
        return render_template('mural-de-noticias.html', usuario=usuario_actual)
    else:
        return render_template('mural-de-noticias.html', usuario=None)


@app.route('/servicios')
def desplegar_servicios():
    # Asegurarse de que el usuario esté en sesión antes de renderizar la plantilla
    if 'id_usuario' in session:
        usuario_actual = Usuario.obtener_uno_por_id(session['id_usuario'])
        return render_template('servicio.html', usuario=usuario_actual)
    else:
        return render_template('servicio.html', usuario=None)

@app.route('/index')
def desplegar_index():
    return render_template('index.html')

#aca terminan las rutas del mati quedaron excelente 

#rutas para subir producto he imagenes
@app.route('/procesa/producto')
def crear_producto():
    redirect('/recienagregados')

#rutas para crear servicios
@app.route('/crear_servicio_form', methods=['POST'])
def crear_servicio_form():
    return render_template('crear_servicios.html')

#@app.route('/crear_servicio', methods=['POST'])
def crear_servicio():
    if "id_usuario" not in session:
        return redirect('/')
    if request.method == 'POST':
        # No necesitas 'id' en este formulario, elimínalo
        nombre_servicio = request.form['nombre_servicio']
        descripcion = request.form['descripcion']
        imagenes = request.form['imagenes'].split(',')
        valoracion = request.form['valoracion']

        datos_servicio = {
            'nombre_servicio': nombre_servicio,
            'descripcion': descripcion,
            'imagenes': imagenes,
            'valoracion': valoracion
        }

        # Llamar a la función para crear el servicio
        servicio_creado = servicios.crear_servicio(datos_servicio)

        if not servicio_creado:
            flash('Error al crear el servicio', 'error')
            return redirect('/procesa/producto')  # Ajusta esta redirección según tus necesidades

        # Redirigir a una nueva ruta para mostrar el servicio creado
        return redirect(f'/servicio_creado/{servicio_creado.get_id()}')

# Ruta para mostrar el servicio recién creado
@app.route('/servicio_creado/<int:id_servicio>')
def mostrar_servicio_creado(id_servicio):
    if "id_usuario" not in session:
        return redirect('/')
    # Utiliza el método de clase para obtener el servicio por ID
    servicio_creado = servicios.obtener_servicio_por_id(id_servicio)

@app.route('/producto_creado/<int:id_producto>')
def mostrar_producto_creado(id_producto):
    if "id_usuario" not in session:
        return redirect('/')
    # Utiliza el método de clase para obtener el servicio por ID
    producto_creado = servicios.obtener_producto_por_id(id_producto)
    if producto_creado:
        return render_template('producto_creado.html', producto=producto_creado)
    # Manejo de errores si no se encuentra el servicio
    flash('producto no encontrado', 'error')
    return redirect('/')
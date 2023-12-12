from flask import render_template, request, redirect, session, flash
from app_flask.modelos.modelo_tienda import Tienda
from app_flask.modelos.modelo_usuarios import Usuario
from app_flask import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#redireccion perfil
@app.route('/perfil')
def despliega_perfil():
    return render_template('perfil.html')

# redireccion a login
@app.route('/login', methods=['GET'])
def despliega_login():
    return render_template('login_registro.html')
# redireccion a registro
@app.route('/registro', methods=['GET'])
def despliega_registro():
    return render_template('login_registro.html')
# redireccion al home
@app.route('/index', methods=['GET'])
def despliega_home():
    # Verificar si hay una sesión activa
    if 'id_usuario' in session:
        usuario_actual = Usuario.obtener_uno_por_id(session['id_usuario'])
        return render_template('index.html', usuario=usuario_actual)
    else:
        return render_template('index.html', usuario=None)

#cerrar sesion
@app.route('/cerrar_sesion')
def cerrar_sesion():
    # Eliminar las variables de sesión
    session.pop('id_usuario', None)
    session.pop('nombre', None)
    session.pop('apellido', None)
    
    # Redireccionar a la página de inicio de sesión o a donde desees después de cerrar sesión
    return redirect('/index')

@app.route('/procesa/registro', methods=['POST'])
def procesa_registro():
    datos_registro = {
        "nombre": request.form.get('nombre', ''),
        "apellido": request.form.get('apellido', ''),
        "email": request.form.get('email', ''),
        "password": request.form.get('password', ''),
        "password_confirmar": request.form.get('password_confirmar', ''),
        "es_artesano": request.form.get('es_artesano', '')  # Obtener el estado del checkbox
    }

    if not Usuario.validar_registro(datos_registro):
        return redirect('/')

    password_encriptado = bcrypt.generate_password_hash(datos_registro['password'])

    # Establecer el valor de tipo_usuario según la selección del usuario
    if datos_registro['es_artesano'] == 'on':
        datos_registro['tipo_usuario'] = 1  # Es artesano
    else:
        datos_registro['tipo_usuario'] = 2  # No es artesano

    nuevo_usuario = {
        **datos_registro,
        'password': password_encriptado
    }

    id_usuario = Usuario.crear_uno(nuevo_usuario)

    session['id_usuario'] = id_usuario
    session['nombre'] = nuevo_usuario['nombre']
    session['apellido'] = nuevo_usuario['apellido']

    return redirect('/index')


@app.route('/procesa/login', methods=['POST'])
def procesa_login():
    usuario_login = Usuario.obtener_uno_por_email(request.form.get('email', ''))

    if usuario_login is None:
        flash('Este correo no existe', 'error_login')
        return redirect('/')

    if not bcrypt.check_password_hash(usuario_login.password, request.form.get('password', '')):
        flash('Credenciales incorrectas', 'error_login')
        return redirect('/')

    session['id_usuario'] = usuario_login.id
    session['nombre'] = usuario_login.nombre
    session['apellido'] = usuario_login.apellido

    return redirect('/index')

@app.route('/procesa/datos_usuario', methods=['POST'])
def procesa_datos_usuario():
    return render_template('index.html')

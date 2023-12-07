import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX


class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.id_servicio = datos['id_servicio']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.contraseña = datos['password']
        self.direccion = datos['direccion']
        self.ciudad = datos['ciudad']
        self.region = datos['region']
        self.tipo_usuario = datos['tipo_usuario']
        self.artesanias = datos['artesanias']
        self.celular = datos['celular']
        self.redes_sociales = datos['redes_sociales']
        self.pagina_web = datos['pagina_web']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

#crear un usuario

    @classmethod
    def crear_uno(cls, datos):
        tipo_usuario = 1 if datos.get('es_artesano') == 'on' else 2
        query = """
                INSERT INTO usuarios(nombre, apellido, email, password, direccion, ciudad, region, tipo_usuario)
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(direccion)s, %(ciudad)s, %(region)s, %(tipo_usuario)s);
                """
        datos_usuario = {
            'nombre': datos['nombre'],
            'apellido': datos['apellido'],
            'email': datos['email'],
            'password': datos['password'],
            'direccion': datos['direccion'],
            'ciudad': datos['ciudad'],
            'region': datos['region'],
            'tipo_usuario': tipo_usuario
        }
        return connectToMySQL(BASE_DATOS).query_db(query, datos_usuario)


    @staticmethod
    def validar_registro(datos):
        es_valido = True
        if len(datos['nombre']) < 2:
            es_valido = False
            flash('Por favor escribe tu nombre, 2 caracteres mínimos.', 'error_nombre')
        if len(datos['apellido']) < 2:
            es_valido = False
            flash('Por favor escribe tu apellido, 2 caracteres mínimos.', 'error_apellido')
        if not Usuario.validar_email(datos['email']):
            es_valido = False
            flash('Por favor ingresa un correo válido', 'error_email')
        if datos['password'] != datos['password_confirmar']:
            es_valido = False
            flash('Tus contraseñas no coinciden.', 'error_password')
        if len(datos['password']) < 8:
            es_valido = False
            flash('Por favor proporciona una contraseña, 8 caracteres mínimos.', 'error_password')
        return es_valido
    
    @staticmethod
    def validar_email(email):
        return re.match(EMAIL_REGEX, email) is not None
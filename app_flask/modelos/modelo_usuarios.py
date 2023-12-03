import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX


class Usuario:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.email = datos['email']
        self.contraseña = datos['password']
        self.direccion = datos['direccion']
        self.ciudad = datos['ciudad']
        self.region = datos['region']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

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

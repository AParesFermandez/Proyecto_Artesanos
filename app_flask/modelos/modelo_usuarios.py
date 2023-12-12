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
        self.password = datos['password']
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

    def full_name(self):
        return f"{self.nombre} {self.apellido}"

#crear un usuario

    @classmethod
    def crear_uno(cls, datos):
        tipo_usuario = 1 if datos.get('es_artesano') == 'on' else 2
        query = """
                INSERT INTO usuarios(nombre, apellido, email, password, tipo_usuario)
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(tipo_usuario)s);
                """
        datos_usuario = {
            'nombre': datos['nombre'],
            'apellido': datos['apellido'],
            'email': datos['email'],
            'password': datos['password'],
            'tipo_usuario': tipo_usuario
        }

        print("Antes del try-except")  # Impresión de prueba

        try:
            resultado = connectToMySQL(BASE_DATOS).query_db(query, datos_usuario)
            return resultado  # Podrías retornar algo para identificar que la consulta se realizó correctamente
        except Exception as e:
            print("Error al insertar usuario:", e)  # Imprimir el mensaje de error para conocer la excepción
            print("Datos de usuario:", datos_usuario)  # También puedes imprimir los datos que se intentaron insertar
            raise  # Re-raise the exception to get the traceback information

        print("Después del try-except")  # Impresión de prueba

    #metodo para capturar usuario logueado
    @classmethod
    def obtener_uno_por_id(cls, id_usuario):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos = {'id': id_usuario}
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) > 0:
            return cls(resultado[0])
        else:
            return None

    @classmethod
    def obtener_uno_por_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        datos = {'email': email}
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) > 0:
            return cls(resultado[0])
        else:
            return None

    @classmethod
    def procesa_datos_usuario(cls):
        query=  """
                INSERT INTO usuarios (nombre, email, region, celular, redes_sociales)
                VALUES (%(nombre)s, %(email)s, %(region)s, %(celular)s, %(redes_sociales)s );
                """
        return connectToMySQL(BASE_DATOS).query_db(query)

    @classmethod
    def editar_usuario(cls):
        query=  """
                UPDATED FROM usuarios(nombre, apellido, region, celular, email)
                VALUES (%(nombre)s, %(apellido)s, %(region)s, %(celular)s, %(email)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query)

    @classmethod
    def actualizar(self):
        query = """
            UPDATE usuarios 
            SET nombre = %(nombre)s, apellido = %(apellido)s,
                email = %(email)s, direccion = %(direccion)s,
                ciudad = %(ciudad)s, region = %(region)s,
                numero_contacto = %(numero_contacto)s,
                redes_sociales = %(redes_sociales)s
            WHERE id = %(id)s;
        """

        datos_usuario = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'region': self.region,
            'numero_contacto': self.celular,
            'redes_sociales': self.redes_sociales
        }

        try:
            connectToMySQL(BASE_DATOS).query_db(query, datos_usuario)
        except Exception as e:
            print("Error al actualizar usuario:", e)
            raise  # Re-raise the exception to get the traceback information

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

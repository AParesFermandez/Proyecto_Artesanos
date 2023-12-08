import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS, EMAIL_REGEX

class Venta:
    def __init__(self, datos):
        self.id = datos['id']
        self.id_usuario = datos['id_usuario']
        self.id_producto = datos['id_producto']
        self.total = datos['total']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def crear_uno(cls, datos):
        query = """
                INSERT INTO ventas(id_usuario, id_producto, total, fecha_creacion, fecha_actualizacion)
                VALUES (%(id_usuario)s, %(id_producto)s, %(total)s, %(fecha_creacion)s, %(fecha_actualizacion)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @classmethod
    def obtener_todos(cls):
        query = "SELECT * FROM ventas;"
        resultados = connectToMySQL(BASE_DATOS).query_db(query)
<<<<<<< HEAD
        ventas = [cls(resultado) for resultado in resultados]
=======
        ventas = []
        for resultado in resultados:
            ventas.append(cls(resultado))
>>>>>>> origin/main
        return ventas

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM ventas WHERE id = %(id)s;"
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])
    
    @classmethod
    def obtener_detalles(cls, datos):
        query = "SELECT * FROM detallesventa WHERE id_venta = %(id)s;"
        resultados = connectToMySQL(BASE_DATOS).query_db(query, datos)
<<<<<<< HEAD
        detalles = [DetallesVenta(resultado) for resultado in resultados]
        return detalles

=======
        detalles = []
        for resultado in resultados:
            detalles.append(resultado)
        return detalles


>>>>>>> origin/main
    @classmethod
    def actualizar(cls, datos):
        query = """
            UPDATE ventas
            SET id_usuario = %(id_usuario)s, id_producto = %(id_producto)s, total = %(total)s, fecha_creacion = %(fecha_creacion)s, fecha_actualizacion = %(fecha_actualizacion)s
            WHERE id = %(id)s;
            """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @classmethod
    def eliminar(cls, datos):
        query = "DELETE FROM ventas WHERE id = %(id)s;"
        return connectToMySQL(BASE_DATOS).query_db(query, datos)
<<<<<<< HEAD


class DetallesVenta:
    def __init__(self, datos):
        self.id = datos['id']
        self.id_venta = datos['id_venta']
        self.id_producto = datos['id_producto']
        self.cantidad = datos['cantidad']
        self.precio = datos['precio']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM detallesventa WHERE id = %(id)s;"
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])

class Curso:
    def __init__(self, datos):
        self.id = datos['id']
        self.id_usuario = datos['id_usuario']
        self.id_comentario = datos['id_comentario']
        self.titulo = datos['titulo']
        self.contenido = datos['contenido']
        self.imagenes = datos['imagenes']
        self.videos = datos['videos']
        self.categoria = datos['categoria']
        self.valoracion = datos['valoracion']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])


class Tutorial:
    def __init__(self, datos):
        self.id = datos['id']
        self.titulo = datos['titulo']
        self.contenido = datos['contenido']
        self.imagenes = datos['imagenes']
        self.videos = datos['videos']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM tutoriales WHERE id = %(id)s;"
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])


class Mensaje:
    def __init__(self, datos):
        self.id = datos['id']
        self.id_usuario = datos['id_usuario']
        self.id_artesano = datos['id_artesano']
        self.mensaje = datos['mensaje']
        self.imagen_link = datos['imagen_link']
        self.video_link = datos['video_link']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM mensajes WHERE id = %(id)s;"
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])


class Notificacion:
    def __init__(self, datos):
        self.id_notificacion = datos['id_notificacion']
        self.titulo = datos['titulo']
        self.contenido = datos['contenido']
        self.imagenes = datos['imagenes']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

    @classmethod
    def obtener_por_id(cls, datos):
        query = "SELECT * FROM noticias WHERE id_noticias = %(id_notificacion)s;"
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])


=======
>>>>>>> origin/main

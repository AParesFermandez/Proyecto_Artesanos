import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS

class Tienda:
    def __init__(self, datos):
        self.id = datos['id']
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = datos["fecha_actualizacion"]
    
    def get_id(self):
        return self.id
    
#NOTICIAS
class noticias:
    def __init__(self, datos):
        self.id_noticias = datos['id_noticias']
        self.titulo = datos['titulo']
        self.contenido = datos['contenido']
        self.imagenes = datos['imagenes']
        self.fecha_creacion = datos['fecha_creacion']
        self.fecha_actualizacion = datos['fecha_actualizacion']

class servicios:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre_servicio = datos['nombre_servicio']
        self.descripcion = datos['descripcion']
        self.imagenes = datos['imagenes']
        self.valoracion = datos['valoracion']
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = datos["fecha_actualizacion"]
        
    def get_id(self):
        return self.id
    


class productos:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id_venta = datos["id_venta"]
        self.id_categoria = datos["id_categoria"]
        self.nombre = datos["nombre"]
        self.descripcion = datos["descripcion"]
        self.precio = datos["precio"]
        self.imagen = datos["imagen"]
        self.stock = datos["stock"]
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = datos["fecha_actualizacion"]
    
    def get_id(self):
        return self.id

class categorias:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id_producto = datos["id_producto"]
        self.nommbre_categoria = datos["nombre_categoria"]
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = datos["fecha_actualizacion"]
    
    def get_id(self):
        return self.id

class carritocompras:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id_usuario = datos["id_usuario"]
        self.id_producto = datos["id_producto"]
        self.cantidad = datos["cantidad"]
        self.precio = datos["precio"]
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = datos["fecha_actualizacion"]
    
    def get_id(self):
        return self.id


class comentarios:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id_tienda = datos["id_tienda"]
        self.id_producto = datos["id_producto"]
        self.comentario = datos["comentario"]
        self.fecha_creacion = datos["fecha_creacion"]
        self.fecha_actualizacion = datos["fecha_actualizacion"]

    def get_id(self):
        return self.id
    
    
    @classmethod
    def crear_servicio(cls, datos_servicio):
        query = """
                INSERT INTO servicios (nombre_servicio, descripcion, imagenes, valoracion) 
                VALUES (%(nombre_servicio)s, %(descripcion)s, %(imagenes)s, %(valoracion)s);
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos_servicio)
        return resultado
    
    

    @classmethod
    def crear_producto(cls, datos_producto):
        query = """
                INSERT INTO productos (nombre, descripcion, imagen) 
                VALUES (%(nombre)s, %(descripcion)s, %(imagen)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos_producto)
        return resultado

    @classmethod
    def obtener_producto_por_id(cls, producto_id):
        query = """
                SELECT *
                FROM productos
                WHERE id = %(producto_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'producto_id': producto_id})
        return cls(resultado[0]) if resultado else None
    
    @classmethod
    def obtener_productos_por_categoria(cls, categorias):
        query = """
                SELECT p.*
                FROM productos AS p
                INNER JOIN productos_categorias AS pc ON p.id = pc.id_producto
                WHERE pc.id_categoria = %(categoria_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'categoria': categorias})
        if len(resultado) == 0:
            return None
        return cls(resultado[0])

    @classmethod
    def crear_comentario(cls, comentario): #creo que falta el inner join con usuarios para que pida tambien el nombre del usuario
        query = """
                INSERT INTO comentarios (id_producto, comentario, fecha_creacion) 
                VALUES (%(id_producto)s, %(comentario)s, NOW());
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'comentario': comentario})
        if len(resultado) == 0:
            return None
        return cls(resultado[0])

    """  
    @staticmethod
    def validar_crear_producto(datos):
    """  
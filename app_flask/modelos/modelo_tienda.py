import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS

class Tienda:
    def __init__(self, datos):
        self.id = datos['id']
    
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
    def crear_producto(cls, productos):
        query = """
                INSERT INTO productos (id, nombre, descripcion, precio) VALUES (%(id)s, %(nombre)s, %(descripcion)s, %(precio)s); 
                FROM productos
                WHERE id = %(productos_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'productos': productos})
        if len(resultado) == 0:
            return None
        return cls(resultado[0])
    
    @classmethod
    def obtener_producto_por_id(cls, productos):
        query = """
                SELECT *
                FROM productos
                WHERE id = %(productos_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, {'productos': productos})
        if len(resultado) == 0:
            return None
        return cls(resultado[0])
    
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
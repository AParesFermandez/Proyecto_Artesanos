import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS

class Tienda:
    def __init__(self, datos):
        self.id = datos['id']

class productos:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id = datos["id_venta"]
        self.id = datos["id_categoria"]
        self.nombre = datos["nombre"]
        self.descripcion = datos["descripcion"]
        self.precio = datos["precio"]
        self.imagen = datos["imagen"]
        self.stock = datos["stock"]
        self.fecha_creacion = ["fecha_creacion"]
        self.fecha_actualizacion = ["fecha_actualizacion"]

class categorias:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id = datos["id_producto"]
        self.nommbre_categoria = datos["nombre_categoria"]
        self.fecha_creacion = ["fecha_creacion"]
        self.fecha_actualizacion = ["fecha_actualizacion"]


class carritocompras:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id = datos["id_usuario"]
        self.id = datos["id_producto"]
        self.cantidad = datos["cantidad"]
        self.precio = datos["precio"]
        self.fecha_creacion = ["fecha_creacion"]
        self.fecha_actualizacion = ["fecha_actualizacion"]

class comentarios:
    def __init__(self, datos):
        self.id = datos["id"]
        self.id = datos["id_tienda"]
        self.id = datos["id_producto"]
        self.comentario = datos["comentario"]
        self.fecha_creacion = ["fecha_creacion"]
        self.fecha_actualizacion = ["fecha_actualizacion"]

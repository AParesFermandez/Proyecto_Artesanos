import re
from app_flask.config.mysqlconnection import connectToMySQL
from flask import flash
from app_flask import BASE_DATOS

class Tienda:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']

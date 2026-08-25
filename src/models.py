#definicion de la clase tarea 
"""
este es el que define la estructura de una tarea usando 
dataclases
"""
#importes para usar librerias 
from dataclasses import dataclass 
from datetime import datetime

@dataclass
class Tarea:
    titulo : str 
    descripcion : str = ""
    completada: bool
    fecha_creacion: datetime
    def __post_init__(self):
        if self.fecha_creacion is None:
            self.fecha_creacion = datetime.now ()
    def completar(self):
        self.completada=True
    



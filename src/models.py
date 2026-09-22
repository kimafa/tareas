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
    #def es una funcion, que funciona como un metodo (de poo), osea que lo que hace es ejecutar una accion 
    def __post_init__(self):
        if self.fecha_creacion is None:
            self.fecha_creacion = datetime.now ()
    def completar(self):
        self.completada=True
    def __str__(self):
        estado = "completada" if self.completada else "pendiente"
        return f"Tarea: {self.titulo} \n Descripion:{self.descripcion}\nEstado:{estado}\nFecha de cración{self.fecha_creacion.strftime("%d/%m/%Y, %H:%M:%S")}"
    



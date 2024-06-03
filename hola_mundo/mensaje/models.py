from django.db import models




# Video 2 
PRESENTACION =[
    ("1", "Caja"),
    ("2", "Pieza"),
    ("3", "Paquete"),
]
COLOR = [
    ("r", "Rojo"),
    ("a", "Azul"),
    ("v", "Verde"),
]
class Articulos(models.Model):
    nombre          = models.CharField(max_length=100)
    descripcion     = models.TextField("Descripcion", null=True, blank=True)
    stock           = models.IntegerField()
    presentacion    = models.CharField("Presentación", max_length=1, choices=PRESENTACION)
    color           = models.CharField(max_length=1, choices=COLOR)
 
    def __str__(self):
        return self.nombre
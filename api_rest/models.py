from django.db import models

# Create your models here.
class Comida(models.Model):
    nombre=models.CharField(max_length=30)
    origen=models.CharField(max_length=30)
    calorias = models.IntegerField()
    ingredientes = models.TextField()
    disponible = models.BooleanField(default=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.ingredientes}-{self.fecha_creado}"
        

class Bebida(models.Model):
    nombre=models.CharField(max_length=30)
    sabor=models.CharField(max_length=30)
    marca=models.CharField(max_length=30)
    calorias = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.marca}-{self.fecha_creado}"
    

class Snack(models.Model):
    nombre=models.CharField(max_length=30)
    calorias = models.IntegerField()
    ingredientes = models.TextField()
    disponible = models.BooleanField(default=True)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.fecha_creado}"   

    
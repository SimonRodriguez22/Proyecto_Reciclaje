from django.db import models

# Create your models here.

from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12, unique=True)  
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=128)  
    telefono = models.CharField(max_length=15, blank=True, null=True) 
    direccion = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(unique=True)  
    rol = models.CharField(max_length=20, choices=[
        ('admin', 'Administrador'),
        ('usuario', 'Usuario')
    ]) 
    puntos = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    valor = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre
    
class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, to_field='rut', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)  
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Registro de {self.material} por {self.usuario} - Peso: {self.peso}kg"

class Beneficio(models.Model):
    id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()
    costo=models.PositiveSmallIntegerField()
    empresa=models.CharField(max_length=80)




    

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    rut = models.CharField(max_length=200)
    SEXO = (
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('No Binario','No Binario'),
    )
    sexo = models.CharField(max_length=80,choices=SEXO,default='Masculino')
    TIPO = (
        ('Tecnico','Tecnico'),
        ('Cliente','Cliente'),
        ('Recursos_Humanos','Recursos_Humanos'),
        ('Administrador','Administrador'),
    )
    tipo = models.CharField(max_length=80,choices=TIPO,default='Cliente')
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return self.rut

class Producto(models.Model):
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    ESTADO = (
        ('NO DISPONIBLE','NO DISPONIBLE'),
        ('DISPONIBLE','DISPONIBLE'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')

class Servicio(models.Model):
    tecnico = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    hora_atencion = models.TimeField()
    cant_pers = models.IntegerField()
    precio = models.CharField(max_length=20)
    ESTADO = (
        ('PENDIENTE','PENDIENTE'),
        ('EN PROCESO','EN PROCESO'),
        ('TERMINADO','TERMINADO'),
        ('CANCELADO','CANCELADO'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    descripcion_cliente = models.TextField()
    descripcion_tecnico = models.TextField()

class Modelo(models.Model):
    codigo = models.CharField(max_length=200)
    precio = models.CharField(max_length=20)
    peso = models.TextField(max_length=100)
    largo = models.TextField(max_length=100)
    ancho = models.TextField(max_length=100)
    alto = models.TextField(max_length=100)
    descripcion = models.TextField()
    foto = models.TextField()

    def __str__(self):
        return self.codigo
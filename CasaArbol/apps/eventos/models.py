from datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Eventos(models.Model):
    autor= models.ForeignKey('auth.user',on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    contenido=models.TextField()
    imagen=models.ImageField(null=True,blank=True,upload_to='img/eventos',help_text='Selecciones una imágen para mostrar')
    fecha_creacion=models.DateField(default=timezone.now)
    modificado=models.DateField(auto_now=True)
    publicado=models.DateTimeField(blank=True,null=True)
    categoria=models.ManyToManyField('Categoria',related_name='Eventos')
    
    def publicarEvento(self):
        self.publicado=datetime.now()
        self.save
        
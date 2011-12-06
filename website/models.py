from django.db import models
from django.forms import ModelForm

# Create your models here.
class Chavales(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	fecha_nac = models.DateField()
	direccion = models.CharField(max_length=100)
	provincia = models.CharField(max_length=50,default='Bizkaia')
	municipio = models.CharField(max_length=50)
	cp = models.PositiveIntegerField()
	dni = models.CharField(max_length=10)
	nombre_padre = models.CharField(max_length=50)
	dni_padre = models.CharField(max_length=10)
	nombre_madre = models.CharField(max_length=50)
	dni_madre = models.CharField(max_length=10)
	email = models.EmailField()
	telefono = models.CharField(max_length=12)
	movil = models.CharField(max_length=12)
	observ = models.TextField()
	foto = models.ImageField(upload_to='media/',height_field=100, width_field=100)
	rama = models.ForeignKey('Ramas')
	created = models.DateTimeField(blank=False, auto_now_add=True)
	available = models.BooleanField(default=True)

	def __unicode__(self):
		return u'%s %s' % (self.nombre, self.apellidos)

class Ramas(models.Model):
	nombre = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.nombre

class ChavalesForm(ModelForm):
    class Meta:
        model = Chavales

class RamasForm(ModelForm):
    class Meta:
        model = Ramas


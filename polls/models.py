from django.db import models

class licitaciones(models.Model):
	expediente = models.CharField(max_length=60)
	inicio = models.DateField()
	tipo = models.CharField(max_length=1, choices =[
		('a', 'Licitacion'),
	    ('b', 'Acuerdo marco'),
	    ])
	detalle = models.CharField(max_length=100)
	#ubicacion = models.ForeignKey(ubicacion)
	fecha_ubicacion = models.DateField(null=True)
	fecha_chekeo = models.DateField(null=True)
	observaciones = models.CharField(max_length=1000)
	proveedor_id = models.ForeignKey('proveedor', on_delete=models.CASCADE)
	importe = models.IntegerField()
	importe_mensual = models.IntegerField()
	pac = models.IntegerField()
	inciso = models.CharField(max_length=1, choices =[
		('a', '2'),
	    ('b', '3'),
	    ('c', '4'),
	    ])


	def __str__(self):
		return self.expediente


class proveedor(models.Model):
	nombre = models.CharField(max_length=100)
	cuit = models.IntegerField()
	correo = models.EmailField()
	telefono = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.nombre


class ubicacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre



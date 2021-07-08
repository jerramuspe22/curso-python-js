from django.db import models

# Create your models here.

class Categoria(models.Model):
	descripcion=models.CharField(max_length=50)

	class Meta:
		verbose_name='Categoria'
		verbose_name_plural='Categorias'

	def __str__(self):
		return(self.descripcion)

class Producto(models.Model):
	titulo=models.CharField(max_length=50)
	imagen=models.ImageField(upload_to='JAGUARETEKAA', null=True, blank=True)
	descripcion=models.CharField(max_length=50)
	precio=models.DecimalField(max_digits=9, decimal_places=2)
	categorias=models.ManyToManyField(Categoria)
	#categorias=models.ForeignKey(Categoria, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Producto'
		verbose_name_plural='Productos'

	def __str__(self):
		return(self.titulo)
from django.shortcuts import render, redirect
from JAGUARETEKAA.models import Categoria, Producto
from .carrito import Carrito

def agregar_producto(request, producto_id):
	carrito = Carrito(request)
	producto = Producto.objects.get(id=producto_id)
	#print(producto.id)
	carrito.agregar_producto(producto=producto)

	return redirect("carrito")


def eliminar_producto(request, producto_id):
	carrito = Carrito(request)
	producto = Producto.objects.get(id=producto_id)

	carrito.eliminar_producto(producto=producto)
	
	return redirect("/")

def restar_producto(request, producto_id):
	carrito = Carrito(request)
	producto = Producto.objects.get(id=producto_id)

	carrito.restar_producto(producto=producto)
	
	return redirect("carrito")

def vaciar_carrito(request):
	carrito = Carrito(request)
	
	carrito.vaciar_carrito()
	return redirect("/") 

'''def carrito(request):
	categoria=Categoria.objects.all()
	return render(request, 'carrito/carrito.html', {
		"categorias":categoria
	})
'''
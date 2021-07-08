from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .forms import ProductoForm, CustomUserCreationForm
from .models import Categoria, Producto

# Create your views here.
def home(request):
	return render(request, "JAGUARETEKAA/home.html")

def home(request):
	categoria=Categoria.objects.all()
	
	return render(request, "JAGUARETEKAA/home.html", {
		"productos": Producto.objects.all(),
		
		"primeros_tres_productos": Producto.objects.all().order_by('-id')[:3],
		#"primeros_tres_productos": Producto.objects.all()[0:3],
		"resto_productos": Producto.objects.all()[4:10],
		"categorias":categoria
		})


def categoria(request, id):
	categoria=Categoria.objects.all()
	categoriafiltro = Categoria.objects.get(id=id)
	productos=Producto.objects.filter(categorias=categoriafiltro)
	#print(productos)
	return render(request, "JAGUARETEKAA/categoria.html", {
		'categoriafiltro': categoriafiltro,
		'productosfiltro': productos,
		'categorias': categoria
	})

def altaproducto(request):
	categoria=Categoria.objects.all()
	if request.method == "POST":
		formulario = ProductoForm(data=request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
		else:
			return render(request, "JAGUARETEKAA/altaproducto.html", {
				"categorias":categoria,
				'form': formulario
			})				

	return render(request, "JAGUARETEKAA/altaproducto.html", {
		"categorias":categoria,
		'form': ProductoForm()
		})	

def modificarproducto(request, id):
	categoria=Categoria.objects.all()
	producto = get_object_or_404(Producto, id=id)
	data = {
		'form': ProductoForm(instance=producto)
	}

	if request.method == "POST":
		formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			return redirect(to="listaproductos")
		data["form"] = formulario

	return render(request, "JAGUARETEKAA/modificarproducto.html", {
		#data, 
		'form': ProductoForm(instance=producto),
		"categorias":categoria, 
		})

def eliminarproducto(request, id):
	producto = get_object_or_404(Producto, id=id)
	producto.delete()
	return redirect(to="listaproductos")

def buscarproducto(request):
	categoria=Categoria.objects.all()
	buscar = request.GET.get('buscar')
	buscarproductos = Producto.objects.filter(titulo__icontains=buscar) | Producto.objects.filter(descripcion__icontains=buscar)
	if buscarproductos.count()==0:
		cantidadproductos = 0
	else:
		cantidadproductos = buscarproductos.count()
	return render(request, "JAGUARETEKAA/buscarproducto.html", {
		"buscarproductos":buscarproductos,
		"buscar": buscar,
		"cantidadproductos": cantidadproductos,
		"categorias":categoria
	})

def detalleproducto(request, id):
	categoria=Categoria.objects.all()
	detalleproducto=Producto.objects.get(id=id)
	return render(request, "JAGUARETEKAA/detalleproducto.html", {
		"detalleproducto": detalleproducto,
		"categorias":categoria
	})


def listaproductos(request):
	categoria=Categoria.objects.all()
	
	listaproductos=Producto.objects.all()
	return render(request, "JAGUARETEKAA/listaproductos.html", {
		'listaproductos': listaproductos,
		'categorias': categoria
	})


def acercade(request):
	categoria=Categoria.objects.all()
	return render(request, "JAGUARETEKAA/acercade.html", {
		"categorias":categoria
		})

def contacto(request):
	categoria=Categoria.objects.all()
	#if request.method == "POST":
    	#subject=request.POST["asunto"]
    	#message=request.POST["mensaje"] + " " + request.POST["email"]
    	#return render(request, "gracias.html")
    # Aca va el mailto

	return render(request, "JAGUARETEKAA/contacto.html", {
		"categorias":categoria
		})


def registro(request):
	data = {
		'form': CustomUserCreationForm()
	}

	if request.method == 'POST':
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect(to="home")
		data["form"] = formulario

	return render(request, 'registration/registro.html', data)

def carrito(request):
	categoria=Categoria.objects.all()
	return render(request, 'JAGUARETEKAA/carrito.html', {
		"categorias":categoria
	})
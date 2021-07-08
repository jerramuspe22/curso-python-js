from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from JAGUARETEKAA import views


urlpatterns =[
	path('', views.home, name="home"),
	path('categoria/<int:id>/', views.categoria, name="categoria"),
	path('altaproducto', views.altaproducto, name="altaproducto"),
	path('modificarproducto/<int:id>/', views.modificarproducto, name="modificarproducto"),
	path('eliminarproducto/<int:id>/', views.eliminarproducto, name="eliminarproducto"),
	path('buscarproducto', views.buscarproducto, name="buscarproducto"),
	path('detalleproducto/<int:id>', views.detalleproducto, name="detalleproducto"),
	path('listaproductos', views.listaproductos, name="listaproductos"),

	path('acercade/', views.acercade, name="acercade"),
	path('contacto/', views.contacto, name="contacto"),
	path('registro/', views.registro, name="registro"),
	path('carrito/', views.carrito, name="carrito"),

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
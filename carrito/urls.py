from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "carrito"

urlpatterns =[
	path("agregar_producto/<int:producto_id>/", views.agregar_producto, name="agregar_producto"),
	path("eliminar_producto/<int:producto_id>/", views.eliminar_producto, name="eliminar_producto"),
	path("restar_producto/<int:producto_id>/", views.restar_producto, name="restar_producto"),
	path("vaciar_carrito/", views.vaciar_carrito, name="vaciar_carrito"),
	#path('carrito/', views.carrito, name="carrito"),
]
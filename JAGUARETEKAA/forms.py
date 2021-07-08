from django import forms
from .models import Producto, Categoria
from django.contrib.auth.forms import UserCreationForm

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
	pass	
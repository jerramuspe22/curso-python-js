class Carrito:
	def __init__(self, request):
		self.request = request
		self.session = request.session
		carrito = self.session.get("carrito")
		if not carrito:
			carrito = self.session["carrito"] = {}
		#else:
		self.carrito=carrito
	

	def actualizar_carrito(self):
		self.session["carrito"] = self.carrito
		self.session.modified = True


	def agregar_producto(self, producto):
		print("suma")
		if(str(producto.id) not in self.carrito.keys()):
			self.carrito[producto.id] = {
				"producto_id": producto.id,
				"titulo": producto.titulo,
				"precio": str(producto.precio),
				"cantidad": 1
			}
		else:
			for key, value in self.carrito.items():
				if key == str(producto.id):
					value["cantidad"] = value["cantidad"] + 1
					break
		self.actualizar_carrito()

	def eliminar_producto(self, producto):
		producto.id = str(producto.id)
		if producto.id in self.carrito:
			del self.carrito[producto.id]
			self.actualizar_carrito()

	def restar_producto(self, producto):
		print("resta")
		for key, value in self.carrito.items():
			if key == str(producto.id):
				value["cantidad"] = value["cantidad"] - 1
				if value["cantidad"] < 1:
					self.eliminar_producto(producto)
				break
		self.actualizar_carrito()

	def vaciar_carrito():
		carrito = self.session["carrito"] = {}
		self.session.modified = True
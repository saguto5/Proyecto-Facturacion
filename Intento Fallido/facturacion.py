class Facturacion(baseDeDatos):

	def __init__ (self):
		pass

	def buscarID(nombre):
		if self.nombre == "camisa":
			self.id = 1
		elif self.nombre == "pantalon":
			self.id == 2


	def CalcularSubtotal(self,id):
		precio = select_id_precio(self,self.id)
		if select_id_nombre(self, self.id) == "camisa":
			subtotal = precio/(1+(16/100))
		else:
			subtotal = precio/(1+(19/100))

"""	
	def CalcularIva(self,id):
		iva = ""
		if select_id_nombre(self, self.id) == "camisa":
			iva = "16%"
		else:
			select_id_nombre(self,self.id) == "pantalon":
			iva = "19%"
	
"""






















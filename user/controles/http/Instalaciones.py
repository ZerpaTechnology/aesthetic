from controlador import Controlador
class Sesion(Controlador):
	def __init__(self,data):
		Controlador.__init__(self,data)
		self.add_vista("administrativo")

		self.servir()
	
	def Coordinaciones(self):
		self.add_vista("coordinaciones")
		self.servir()
	def Organizaciones(self):
		self.add_vista("organizaciones")
		self.servir()
	def Instalaciones(self):
		self.add_vista("instalaciones")
		self.servir()
	

		
		
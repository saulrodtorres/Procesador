#Para la matriz de transicion hay que utilizar un diccionario
#key = tupla | value = tupla --> {(estado, caracter): (estado, accion), ...}

class Lexico:
	def __init__(self,p_inputFile):
		self.file = open(p_inputFile, 'r')
		#self.tokensFile = open('fichero_tokens.txt', 'a')
		
	def getToken():
		estado = 0
		while estado < 10:
			c = self.file.read(1)
			#estado = diccionario(estado, c)
			#accion = diccionario(estado, c)
			if estado is null:
				error()
			else:
				switch(){}

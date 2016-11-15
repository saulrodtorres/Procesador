#Para la matriz de transicion hay que utilizar un diccionario
#key = tupla | value = tupla --> {(estado, caracter): (estado, accion), ...}

class Lexico:
	MT = {(0,0): (1,L), (0,1): (2,L)}
	
	def __init__(self, p_inputFile):
		self.file = open(p_inputFile, 'r')
		#self.tokensFile = open('fichero_tokens.txt', 'a')

	def filter(c):
		#Vamos a mirar que caracter recibe para entrar en la MT
		if c == '=':
			return 0
		elif c == '!':
			return 1
		elif c == '|':
			return 2
		elif c == '+':
			return 3
		elif c.isdigit():
			return 4
		elif c
		
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

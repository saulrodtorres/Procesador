#Para la matriz de transicion hay que utilizar un diccionario
#key = tupla | value = tupla --> {(estado, caracter): (estado, accion), ...}

class Lexico:


	MT = {(0,0):(1,"L"), (0,1):(2,"L"), (0,2):(3,"L"), (0,3):(4,"L"), (0,4):(5,"A"), #Estado 0
		(0,5):(6,"L"), (0,6):(7,"F"), (0,7):(8,"L"), (0,8):(10,"G6"), (0,9):(11,"G7"),
		(0,10):(12,"G14"), (0,11):(13,"G15"), (0,12):(14,"G4"), (0,13):(15,"G3"), (0,14):(16,"G5"),
		(0,15):(26,"G2"), (0,16):(27,"G1"), (0,17):(0,"L"), (0,18):(None,"Err"), (0,19):(None,"Err"),
		(1,0):(17,"G8"), (1,1):(18,"G9"), (1,2):(18,"G9"), (1,3):(18,"G9"), (1,4):(18,"G9"), #Estado 1
		(1,5):(18,"G9"), (1,6):(18,"G9"), (1,7):(18,"G9"), (1,8):(18,"G9"), (1,9):(18,"G9"),
		(1,10):(18,"G9"), (1,11):(18,"G9"), (1,12):(18,"G9"), (1,13):(18,"G9"), (1,14):(18,"G9"),
		(1,15):(18,"G9"), (1,16):(18,"G9"), (1,17):(18,"G9"), (1,18):(18,"G9"), (1,19):(18,"G9"),
		(2,0):(19,"G10"), (2,1):(None,"Err"), (2,2):(None,"Err"), (2,3):(None,"Err"), (2,4):(None,"Err"), #Estado 2
		(2,5):(None,"Err"), (2,6):(None,"Err"), (2,7):(None,"Err"), (2,8):(None,"Err"), (2,9):(None,"Err"),	
		(2,10):(None,"Err"), (2,11):(None,"Err"), (2,12):(None,"Err"), (2,13):(None,"Err"), (2,14):(None,"Err"), 
		(2,15):(None,"Err"), (2,16):(None,"Err"), (2,17):(None,"Err"), (2,18):(None,"Err"), (2,19):(None,"Err"),
		(3,0):(None,"Err"), (3,1):(None,"Err"), (3,2):(20,"G11"), (3,3):(None,"Err"), (3,4):(None,"Err"), #Estado 3
		(3,5):(None,"Err"), (3,6):(None,"Err"), (3,7):(None,"Err"), (3,8):(None,"Err"), (3,9):(None,"Err"),
		(3,10):(None,"Err"), (3,11):(None,"Err"), (3,12):(None,"Err"), (3,13):(None,"Err"), (3,14):(None,"Err"),
		(3,15):(None,"Err"), (3,16):(None,"Err"), (3,17):(None,"Err"), (3,18):(None,"Err"), (3,19):(None,"Err"),
		(4,0):(21,"G12"), (4,1):(22,"G13"), (4,2):(22,"G13"), (4,3):(22,"G13"), (4,4):(22,"G13"), #Estado 4
		(4,5):(22,"G13"), (4,6):(22,"G13"), (4,7):(22,"G13"), (4,8):(22,"G13"), (4,9):(22,"G13"),
		(4,10):(22,"G13"), (4,11):(22,"G13"), (4,12):(22,"G13"), (4,13):(22,"G13"), (4,14):(22,"G13"),
		(4,15):(22,"G13"), (4,16):(22,"G13"), (4,17):(22,"G13"), (4,18):(22,"G13"), (4,19):(22,"G13"),
		(5,0):(23,"C"), (5,1):(23,"C"), (5,2):(23,"C"), (5,3):(23,"C"), (5,4):(5,"B"), #Estado 5
		(5,5):(23,"C"), (5,6):(23,"C"), (5,7):(23,"C"), (5,8):(23,"C"), (5,9):(23,"C"),
		(5,10):(23,"C"), (5,11):(23,"C"), (5,12):(23,"C"), (5,13):(23,"C"), (5,14):(23,"C"),
		(5,15):(23,"C"), (5,16):(23,"C"), (5,17):(23,"C"), (5,18):(23,"C"), (5,19):(23,"C"),
		(6,0):(None,"Err"), (6,1):(None,"Err"), (6,2):(None,"Err"), (6,3):(None,"Err"), (6,4):(None,"Err"), #Estado 6
		(6,5):(24,"E"), (6,6):(None,"Err"), (6,7):(None,"Err"), (6,8):(None,"Err"), (6,9):(None,"Err"),
		(6,10):(None,"Err"), (6,11):(None,"Err"), (6,12):(None,"Err"), (6,13):(None,"Err"), (6,14):(None,"Err"),
		(6,15):(None,"Err"), (6,16):(None,"Err"), (6,17):(None,"Err"), (6,18):(None,"Err"), (6,19):(None,"Err"),
		(7,0):(25,"I"), (7,1):(25,"I"), (7,2):(25,"I"), (7,3):(25,"I"), (7,4):(7,"H"), #Estado 7
		(7,5):(25,"I"), (7,6):(7,"H"), (7,7):(25,"I"), (7,8):(25,"I"), (7,9):(25,"I"),
		(7,10):(25,"I"), (7,11):(25,"I"), (7,12):(25,"I"), (7,13):(25,"I"), (7,14):(25,"I"),
		(7,15):(25,"I"), (7,16):(25,"I"), (7,17):(25,"I"), (7,18):(25,"I"), (7,19):(25,"I"),
		(8,0):(None,"Err"), (8,1):(None,"Err"), (8,2):(None,"Err"), (8,3):(None,"Err"), (8,4):(None,"Err"), #Estado 8
		(8,5):(None,"Err"), (8,6):(None,"Err"), (8,7):(None,"Err"), (8,8):(None,"Err"), (8,9):(None,"Err"),
		(8,10):(None,"Err"), (8,11):(None,"Err"), (8,12):(None,"Err"), (8,13):(None,"Err"), (8,14):(None,"Err"),
		(8,15):(None,"Err"), (8,16):(None,"Err"), (8,17):(None,"Err"), (8,18):(None,"Err"), (8,19):(None,"Err"),
		(9,0):(9,"L"), (9,1):(9,"L"), (9,2):(9,"L"), (9,3):(9,"L"), (9,4):(9,"L"), #Estado 9
		(9,5):(9,"L"), (9,6):(9,"L"), (9,7):(9,"L"), (9,8):(9,"L"), (9,9):(9,"L"),
		(9,10):(9,"L"), (9,11):(9,"L"), (9,12):(9,"L"), (9,13):(9,"L"), (9,14):(9,"L"),
		(9,15):(0,"L"), (9,16):(27,"G1"), (9,17):(9,"L"), (9,18):(9,"L"), (9,19):(9,"L")}

	
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
		elif c == '"':
			return 5
		elif c.isalpha():
			return 6
		elif c == '/':
			return 7
		elif c == '(':
			return 8
		elif c == ')':
			return 9
		elif c == '{':
			return 10
		elif c == '}':
			return 11
		elif c == ';':
			return 12
		elif c == ',':
			return 13
		elif c == '-':
			return 14
		elif c == None:
			return 15
		elif c == '':
			return 16
		elif c.isalnum:
			return 18
		elif c == '_':
			return 19
		elif c == '\t' or c == ' ':
			return 17


	def get_token():
		estado = 0
		while estado < 10:
			c = self.file.read(1)
			accion = MT[(estado, filter(c))][1]
			estado = MT[(estado, filter(c))][0]
			if estado is None:
				pass
			else:
				if accion == 'A':
					valor = c
				elif accion == 'B':
					valor = valor * 10 + c
				elif accion == 'C':
					if valor < 2**15:
						return (14, valor)
					else:
						pass

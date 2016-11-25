class Lexico:


	MT = {	# Estado 0
		(0,0):(1,"L"), (0,1):(2,"L"), (0,2):(3,"L"), (0,3):(4,"L"), 
		(0,4):(5,"A"), (0,5):(6,"J"), (0,6):(7,"H"), (0,7):(8,"L"),
		(0,8):(10,"G6"), (0,9):(11,"G7"), (0,10):(12,"G14"), 
		(0,11):(13,"G15"), (0,12):(14,"G4"), (0,13):(15,"G3"),
		(0,14):(16,"G5"), (0,15):(26,"G2"), (0,16):(27,"G1"), 
		(0,17):(0,"L"), (0,18):(None,"Err"), (0,19):(None,"Err"),
		# Estado 1
		(1,0):(17,"G8"), (1,1):(18,"G9"), (1,2):(18,"G9"), 
		(1,3):(18,"G9"), (1,4):(18,"G9"), (1,5):(18,"G9"),
		(1,6):(18,"G9"), (1,7):(18,"G9"), (1,8):(18,"G9"), 
		(1,9):(18,"G9"), (1,10):(18,"G9"), (1,11):(18,"G9"),
		(1,12):(18,"G9"), (1,13):(18,"G9"), (1,14):(18,"G9"),
		(1,15):(18,"G9"), (1,16):(18,"G9"), (1,17):(18,"G9"),
		(1,18):(18,"G9"), (1,19):(18,"G9"),
		# Estado 2
		(2,0):(19,"G10"), (2,1):(None,"Err"), (2,2):(None,"Err"),
		(2,3):(None,"Err"), (2,4):(None,"Err"),	(2,5):(None,"Err"),
		(2,6):(None,"Err"), (2,7):(None,"Err"), (2,8):(None,"Err"),
		(2,9):(None,"Err"), (2,10):(None,"Err"), (2,11):(None,"Err"),
		(2,12):(None,"Err"), (2,13):(None,"Err"), (2,14):(None,"Err"),
		(2,15):(None,"Err"), (2,16):(None,"Err"), (2,17):(None,"Err"),
		(2,18):(None,"Err"), (2,19):(None,"Err"),
		# Estado 3
		(3,0):(None,"Err"), (3,1):(None,"Err"), (3,2):(20,"G11"),
		(3,3):(None,"Err"), (3,4):(None,"Err"), (3,5):(None,"Err"),
		(3,6):(None,"Err"), (3,7):(None,"Err"), (3,8):(None,"Err"),
		(3,9):(None,"Err"), (3,10):(None,"Err"), (3,11):(None,"Err"),
		(3,12):(None,"Err"), (3,13):(None,"Err"), (3,14):(None,"Err"),
		(3,15):(None,"Err"), (3,16):(None,"Err"), (3,17):(None,"Err"),
		(3,18):(None,"Err"), (3,19):(None,"Err"),
		# Estado 4
		(4,0):(21,"G12"), (4,1):(22,"G13"), (4,2):(22,"G13"),
		(4,3):(22,"G13"), (4,4):(22,"G13"), (4,5):(22,"G13"),
		(4,6):(22,"G13"), (4,7):(22,"G13"), (4,8):(22,"G13"),
		(4,9):(22,"G13"), (4,10):(22,"G13"), (4,11):(22,"G13"),
		(4,12):(22,"G13"), (4,13):(22,"G13"), (4,14):(22,"G13"),
		(4,15):(22,"G13"), (4,16):(22,"G13"), (4,17):(22,"G13"),
		(4,18):(22,"G13"), (4,19):(22,"G13"),
		# Estado 5
		(5,0):(23,"C"), (5,1):(23,"C"), (5,2):(23,"C"), (5,3):(23,"C"),
		(5,4):(5,"B"), (5,5):(23,"C"), (5,6):(23,"C"), (5,7):(23,"C"),
		(5,8):(23,"C"), (5,9):(23,"C"), (5,10):(23,"C"),
		(5,11):(23,"C"), (5,12):(23,"C"), (5,13):(23,"C"),
		(5,14):(23,"C"), (5,15):(23,"C"), (5,16):(23,"C"),
		(5,17):(23,"C"), (5,18):(23,"C"), (5,19):(23,"C"),
		# Estado 6
		(6,0):(6,"D"), (6,1):(6,"D"), (6,2):(6,"D"), (6,3):(6,"D"),
		(6,4):(6,"D"), (6,5):(24,"E"), (6,6):(6,"D"), (6,7):(6,"D"),
		(6,8):(6,"D"), (6,9):(6,"D"), (6,10):(6,"D"), (6,11):(6,"D"),
		(6,12):(6,"D"), (6,13):(6,"D"), (6,14):(6,"D"),
		(6,15):(None,"Err"), (6,16):(None,"Err"), (6,17):(6,"D"),
		(6,19):(6,"D"),
		# Estado 7
		(7,0):(25,"I"), (7,1):(25,"I"), (7,2):(25,"I"), (7,3):(25,"I"),
		(7,4):(7,"F"), (7,5):(25,"I"), (7,6):(7,"F"), (7,7):(25,"I"),
		(7,8):(25,"I"), (7,9):(25,"I"),	(7,10):(25,"I"),
		(7,11):(25,"I"), (7,12):(25,"I"), (7,13):(25,"I"),
		(7,14):(25,"I"), (7,15):(25,"I"), (7,16):(25,"I"), 
		(7,17):(25,"I"), (7,18):(25,"I"), (7,19):(7,"F"),
		# Estado 8
		(8,0):(None,"Err"), (8,1):(None,"Err"), (8,2):(None,"Err"),
		(8,3):(None,"Err"), (8,4):(None,"Err"), (8,5):(None,"Err"),
		(8,6):(None,"Err"), (8,7):(9,"L"), (8,8):(None,"Err"),
		(8,9):(None,"Err"), (8,10):(None,"Err"), (8,11):(None,"Err"),
		(8,12):(None,"Err"), (8,13):(None,"Err"), (8,14):(None,"Err"),
		(8,15):(None,"Err"), (8,16):(None,"Err"), (8,17):(None,"Err"),
		(8,18):(None,"Err"), (8,19):(None,"Err"),
		# Estado 9
		(9,0):(9,"L"), (9,1):(9,"L"), (9,2):(9,"L"), (9,3):(9,"L"),
		(9,4):(9,"L"), (9,5):(9,"L"), (9,6):(9,"L"), (9,7):(9,"L"),
		(9,8):(9,"L"), (9,9):(9,"L"), (9,10):(9,"L"), (9,11):(9,"L"),
		(9,12):(9,"L"), (9,13):(9,"L"), (9,14):(9,"L"),	(9,15):(0,"L"),
		(9,16):(27,"G1"), (9,17):(9,"L"), (9,18):(9,"L"), (9,19):(9,"L")
	}

	
	def __init__(self, p_inputFile):
		self.file = open(p_inputFile, 'r')


	def filter(self, c):
		# Metodo para filtrar el caracter recibido en un numero.
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
		elif c is None:
			return 15
		elif c == '':
			return 16
		elif c == '_':
			return 19
		elif c == '\t' or c == ' ':
			return 17


	def get_token(self):
		estado = 0
		while estado < 10:
			c = self.file.read(1)
			accion = self.MT[(estado, self.filter(c))][1]
			estado = self.MT[(estado, self.filter(c))][0]
			if estado is None:
				# Tratar error
				# Hay que implementar el GE
				return None
			else:
				if accion == 'A':
					valor = c
				elif accion == 'B':
					valor = valor * 10 + c
				elif accion == 'C':
					if valor < 2**15:
						self.gen_token("INT", valor)
						return (14, valor)
					else:
						# Tratar error
						# Hay que implementar el GE
						continue
				elif accion == 'D':
					cadena += c
				elif accion == 'E':
					self.gen_token("CAD", cadena)
					return (15, cadena)
				elif accion == 'F':
					palabra += c
				elif accion == 'H':
					palabra = ''
				elif accion == 'I':
					# Depende de la TS
					continue
				elif accion == 'J':
					cadena = ''
				elif accion == 'L':
					continue
				elif accion == 'G1':
					self.gen_token("EOF", "")
					return (1,)
				elif accion == 'G2':
					self.gen_token("CR", "")
					return (2,)
				elif accion == 'G3':
					self.gen_token("COMA", "")
					return (3,)
				elif accion == 'G4':
					self.gen_token("PYC", "")
					return (4,)
				elif accion == 'G5':
					self.gen_token("MENOS", "")
					return (5,)
				elif accion == 'G6':
					self.gen_token("P1", "")
					return (6,)
				elif accion == 'G7':
					self.gen_token("P2", "")
					return (7,)
				elif accion == 'G8':
					self.gen_token("IG", "")
					return (8,)
				elif accion == 'G9':
					self.gen_token("ASIG", "")
					return (9,)
				elif accion == 'G10':
					self.gen_token("DESIG", "")
					return (10,)
				elif accion == 'G11':
					self.gen_token("OR", "")
					return (11,)
				elif accion == 'G12':
					self.gen_token("SOP", "")
					return (12,)
				else:
					self.gen_token("MAS", "")
					return (13,)

	def gen_token(self, code, value):
		tokensFile = open('fichero_tokens.txt', 'a')
		tokensFile.write("<%s, %s>\n" %(code, value))
		tokensFile.close()

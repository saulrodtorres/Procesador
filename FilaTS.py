
class FilaTS():

    def __init__(self,lex):

    	self.lexema = lex
    	self.tipo = ''
    	self.tipoRetorno = ''
    	self.numeroParametros = 0
    	self.vectorParametros = []
    	#self.modoPasoParametros = '' #no sabemos si lo vamos a usar
    	self.pos = 0

    def getTipo(self):
    	return self.tipo
    def setTipo(self,t)
    	self.tipo = t 
	def getTipoRetorno(self):
    	return self.tipoRetorno
    def setTipoRetorno(self,tr)
    	self.tipoRetorno = tr 
    def getVectorParametros(self):
    	return self.vectorParametros
    def setVectorParametros(self,vp)
    	self.vectorParametros = vp
    def getNumeroParametros(self):
    	return self.numeroParametros
    def setNumeroParametros(self,n):
    	self.numeroParametros = n
	def getPos(self):
    	return self.modoPasoParametros
    def setPos(self,p)
    	self.modoPasoParametros = p 




    	

class Stack:

    def __init__(self):
        self.items = []
        #Los atributos sera una pila de vectores
        #[ [pos0,  pos1,pos2,       pos3,            pos4,            pos5]]
        #[ [lexema,tipo,tipoRetorno,numeroParametros,vectorParametros,pos]]
        self.atributos = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def setAtributoTipo(self,tipo,pos):
        self.atributos[len(self.items)-1-pos][1]=tipo

    def getAtributoTipo(self,pos):
        #pos = 0 es la cima de la pila
        return self.atributos[len(self.items)-1-pos][1]
    
    def setAtributoRetorno(self,):
        self.atributos[len(self.items)-1-pos][2]
    
    def getAtributoRetorno(self,):
        return self.atributos[len(self.items)-1-pos][2]
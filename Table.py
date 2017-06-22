from FilaTS import FilaTS
"""
Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""

class Table():

    def __init__(self, idTable):
        #lexema:FilaTS
        self.diccionario_lexemas = {}
        self.exists = True
        self.idTable = idTable
        self.posicion = 1
    def delete(self):
        """This ufnction marks this table as deleted"""
        self.exists = False
        return True

    def exist(self):
        """Checks if this table is deleted or not"""
        return self.exists

    def add(self, lex):
        """Adds lex to this table.
        Returns the position of the lex if everything went OK. Otherwise, it returns False"""
        objeto_filaTS = FilaTS(lex);

        if lex in self.diccionario_lexemas:            
            return self.diccionario_lexemas[lex].getPos()
        else:            
            objeto_filaTS.setPos(self.posicion)
            self.posicion = self.posicion + 1
            self.diccionario_lexemas[lex] = objeto_filaTS
            return self.diccionario_lexemas[lex].getPos()

    def setType(self, lex, type):
        """Sets the type of lex.
        Returns True if everything went OK. Otherwise, returns False"""

        if lex in self.diccionario_lexemas:
            self.diccionario_lexemas[lex].setTipo(type)
            return True
        else:
            return False

    def getType(self, lex):
        "Returns the type of lex"

        return self.diccionario_lexemas[lex].getTipo()
    def getParams(self,lex):
        return self.diccionario_lexemas[lex].getVectorParametros()
    def setParams(self,lex,vector):    
        self.diccionario_lexemas[lex].setVectorParametros(vector)                
    def getRetorno(self,lex):
        return self.diccionario_lexemas[lex].getTipoRetorno()
    def setRetorno(self,lex,tipo):    
        self.diccionario_lexemas[lex].setTipoRetorno(tipo)
    def getParams(self,lex):
        return self.diccionario_lexemas[lex].getVectorParametros()
    def setParams(self,lex,vector):    
        self.diccionario_lexemas[lex].setTipo(vector)
    def getNumeroParametros(self,lex):
        return self.diccionario_lexemas[lex].getNumeroParametros()
    def setNumeroParametros(self,lex,n):    
        self.diccionario_lexemas[lex].setNumeroParametros(n)             
    def contains(self, lex):
        "Checks if lex is in the table or not"

        return self.diccionario_lexemas.has_key[lex]

    def write(self, path):
        "Writes the contents of this table to the file pointed to by path"
"""
        if self.exist():
            f = open(path, 'a')
            f.write('CONTENIDO DE LA TABLA # ' + str(self.id) + ':\n')
            for e in self.diccionario_lexemas.keys():
                f.write('* LEXEMA: \'' + str(e) + '\'\n')
                if self.diccionario_lexemas[e] != '':
                    f.write(' ATRIBUTOS:\n')
                    f.write(' + tipo: \'' + self.diccionario_lexemas[e] + '\'' )
                f.write('\n')
            f.write('\n\n\n')
            f.close()
            return True
        else:
            return False
"""
    return False

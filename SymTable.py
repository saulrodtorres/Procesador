"""
Software distributed under a Creative Commons Attribution-ShareAlike 3.0 Unported license. This allows you to adapt, copy, distribute and transmit the work while crediting the author of the original work and sharing under the same or similar license.
Full legal text of this license can be found on http://creativecommons.org/licenses/by-sa/3.0/legalcode
"""

from Table import Table


class SymTable():

    def __init__(self):
        self.tables = []
        self.nextId = 0
        # Tabla de trabajo actual
        self.workingTable = 0
        # Modo de uso
        # decZone = 0 -> Zona de sentencias
        # decZone = 1 -> Zona de declaracion
        self.decZone = 0

    def newTable(self):
        "Creates a new symbol table and returns its ID"
        a = Table(self.nextId)
        self.tables.append(a)
        self.nextId = self.nextId + 1
        return self.nextId - 1

    def destroyTable(self, id):
        "Deletes table ID"
        self.tables[id].delete()
        pass

    def add(self, id, lex):
        """Adds the lexem lex to table ID.
        Returns the ID of the lex if everything is OK or false if lex already exist on that table"""
        return self.tables[id].add(lex)

    def addParams (self,id,lex,vector):
        """Adds the params in a vector form"""
        self.tables[id].setParams(lex,vector)
    def addReturnType (self,id,lex,type):
        """Adds the return type"""
        self.tables[id].setRetorno(type)
    def addNumeroParametros (self,id,lex,n):
        """Adds the number of Param"""
        self.tables[id].setParams(n)


    #faltan los get    
    def existTable(self, id):
        "Checks wether Table ID exists or not"
        a = self.tables[id]
        if not a or not a.exist():
            return False
        else:
            return True 

    def addType(self, id, lex, type):
        """Sets the type of lex in table id to type.
        Returns True if everything is OK and false if lex does not exist on that table"""

        return self.tables[id].setType(lex, type)

    def getType(self, id, lex):
        """Returns the type of lex on table id"""

        return self.tables[id].getType(lex)

    def existsEntry(self, id, lex):
        """checks wether lex exists on table id"""
        return self.tables[id].contains(lex)

    def writeTable(self, path):
        """This function writes the content of all the tables into file pointed by path"""

        for tab in self.tables:
            tab.write(path)
        return True



class Stack:

    def __init__(self):
        self.items = []

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

class Sintactico:

    Term = [
        "true", "false", "if", "while", "var", "bool", "chars", "int",
        "function", "prompt", "write", "return", "numero", "cadena",
        "booleano", "cr", "$", "id", ",", ";", "(", ")", "-", "==", "=",
        "!=", "||", "+=", "+", "{", "}"
        ]

    def __init__(self, p_lexic, p_symTable):
        self.AL = p_lexic
        # Semantico en un futuro
        self.TS = p_symTable
        self.pila = Stack()
        # Inicializar la pila con los valores adecuados
        self.pila.push("$") 
        self.pila.push("A") 
        a = self.AL.get_token()
        X = "A"
        while X is not "$":
            X = self.pila.pop() 
            if X in self.Term:
                # Palabras Reservadas
                if (X == "true" and a[0] == 19):        
                    a = self.AL.get_token()
                elif (X == "false" and a[0] == 20):
                    a = self.AL.get_token()
                elif (X == "if" and a[0] == 21):
                    a = self.AL.get_token()
                elif (X == "while" and a[0] == 22):
                    a = self.AL.get_token()
                elif (X == "var" and a[0] == 23):
                    a = self.AL.get_token()
                elif (X == "bool" and a[0] == 24):
                    a = self.AL.get_token()
                elif (X == "chars" and a[0] == 25):
                    a = self.AL.get_token()
                elif (X == "int" and a[0] == 26):
                    a = self.AL.get_token()
                elif (X == "function" and a[0] == 27):
                    a = self.AL.get_token()
                elif (X == "prompt" and a[0] == 28):
                    a = self.AL.get_token()
                elif (X == "write" and a[0] == 29):
                    a = self.AL.get_token()
                elif (X == "return" and a[0] == 30):
                    a = self.AL.get_token()
                #Resto
                elif (X == "numero" and a[0] == 14):
                    a =self.AL.get_token()
                elif (X == "cadena" and a[0] == 15):
                    a=self.AL.get_token()
                elif (X=="id" and a[0]==18):
                    a=self.AL.get_token()
                elif (X=="$" and a[0]==1):
                    a=self.AL.get_token()
                elif (X=="cr" and a[0]==2):
                    a=self.AL.get_token()
                elif (X=="," and a[0]==3):
                    a=self.AL.get_token()
                elif (X==";" and a[0]==4):
                    a=self.AL.get_token()
                elif (X=="-" and a[0]==5):
                    a=self.AL.get_token()
                elif (X=="(" and a[0]==6):
                    a=self.AL.get_token()
                elif (X==")" and a[0]==7):
                    a=self.AL.get_token()
                elif (X=="==" and a[0]==8):
                    a=self.AL.get_token()
                elif (X=="=" and a[0]==9):
                    a=self.AL.get_token()
                elif (X=="!=" and a[0]==10):
                    a=self.AL.get_token()
                elif (X=="||" and a[0]==11):
                    a=self.AL.get_token()
                elif (X=="+=" and a[0]==12):
                    a=self.AL.get_token()
                elif (X=="+" and a[0]==13):
                    a=self.AL.get_token()
                elif (X=="{" and a[0]==16):
                    a=self.AL.get_token()
                elif (X=="}" and a[0]==17):
                    a=self.AL.get_token()
                else:
                      # TODO: Tratar Error
                      continue
            else:
                # ya se hace un X=self.pila.pop() arriba
                var = self.M.has_key((X,a[0]))
                print("----------------")
                print(var)
                print(X)
                print(a[0])
                if var is True:
                    for elem in self.M[X,a[0]]:
                        print(elem)
                        self.pila.push(elem)

        # Cuando termina el while
        if a is "$":
            print("AQUI 1")
            return
    #M (NoTerminal,Terminal,valor):(Token ordenado alreves)
    M = { 
        ("A", 2): ("A", "cr"),#2:cr
        ("A", 1): ("eof",) ,#eof
        ("A",18): ("A", "cr", "B"),#18:id
        ("A",21): ("A", "cr", "B"),#19:PR, 2:if
        ("A",22): ("A", "cr", "B"),#19:PR, 3:while
        ("A",23): ("A", "cr", "B"),#19:PR, 4:var
        ("A",27): ("A", "cr", "C"),#19:PR, 8:function
        ("A",28): ("A", "cr", "B"),#19:PR, 9:prompt
        ("A",29): ("A", "cr", "B"),#19:PR, 10:write
        ("A",30): ("A", "cr", "B"),#19:PR, 11:return

        ("B",18): ("D",),#18:id 
        ("B",21): ("D", ")", "I", "(", "if"),#19:PR, 2:if
        ("B",22): ("}", "E", "B", "E", "{", "E", ")", "L", "(", "while"),#19:PR, 3:while
        ("B",23): ("id", "T", "var"),#19:PR, 4:var
        ("B",28): ("D",),#19:PR, 9:prompt
        ("B",29): ("D",),#19:PR, 10:write
        ("B",30): ("D",),#19:PR, 11:return

        ("C",27): ("}", "E", "B", "E", "{", "E", ")", "N", "(", "id", "T", "function"),

        ("D",18): ("G", "id"),#18:id
        ("D",28): (")", "id", "(", "prompt"),#19:PR, 9:prompt
        ("D",29): (")", "I", "(", "write"),#19:PR, 10:write
        ("D",30): ("L", "return"),#19:PR, 11:return                    

        ("E",2 ): ("E", "cr"),#2:cr
        ("E",16): ("lambda",),#16:abrir llave           
        ("E",17): ("lambda",),#17:cerrar llave
        ("E",18): ("lambda",),#18:id
        ("E",21): ("lambda",),#19:PR
        ("E",22): ("lambda",),#19:PR, 3:while
        ("E",23): ("lambda",),#19:PR, 4:var
        ("E",28): ("lambda",),#19:PR, 9:prompt
        ("E",29): ("lambda",),#19:PR, 10:write
        ("E",30): ("lambda",),#19:PR, 11:return

        ("G",6): (")", "LL", "("),#abrir parentesis
        ("G",9): ("I","="),#9:igual 

        ("I",19):("IP", "II"),      
        ("I",20):("IP", "II"),
        ("I",15):("IP", "II"),
        ("I",18):("IP", "II"), 
        ("I",14):("IP", "II"),

        ("II", 19):("IIP", "III"),      
        ("II", 20):("IIP", "III"),
        ("II", 15):("IIP", "III"),
        ("II", 18):("IIP", "III"), 
        ("II", 14):("IIP", "III"),

        ("III",19):("IIIP","IV"),      
        ("III",20):("IIIP","IV"),
        ("III",15):("IIIP","IV"),
        ("III",18):("IIIP","IV"), 
        ("III",14):("IIIP","IV"),

        ("IIIP", 7):("lambda",),
        ("IIIP", 3):("lambda",),
        ("IIIP",17):("lambda",),
        ("IIIP", 2):("lambda",),
        ("IIIP",10):("lambda",),
        ("IIIP", 8):("lambda",),
        ("IIIP",11):("IIIP", "IV", "or"),
        
        ("IIP", 7):("lambda",),
        ("IIP", 3):("lambda",),
        ("IIP",17):("lambda",),
        ("IIP", 2):("lambda",),
        ("IIP",10):("desigual","III","IP"),
        ("IIP", 8):("lambda",),        

        ("IP", 7):("lambda",),
        ("IP", 3):("lambda",),
        ("IP",17):("lambda",),
        ("IP", 2):("lambda",),        
        ("IP", 8):("IP", "II", "dobleigual"),

        ("IV",10):("IVP", "V"),
        ("IV",20):("IVP", "V"),
        ("IV",15):("IVP", "V"),
        ("IV",18):("IVP", "V"),
        ("IV",14):("IVP", "V"),

        ("IVP", 7):("lambda",),
        ("IVP",13):("IVP", "V", "+"),
        ("IVP", 3):("lambda",),
        ("IVP",17):("lambda",),
        ("IVP", 2):("lambda",),
        ("IVP",10):("lambda",),
        ("IVP", 8):("lambda",),
        ("IVP",11):("lambda",),   

        ("L", 7):("lambda",),
        ("L",19):("I",),      
        ("L",20):("I",),
        ("L",17):("lambda",),
        ("L",15):("I",),
        ("L", 2):("lambda",),
        ("L",18):("I",),
        ("L",14):("I",),

        ("LL",7 ):("lambda"),
        ("LL",19):("Q","I"),
        ("LL",20):("Q","I"),
        ("LL",15):("Q","I"),
        ("LL",18):("Q","I"),
        ("LL",14):("Q","I"),


        ("N", 7):("lambda",),      
        ("N",24):("NN", "id", "T"),
        ("N",25):("NN", "id", "T"),
        ("N",26):("NN", "id", "T"),


        ("NN",7):("lambda",),
        ("NN",3):("NN", "id", "T", ","),

        ("Q",7):("lambda",),      
        ("Q",3):("Q", "I", ","),

        ("T", 18): ("lambda",),
        ("T", 24): ("bool",),
        ("T", 25): ("chars",),
        ("T", 26): ("int",),

        ("U", 6): (")","LL","("),      
        ("U", 7): ("lambda",),
        ("U", 13): ("lambda",),
        ("U", 3): ("lambda",),
        ("U", 5): ("lambda",),
        ("U", 17): ("lambda",),      
        ("U", 2): ("lambda",),
        ("U", 10): ("lambda",),
        ("U", 8): ("lambda",),
        ("U", 11): ("lambda",),

        ("V", 19): ("VP", "VI"),      
        ("V", 20): ("VP", "VI"),
        ("V", 15): ("VP", "VI"),
        ("V", 18): ("VP", "VI"),
        ("V", 14): ("VP", "VI"),
        
        ("VI", 19): ("booleano",),
        ("VI", 20): ("booleano",),
        ("VI", 15): ("cadena",),
        ("VI", 18): ("id",),
        ("VI", 14): ("numero",),

        ("VP", 7): ("lambda",),
        ("VP", 13): ("lambda",),
        ("VP", 3): ("lambda",),
        ("VP", 5): ("VP","VI"),
        ("VP", 17): ("lambda",),
        ("VP", 2): ("lambda",),
        ("VP", 10): ("lambda",),
        ("VP", 8): ("lambda",),
        ("VP", 11): ("lambda",)#or
}

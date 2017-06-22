from gestorErrores import *
from Stack import *

class ASintactico:

 
    M = {
        #M (NoTerminal, Token): (Consecuente de la regla ordenado al reves)
        ("A", 2): ("A", "cr"),
        ("A", 1): ("eof",),
        ("A",18): ("A", "cr", "B"),
        ("A",21): ("A", "cr", "B"),
        ("A",22): ("A", "cr", "B"),
        ("A",23): ("A", "cr", "B"),
        ("A",27): ("A", "cr", "C"),
        ("A",28): ("A", "cr", "B"),
        ("A",29): ("A", "cr", "B"),
        ("A",30): ("A", "cr", "B"),

        ("B",18): ("D",),
        ("B",21): ("D", ")", "I", "(", "if"),
        ("B",22): ("}", "E", "B", "E", "{", "E", ")", "L", "(", "while"),
        ("B",23): ("id", "T", "var"),
        ("B",28): ("D",),
        ("B",29): ("D",),
        ("B",30): ("D",),

        ("C",27): ("}", "E", "B", "E", "{", "E", ")", "N", "(", "id", "T", "function"),

        ("D",18): ("G", "id"),
        ("D",28): (")", "id", "(", "prompt"),
        ("D",29): (")", "I", "(", "write"),
        ("D",30): ("L", "return"),

        ("E",2 ): ("E", "cr"),
        ("E",16): ("lambda",),
        ("E",17): ("lambda",),
        ("E",18): ("lambda",),
        ("E",21): ("lambda",),
        ("E",22): ("lambda",),
        ("E",23): ("lambda",),
        ("E",28): ("lambda",),
        ("E",29): ("lambda",),
        ("E",30): ("lambda",),

        ("G",6): (")", "LL", "("),
        ("G",9): ("I","="),

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
        ("IIIP",11):("IIIP", "IV", "||"),

        ("IIP", 7):("lambda",),
        ("IIP", 3):("lambda",),
        ("IIP",17):("lambda",),
        ("IIP", 2):("lambda",),
        ("IIP",10):("IIP","III","!="),
        ("IIP", 8):("lambda",),

        ("IP", 7):("lambda",),
        ("IP", 3):("lambda",),
        ("IP",17):("lambda",),
        ("IP", 2):("lambda",),
        ("IP", 8):("IP", "II", "=="),

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
        ("VI", 18): ("U", "id"),
        ("VI", 14): ("numero",),

        ("VP", 7): ("lambda",),
        ("VP", 13): ("lambda",),
        ("VP", 3): ("lambda",),
        ("VP", 5): ("VP","VI", "-"),
        ("VP", 17): ("lambda",),
        ("VP", 2): ("lambda",),
        ("VP", 10): ("lambda",),
        ("VP", 8): ("lambda",),
        ("VP", 11): ("lambda",)
    }

    NR = {
        ("A",("A", "cr", "B")):1,
        ("A",("A", "cr", "C")):2,
        ("A",("A", "cr")): 3,
        ("A",("eof",)): 4,

        ("B", ("D",)):7,
        ("B", ("D", ")", "I", "(", "if")):5,
        ("B", ("}", "E", "B", "E", "{", "E", ")", "L", "(", "while")):8,
        ("B", ("id", "T", "var")):6,

        ("C", ("}", "E", "B", "E", "{", "E", ")", "N", "(", "id", "T", "function")):9,

        ("D", ("G", "id")):10,
        ("D", (")", "I", "(", "write")):11,
        ("D", (")", "id", "(", "prompt")):12,
        ("D", ("L", "return")):13,

        ("E", ("E", "cr")):14,
        ("E", ("lambda",)):15,

        ("G",("I","=")):16,
        ("G",(")", "LL", "(")):17,

        ("LL",("lambda")):19,
        ("LL",("Q","I")):18,

        ("L", ("lambda",)):21,
        ("L",("I",)):20,

        ("I",("IP", "II")):22,

        ("IP",("IP", "II", "==")):23,
        ("IP",("lambda",)):24,

        ("II", ("IIP", "III")):25,

        ("IIP", ("IIP","III","!=")):26,
        ("IIP", ("lambda",)):27,

        ("III",("IIIP","IV")):28,

        ("IIIP", ("IIIP", "IV", "||")):29,
        ("IIIP", ("lambda",)):30,

        ("IV",("IVP", "V")):31,

        ("IVP",("IVP", "V", "+")):32,
        ("IVP",("lambda",)):33,

        ("V", ("VP", "VI")):34,

        ("VP", ("lambda",)):36,
        ("VP",("VP","VI","-")):35,

        ("VI", ("numero",)):37,
        ("VI", ("cadena",)):38,
        ("VI", ("booleano",)):39,
        ("VI", ("U","id")):40,

        ("U", (")","LL","(")):42,
        ("U", ("lambda",)):41,

        ("N", ("NN", "id", "T")):43,
        ("N", ("lambda",)):44,

        ("NN",("lambda",)):45,
        ("NN",("NN", "id", "T", ",")):46,

        ("Q", ("lambda",)):48,
        ("Q", ("Q", "I", ",")):47,

        ("T", ("lambda",)):49,
        ("T", ("bool",)):50,
        ("T", ("int",)):51,
        ("T", ("chars",)):52
    }

    Term = [
        "true", "false", "if", "while", "var", "bool", "chars", "int",
        "function", "prompt", "write", "return", "numero", "cadena",
        "booleano", "cr", "eof", "id", ",", ";", "(", ")", "-", "==", "=",
        "!=", "||", "+=", "+", "{", "}"
        ]

    def __init__(self, p_lexic, p_symTable):
        self.AL = p_lexic
        # Semantico en un futuro
        self.TS = p_symTable
        self.pila = Stack()
        # Inicializar la pila con los valores adecuados
        self.pila.push("eof") 
        self.pila.push("A") 
        a = self.AL.get_token()
        X = "A"
        while X != "eof":
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
                # Resto de simbolos terminales
                elif (X == "numero" and a[0] == 14):
                    a = self.AL.get_token()
                elif (X == "cadena" and a[0] == 15):
                    a = self.AL.get_token()
                elif X == "id" and a[0] == 18:
                    a = self.AL.get_token()
                elif (X == "eof" and a[0] == 1):
                    return
                elif (X == "cr" and a[0] == 2):
                    a = self.AL.get_token()
                elif (X == "," and a[0] == 3):
                    a = self.AL.get_token()
                elif (X == ";" and a[0] == 4):
                    a = self.AL.get_token()
                elif (X == "-" and a[0] == 5):
                    a = self.AL.get_token()
                elif (X == "(" and a[0] == 6):
                    a = self.AL.get_token()
                elif (X == ")" and a[0] == 7):
                    a = self.AL.get_token()
                elif (X == "==" and a[0] == 8):
                    a = self.AL.get_token()
                elif (X == "=" and a[0] == 9):
                    a = self.AL.get_token()
                elif (X == "!=" and a[0] == 10):
                    a = self.AL.get_token()
                elif (X == "||" and a[0] == 11):
                    a = self.AL.get_token()
                elif (X == "+=" and a[0] == 12):
                    a = self.AL.get_token()
                elif (X == "+" and a[0] == 13):
                    a = self.AL.get_token()
                elif (X == "{" and a[0] == 16):
                    a = self.AL.get_token()
                elif (X == "}" and a[0] == 17):
                    a = self.AL.get_token()
                else:
                    error("SINTACTICO", self.AL.n_cr, "Estructura mal formada")
            else:
                print("----------------")
                print(X)
                if (X, a[0]) in self.M:
                    fd = open('fichero_parse.txt', 'a')
                    fd.write(str(self.NR[X,self.M[X,a[0]]]) + "\n")
                    fd.close()
                    for elem in self.M[X,a[0]]:
                        print(elem)
                        self.pila.push(elem)

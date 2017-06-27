from gestorErrores import *
from Stack import *

class ASintactico:

 
    M = {
        #M (NoTerminal, Token): (Consecuente de la regla ordenado al reves)
        ("P", 2): ("P", "cr"),
        ("P", 1): ("eof",),
        ("P",18): ("P", "cr", "SS"),
        ("P",21): ("P", "cr", "SC"),
        ("P",22): ("P", "cr", "SC"),
        ("P",23): ("P", "cr", "SS"),
        ("P",27): ("P", "cr", "F"),
        ("P",28): ("P", "cr", "SS"),
        ("P",29): ("P", "cr", "SS"),
        ("P",30): ("P", "cr", "SS"),

        ("SC",21): ("SS", ")", "E", "(", "if"),
        ("SC",22): ("}", "B", "{", "R", ")", "E", "(", "while"),

        ("SS",23): ("id", "T", "var"),
        ("SS",18): ("G", "id"),
        ("SS",28): (")", "id", "(", "prompt"),
        ("SS",29): (")", "E", "(", "write"),
        ("SS",30): ("E", "return"),

        ("F",27): ("}", "B", "{", "R", ")", "A1", "(", "id", "T", "function"),

        ("R", 2): ("R", "cr"),
        ("R",16): ("lambda",),

        ("G", 6): (")", "LL", "("),
        ("G", 9): ("E", "="),
        ("G",12): ("E", "+="),

        ("B",17): ("lambda",),
        ("B", 2): ("B", "cr"),
        ("B",18): ("B", "cr", "SS"),
        ("B",21): ("B", "cr", "SC"),
        ("B",22): ("B", "cr", "SC"),
        ("B",23): ("B", "cr", "SS"),
        ("B",28): ("B", "cr", "SS"),
        ("B",29): ("B", "cr", "SS"),
        ("B",30): ("B", "cr", "SS"), 

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
        ("IIIP", 2):("lambda",),
        ("IIIP",10):("lambda",),
        ("IIIP",11):("lambda",),
        ("IIIP", 8):("IIIP", "IV", "=="),

        ("IIP", 7):("lambda",),
        ("IIP", 3):("lambda",),
        ("IIP", 2):("lambda",),
        ("IIP",10):("IIP","III","!="),
        ("IIP",11):("lambda",),

        ("IP", 7):("lambda",),
        ("IP", 3):("lambda",),
        ("IP", 2):("lambda",),
        ("IP",11):("IP", "II", "||"),

        ("IV",19):("IVP", "V"),
        ("IV",20):("IVP", "V"),
        ("IV",15):("IVP", "V"),
        ("IV",18):("IVP", "V"),
        ("IV",14):("IVP", "V"),

        ("IVP", 7):("lambda",),
        ("IVP",13):("IVP", "V", "+"),
        ("IVP", 3):("lambda",),
        ("IVP", 2):("lambda",),
        ("IVP",10):("lambda",),
        ("IVP", 8):("lambda",),
        ("IVP",11):("lambda",),

        ("E", 7):("lambda",),
        ("E",19):("I",),
        ("E",20):("I",),
        ("E",15):("I",),
        ("E", 2):("lambda",),
        ("E",18):("I",),
        ("E",14):("I",),

        ("LL",7 ):("lambda"),
        ("LL",19):("Q","I"),
        ("LL",20):("Q","I"),
        ("LL",15):("Q","I"),
        ("LL",18):("Q","I"),
        ("LL",14):("Q","I"),

        ("A1", 7):("lambda",),
        ("A1",24):("A2", "id", "T"),
        ("A1",25):("A2", "id", "T"),
        ("A1",26):("A2", "id", "T"),

        ("A2",7):("lambda",),
        ("A2",3):("A2", "id", "T", ","),

        ("Q",7):("lambda",),
        ("Q",3):("Q", "I", ","),
        
        ("T", 24): ("bool",),
        ("T", 25): ("chars",),
        ("T", 26): ("int",),

        ("X", 18): ("lambda",),
        ("X", 24): ("T",),
        ("X", 25): ("T",),
        ("X", 26): ("T",),

        ("U", 6): (")","LL","("),
        ("U", 7): ("lambda",),
        ("U", 13): ("lambda",),
        ("U", 3): ("lambda",),
        ("U", 5): ("lambda",),
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
        ("VP", 2): ("lambda",),
        ("VP", 10): ("lambda",),
        ("VP", 8): ("lambda",),
        ("VP", 11): ("lambda",)
    }

    NR = {
        ("P",("P", "cr", "SS")):1,
        ("P",("P", "cr", "SC")):2,
        ("P",("P", "cr", "F")):3,
        ("P",("P", "cr")): 4,
        ("P",("eof",)): 5,

        ("SC", ("SS", ")", "E", "(", "if")):6,
        ("SC", ("}", "B", "{", "R", ")", "E", "(", "while")):7,

        ("SS", ("id", "T", "var")):8,
        ("SS", ("G", "id")):9,
        ("SS", (")", "E", "(", "write")):10,
        ("SS", (")", "id", "(", "prompt")):11,
        ("SS", ("E", "return")):12,

        ("F", ("}", "B", "{", "R", ")", "A1", "(", "id", "T", "function")):13,

        ("R", ("R", "cr")):14,
        ("R", ("lambda",)):15,

        ("G",("E", "+=")):16,
        ("G",("E", "=")):17,
        ("G",(")", "LL", "(")):18,

        ("B",("B", "cr", "SS")):19,
        ("B",("B", "cr", "SC")):20,
        ("B",("B", "cr",)):21,
        ("B",("lambda",)):22,

        ("LL",("lambda",)):24,
        ("LL",("Q","I")):23,

        ("E", ("lambda",)):26,
        ("E",("I",)):25,

        ("I",("IP", "II")):27,

        ("IP",("IP", "II", "||")):28,
        ("IP",("lambda",)):29,

        ("II", ("IIP", "III")):30,

        ("IIP", ("IIP","III","!=")):31,
        ("IIP", ("lambda",)):32,

        ("III",("IIIP","IV")):33,

        ("IIIP", ("IIIP", "IV", "==")):34,
        ("IIIP", ("lambda",)):35,

        ("IV",("IVP", "V")):36,

        ("IVP",("IVP", "V", "+")):37,
        ("IVP",("lambda",)):38,

        ("V", ("VP", "VI")):39,

        ("VP", ("lambda",)):41,
        ("VP",("VP","VI","-")):40,

        ("VI", ("numero",)):42,
        ("VI", ("cadena",)):43,
        ("VI", ("booleano",)):44,
        ("VI", ("U","id")):45,

        ("U", (")","LL","(")):47,
        ("U", ("lambda",)):46,

        ("A1", ("A2", "id", "T")):48,
        ("A1", ("lambda",)):49,

        ("A2",("lambda",)):50,
        ("A2",("A2", "id", "T", ",")):51,

        ("Q", ("lambda",)):53,
        ("Q", ("Q", "I", ",")):52,
        
        ("T", ("bool",)):54,
        ("T", ("int",)):55,
        ("T", ("chars",)):56,

        ("X", ("T",)):57,
        ("X", ("lambda",)):58
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
        self.pila.push("P") 
        a = self.AL.get_token()
        X = "P"
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
                elif (X == "booleano"):
                    if (a[0] == 19 or a[0] == 20):
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

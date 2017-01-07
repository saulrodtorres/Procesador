import sys
from analizadorLexico import Lexico
from analizadorSintactico import Sintactico
from SymTable import SymTable

def main():
    inputfile = ''
    if (len(sys.argv) == 1):
        print "Usage: procesador.py <inputfile>"
        sys.exit(2)
    tokensFile = open('fichero_tokens.txt', 'w')
    tokensFile.close()
    tableFile = open('fichero_tabla.txt', 'w')
    tableFile.close()
    parseFile = open('fichero_parse.txt', 'w')
    parseFile.write("Descendente\n")
    parseFile.close()
    inputfile = sys.argv[1]
    TS = SymTable()
    TS.newTable()
    AL = Lexico(inputfile, TS)
    AS = Sintactico(AL, TS)
    TS.writeTable('./fichero_tabla.txt')
    sys.exit(0)


if __name__ == '__main__':
    main()

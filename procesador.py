import sys
from analizadorLexico import Lexico
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
    inputfile = sys.argv[1]
    TS = SymTable()
    TS.newTable()
    AL = Lexico(inputfile, TS)
    while True:
        token = AL.get_token()
        if token[0] == 1:
            print(token)
            break
        print(token)
    TS.writeTable('./fichero_tabla.txt')
    sys.exit(0)


if __name__ == '__main__':
    main()

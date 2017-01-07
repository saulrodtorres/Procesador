"""
modulo gestorErrores
	
	Escribe en el fichero_errores.txt con el siguiente formato:
	ERROR (analizador Linea: mensaje)
		* Analizador: LEXICO, SEMANTICO, SINTACTICO
		* Linea: linea donde se produce el error
		* Mensaje: mensaje adicional de descripcion del error
	Un exit(2) detiene la ejecucion nada mas cerrar el fichero
	
"""
def error(machine, linea, mensaje):
    print("# ERROR (%s Linea %d: %s)" %(machine,linea,mensaje))
    file_descriptor = open("fichero_errores.txt", 'w')
    file_descriptor.write("# ERROR (%s Linea %d: %s)\n" %(machine,linea,mensaje))
    file_descriptor.close()
    exit(2)

#bucle de varias pruebas
#para cada prueba, copia el archivo que haya en /ficherosEntrada
ECHO OFF
cd ..\


for /r %%i in (*) [
	do echo COPIANDO ARCHIVO %%i
	copy ..\FicherosEntrada\%%i ..\codigo.txt
	ECHO .............preparacion de la prueba terminada
	###########################################################
	pause
	python procesador.py codigo.txt	
	pause
	###########################################################
	ECHO .                                  .
	ECHO .                                  .
	ECHO .        PAINTING RESULTS          .
	ECHO .                                  .
	ECHO .                                  .
	#crea carpeta especifica con fecha y hora
	set mydate=%date:~6,4%%date:~3,2%%date:~0,2%
	echo %mydate%
	
	mkdir .\Salidas\SALIDAS.%mydate%
	#la idea seria leer FicherosEntrada/tabla_pruebas.org y escribirla en un 
	ECHO .............No results to paint
	pause
]
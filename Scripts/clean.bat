#borra archivos de compilación para entregar en github
ECHO OFF
ECHO .............cambiando directorio
cd ../
ECHO .............borrando los archivos .PYC
del *.pyc
ECHO .............fin de borrado
pause

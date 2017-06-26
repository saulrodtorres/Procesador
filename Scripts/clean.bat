REM borra archivos de compilación para entregar en github

ECHO OFF

cd ../
ECHO ----------------------------------------------------------
ECHO              borrando los archivos .PYC
ECHO ----------------------------------------------------------
del *.pyc
ECHO ----------------------------------------------------------
ECHO              fin llamada a clean.bat
ECHO ----------------------------------------------------------
pause
cd ./Scripts

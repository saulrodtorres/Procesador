echo off
set hour=%time:~0,2%
if "%hour:~0,1%" == " " set hour=0%hour:~1,1%
rem echo hour=%hour%
set min=%time:~3,2%
if "%min:~0,1%" == " " set min=0%min:~1,1%
rem echo min=%min%
set secs=%time:~6,2%
if "%secs:~0,1%" == " " set secs=0%secs:~1,1%
rem echo secs=%secs%

set year=%date:~-4%
echo year=%year%
set month=%date:~3,2%
if "%month:~0,1%" == " " set month=0%month:~1,1%
rem echo month=%month%
set day=%date:~0,2%
if "%day:~0,1%" == " " set day=0%day:~1,1%
rem echo day=%day%

set datetimef=%year%%month%%day%_%hour%%min%%secs%

echo datetimef=%datetimef%

ECHO ###########################################################################
ECHO ###########################STARTING MAIN###################################
ECHO ###########################################################################
ECHO ###########################DATE AND TIME###################################
ECHO ###########################################################################
ECHO                            resultados en /%datetimef%
mkdir ..\Salidas\%datetimef%
ECHO                            CODIGO 01
CALL execute.bat codigo_01.js %datetimef%
ECHO                            CODIGO 02
CALL execute.bat codigo_02.js %datetimef%
ECHO                            CODIGO 03
CALL execute.bat codigo_03.js %datetimef%
ECHO                            CODIGO 04
execute.bat codigo_04.js %datetimef%
ECHO                            CODIGO 05
execute.bat codigo_05.js %datetimef%
ECHO                            CODIGO 06
execute.bat codigo_06.js %datetimef%
ECHO                            CODIGO 07
execute.bat codigo_07.js %datetimef%
ECHO ###########################################################################
ECHO ###########################END OF MAIN#####################################
ECHO ###########################################################################
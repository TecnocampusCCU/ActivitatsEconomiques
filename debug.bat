@echo off
set MYDIR=%cd%
for %%f in (%MYDIR%) do set directory=%%~nxf

@echo on
cmd /c "pyrcc5 -o resources.py resources.qrc"
cmd /c "rmdir /S /Q "%APPDATA%"\QGIS\QGIS3\profiles\default\python\plugins\%directory%"
cmd /c "xcopy ..\%directory% "%APPDATA%"\QGIS\QGIS3\profiles\default\python\plugins\%directory% /E /Q /I /Y"
exit
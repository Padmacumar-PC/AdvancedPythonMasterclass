:: turn MAYA prompt
@echo off

:: set maya version
set "MAYA_VERSION=2022"

:: --- PYTHON custom script path ---
set "PYTHONPATH=E:/WeiterBildung/AlexanderRichterTD/PYadvanced/01_tools/assignment/script"

:: Autodesk root directory
set "MAYA_DIR=C:/Program Files/Autodesk/Maya%MAYA_VERSION%"

:: add Autodesk root dir to system paths
set "PATH=%MAYA_DIR%/bin;%PATH%"

:: --- CALL MAYA ---
start "" "%MAYA_DIR%/bin/maya.exe"

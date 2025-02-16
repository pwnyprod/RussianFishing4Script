@echo off
setlocal

echo Starting
cd src

set /p tocraft=Enter Limit of Items to craft:

python craft.py
pause
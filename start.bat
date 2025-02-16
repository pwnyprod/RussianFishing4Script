@echo off
setlocal

set "ALL_ARGS="

echo Starting
cd src

choice /m "Shutdown computer after terminated without user interruption" /c yn
if errorlevel 1 set "ALL_ARGS=%ALL_ARGS% -s"

choice /m "Recast the spod rod automatically" /c yn
if errorlevel 1 set "ALL_ARGS=%ALL_ARGS% -o"

set /p fishnet=Enter current Net Value:

choice /m "Which profile?" /c bsf
if errorlevel 1 (
    python app.py -n %fishnet% %ALL_ARGS% -g -l -f -x -R -H
) else if errorlevel 2 (
    choice /m "Change current lure with a random one automatically" /c yn
    if errorlevel 1 set "ALL_ARGS=%ALL_ARGS% -L"
    python app.py -n %fishnet% %ALL_ARGS% -g -l -f -x -H
) else if errorlevel 3 (
    python app.py -n %fishnet% %ALL_ARGS% -l -x -H
)

endlocal
pause
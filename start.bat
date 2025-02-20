@echo off
setlocal

echo Starting
cd src

# -o Recast the spod rod automatically
# -s Shutdown computer after terminated without user interruption

set /p fishnet=Enter current Net Value:

choice /m "Which profile?" /c bsf
if %errorlevel%==1 (
    python app.py -n %fishnet% -g -l -f -x -R -H
) else if %errorlevel%==2 (
    choice /m "Change current lure with a random one automatically" /c yn
    if %errorlevel%==1 (
        python app.py -n %fishnet% -g -l -f -x -H -L
    ) else if %errorlevel%==2 (
        python app.py -n %fishnet% -g -l -f -x -H
    )
) else if %errorlevel%==3 (
    python app.py -n %fishnet% -l -x -H
)

endlocal
pause

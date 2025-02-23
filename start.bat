@echo off
setlocal

echo Starting
cd src

:: Read arguments
set RECAST_SPOD_ROD=%1
set SHUTDOWN_AFTER_TERMINATION=%2

:: Check environment variables
if "%RECAST_SPOD_ROD%"=="1" (
    set recast_option=-o
) else (
    set recast_option=
)

if "%SHUTDOWN_AFTER_TERMINATION%"=="1" (
    set shutdown_option=-s
) else (
    set shutdown_option=
)

set /p fishnet=Enter current Net Value:

choice /m "Which arg profile?" /c bsf
set profile=%errorlevel%

if %profile%==1 goto profile1
if %profile%==2 goto profile2
if %profile%==3 goto profile3
goto end

:profile1
python app.py -n %fishnet% -g -l -f -x -R -H %recast_option% %shutdown_option%
goto end

:profile2
choice /m "Change current lure with a random one automatically" /c yn
set lure=%errorlevel%
if %lure%==1 goto lure1
if %lure%==2 goto lure2
goto end

:lure1
python app.py -n %fishnet% -g -l -f -x -H %recast_option% %shutdown_option% -L
goto end

:lure2
python app.py -n %fishnet% -g -l -f -x -H %recast_option% %shutdown_option%
goto end

:profile3
python app.py -n %fishnet% -l -x -H %recast_option% %shutdown_option%
goto end

:end
endlocal
pause
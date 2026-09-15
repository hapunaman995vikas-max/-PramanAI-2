@echo off
title Pramaan AI - Official Portal Launcher
color 0A
echo ========================================================
echo         Launching Pramaan AI Portal...
echo ========================================================
echo.

cd /d "%~dp0"

if not exist "node_modules" (
    echo [INFO] Installing required dependencies...
    call npm install
)

echo.
echo [SUCCESS] Starting dev server at http://localhost:3000/
echo [INFO] Opening default browser...
echo.

start http://localhost:3000/
call npm run dev
pause

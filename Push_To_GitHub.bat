@echo off
title Push Pramaan AI to GitHub
cd /d "%~dp0"
echo ====================================================
echo   PRAMAAN AI - GITHUB AUTOMATED PUSH TOOL
echo ====================================================
echo.

set "GIT_PATH=%TEMP%\MinGit\cmd\git.exe"
if not exist "%GIT_PATH%" (
    where git >nul 2>nul
    if %errorlevel% equ 0 (
        set "GIT_PATH=git"
    ) else (
        echo [ERROR] Git not found.
        pause
        exit /b 1
    )
)

echo [1/3] Adding all files (including src/, public/, netlify.toml)...
"%GIT_PATH%" add .

echo [2/3] Committing changes...
"%GIT_PATH%" commit -m "Upload complete Pramaan AI source code (src, public, netlify config)" 2>nul

echo [3/3] Pushing to https://github.com/abhisheksingh912-dot/PRAMAAN_AI...
echo.
echo ************************************************************
echo If a GitHub login window appears, please click "Sign in with your browser".
echo Or enter your GitHub Personal Access Token if prompted.
echo ************************************************************
echo.

"%GIT_PATH%" push -u origin main --force

echo.
echo ====================================================
echo Check your repository:
echo https://github.com/abhisheksingh912-dot/PRAMAAN_AI
echo ====================================================
pause

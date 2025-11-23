@echo off
REM Convert EPUB to MOBI for Kindle using Calibre
REM Requires Calibre to be installed: https://calibre-ebook.com

echo ========================================
echo Histologic Stories - Kindle Converter
echo ========================================
echo.

cd /d "%~dp0.."

REM Check if ebook-convert exists
where ebook-convert >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Calibre not found!
    echo.
    echo Please install Calibre from: https://calibre-ebook.com
    echo After installation, restart this script.
    echo.
    pause
    exit /b 1
)

echo Converting EPUB to MOBI for Kindle...
echo.

ebook-convert histologic-stories.epub histologic-stories.mobi ^
    --output-profile kindle ^
    --mobi-file-type both ^
    --no-inline-toc ^
    --prefer-metadata-cover

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Conversion successful!
    echo ========================================
    echo.
    echo Created: histologic-stories.mobi
    echo.
    echo Next steps:
    echo   1. Connect your Kindle via USB
    echo   2. Copy histologic-stories.mobi to the "documents" folder
    echo   3. Eject Kindle safely
    echo   4. The book will appear in your library!
    echo.
    echo Or email it to your Kindle:
    echo   1. Find your Kindle email: amazon.com/mycd
    echo   2. Email histologic-stories.mobi to your@kindle.com
    echo   3. Book appears on your Kindle wirelessly!
    echo.
) else (
    echo.
    echo ERROR: Conversion failed!
    echo Please check the error message above.
    echo.
)

pause




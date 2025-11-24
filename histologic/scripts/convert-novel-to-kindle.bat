@echo off
echo ========================================
echo Converting "The Correction" to Kindle Format
echo ========================================
echo.

set EPUB_FILE=novels\04-the-correction\the-correction.epub
set MOBI_FILE=novels\04-the-correction\the-correction.mobi

if not exist "%EPUB_FILE%" (
    echo ERROR: EPUB file not found!
    echo Please run: python scripts/create-novel-ebook.py first
    pause
    exit /b 1
)

echo Converting EPUB to MOBI using Calibre...
echo.

ebook-convert "%EPUB_FILE%" "%MOBI_FILE%" --output-profile kindle

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo Conversion successful!
    echo.
    echo MOBI file: %MOBI_FILE%
    echo ========================================
) else (
    echo.
    echo ========================================
    echo ERROR: Conversion failed!
    echo.
    echo Make sure Calibre is installed and ebook-convert is in PATH
    echo Download from: https://calibre-ebook.com/
    echo ========================================
)

echo.
pause





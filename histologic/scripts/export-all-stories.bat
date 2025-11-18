@echo off
REM Export all Histologic stories to HTML

echo ========================================
echo Histologic Story HTML Exporter
echo ========================================
echo.

cd /d "%~dp0.."

echo Exporting "The Believer's Fall"...
python scripts\export-story-html.py novels\the-believers-fall
echo.

echo Exporting "The Stolen Fact"...
python scripts\export-story-html.py novels\the-stolen-fact
echo.

echo Exporting "The Divided Truth"...
python scripts\export-story-html.py novels\the-divided-truth
echo.

echo ========================================
echo All stories exported successfully!
echo ========================================
echo.
echo HTML files created in each story folder:
echo   - novels\the-believers-fall\the-believers-fall.html
echo   - novels\the-stolen-fact\the-stolen-fact.html
echo   - novels\the-divided-truth\the-divided-truth.html
echo.

pause


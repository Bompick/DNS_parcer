@echo off
cd /d "%~dp0"

echo ==========================================
echo Starting Sequential Parsing Process
echo ==========================================

echo.
echo [1/4] Launching Wildberries Parser...
python.exe .\wb_parser.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Wildberries parser failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/4] Launching Ozon Parser...
python.exe .\ozon_parser.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Ozon parser failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [3/4] Launching DNS Parser...
python.exe .\scrape_dns.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: DNS parser failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [4/4] All parsers finished successfully. Starting Merge Process...
python.exe .\merge_prices.py
if %ERRORLEVEL% NEQ 0 (
    echo Error: Merge process failed!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ==========================================
echo All tasks completed successfully!
echo ==========================================
pause
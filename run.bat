@echo off
REM LuckyWeaver - Local Run Script for Windows

echo Starting LuckyWeaver...
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -q -r requirements.txt

REM Run app
echo Starting application on http://localhost:5001
echo.
echo Press Ctrl+C to stop
echo.

python app.py

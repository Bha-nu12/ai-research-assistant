@echo off
REM Multi-Document RAG Research Assistant - Quick Start Script

echo.
echo ========================================
echo Multi-Document RAG Research Assistant
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created
) else (
    echo Virtual environment already exists
)

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Installing dependencies...
pip install -r requirements.txt

echo.
echo [4/5] Checking .env file...
if not exist .env (
    echo Creating .env from template...
    copy .env.example .env
    echo.
    echo WARNING: Please edit .env file with your API keys:
    echo   - OPENAI_API_KEY
    echo   - PINECONE_API_KEY
    echo   - PINECONE_ENVIRONMENT
    echo   - COHERE_API_KEY
    echo.
    pause
)

echo.
echo [5/5] Launching Streamlit application...
echo.
echo Application will open at: http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

streamlit run app.py

pause

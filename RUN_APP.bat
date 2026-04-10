@echo off
echo ========================================
echo  Multi-Document RAG Research Assistant
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Streamlit app...
streamlit run app.py
pause

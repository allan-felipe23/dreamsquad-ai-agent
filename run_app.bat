@echo off
:: Garante que o script rode a partir da pasta onde o arquivo está salvo
cd /d "%~dp0"

echo ==========================================
echo 🚀 Iniciando DreamSquad AI Agent (Modo Seguro)
echo ==========================================

:: 1. Verificacao de Seguranca
if not exist "venv" (
    echo [ERRO] A pasta 'venv' nao foi encontrada!
    echo Voce precisa criar o ambiente virtual primeiro.
    echo Rode: python -m venv venv
    pause
    exit
)

echo.
echo 1. Iniciando o Backend (API)...
:: Abre nova janela, ativa a venv e roda o uvicorn
start "Backend API" cmd /k "call venv\Scripts\activate.bat && uvicorn main:app --reload"

echo.
echo Aguardando 5 segundos para a API carregar...
timeout /t 5

echo.
echo 2. Iniciando o Frontend...
:: Ativa a venv nesta janela e roda o streamlit
call venv\Scripts\activate.bat

if %errorlevel% neq 0 (
    echo [ERRO] Falha ao ativar o ambiente virtual.
    pause
    exit
)

streamlit run frontend.py

pause

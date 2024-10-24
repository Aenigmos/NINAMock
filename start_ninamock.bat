@echo off
:: Verifica se Docker è in esecuzione
docker version >nul 2>&1
if ERRORLEVEL 1 (
    echo Docker non e' in esecuzione. Avvia Docker Desktop prima di eseguire questo script.
    pause
    exit /b
)

:: Avvia NINAMock con Docker Compose
echo Avvio di NINAMock...
docker-compose up -d

if ERRORLEVEL 0 (
    echo NINAMock avviato correttamente.
) else (
    echo Errore nell'avvio di NINAMock.
)

pause
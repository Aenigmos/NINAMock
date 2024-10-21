@echo off
:: Ferma NINAMock con Docker Compose
echo Fermare NINAMock...
docker-compose down

if ERRORLEVEL 0 (
    echo NINAMock fermato correttamente.
) else (
    echo Errore nel fermare NINAMock.
)

pause
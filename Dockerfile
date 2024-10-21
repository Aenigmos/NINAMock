# Usa un'immagine Python slim
FROM python:3.8-slim

WORKDIR /app

# Installazione della versione 1.5.1 di paho-mqtt
RUN pip install paho-mqtt

# Copia dello script NINAMock nel container
COPY nina_mock.py .

# Comando per eseguire lo script NINAMock
CMD ["python", "nina_mock.py"]
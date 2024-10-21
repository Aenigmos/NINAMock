
# NINAMock Project

## Descrizione
Questo progetto simula l'invio di messaggi MQTT da N.I.N.A. utilizzando Docker. L'indirizzo del broker Mosquitto e il topic sono configurabili tramite un file `config.json`.

## Struttura del progetto

```
ninamock/
│
├── config.json           # File di configurazione per il broker e il topic
├── docker-compose.yml    # File per configurare Docker Compose
├── Dockerfile            # Dockerfile per NINAMock
├── nina_mock.py          # Script Python che simula N.I.N.A.
├── start_ninamock.bat    # Script batch per avviare NINAMock
├── stop_ninamock.bat     # Script batch per fermare NINAMock
└── README.md             # Documentazione del progetto
```

## Prerequisiti

- **Docker** e **Docker Compose** devono essere installati sul tuo sistema.
- Un broker Mosquitto esterno deve essere in esecuzione per ricevere i messaggi.

## Configurazione

1. Modifica il file `config.json` per impostare l'indirizzo del broker Mosquitto e il topic MQTT:

```json
{
  "broker_address": "IP_DEL_BROKER_MOSQUITTO",
  "topic": "nina/status"
}
```

## Istruzioni per l'uso

### 1. Avviare NINAMock

Per avviare NINAMock, fai doppio clic sul file `start_ninamock.bat`. Lo script:

1. Verifica se Docker è in esecuzione.
2. Avvia il container NINAMock in background tramite Docker Compose.

### 2. Fermare NINAMock

Per fermare NINAMock, fai doppio clic sul file `stop_ninamock.bat`. Lo script fermerà il container NINAMock.

### 3. Test

Utilizza un client MQTT per verificare che i messaggi di NINAMock vengano ricevuti dal broker Mosquitto. Ad esempio, puoi utilizzare `mosquitto_sub` per iscriverti al topic:

```bash
mosquitto_sub -h IP_DEL_BROKER_MOSQUITTO -t "nina/status"
```

## Avviare e fermare NINAMock

- **Per avviare NINAMock**: Fai doppio clic su **`start_ninamock.bat`**.
- **Per fermare NINAMock**: Fai doppio clic su **`stop_ninamock.bat`**.

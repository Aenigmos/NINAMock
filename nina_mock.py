import paho.mqtt.client as mqtt
import time
import json
from enum import Enum

# Definisci l'enumerazione per i tipi di messaggio
class MessageType(Enum):
    CALIBRATION_STATUS = "calibration_status"
    OBSERVATION_STARTED = "observation_started"
    OBSERVATION_ENDED = "observation_ended"
    ERROR = "error"

# Leggi il file di configurazione
with open("config.json", "r") as config_file:
    config = json.load(config_file)

broker_address = config["broker_address"]
topic = config["topic"]

# Configurazione del client MQTT
client = mqtt.Client(client_id="NINA_Mock")
client.connect(broker_address, 1883, 60)

# Funzione per inviare messaggi di N.I.N.A.
def send_nina_message(msg_type: MessageType, message: str):
    print(f"Invio del messaggio di tipo {msg_type.value}...")
    payload = {
        "type": msg_type.value,
        "message": message
    }
    client.publish(topic, json.dumps(payload))
    print(f"Messaggio inviato: {payload}")

# Simulazione di invio messaggi
while True:
    # Simula il messaggio di stato di calibrazione
    send_nina_message(MessageType.CALIBRATION_STATUS, "Calibration successful.")
    time.sleep(5)  # Simula un intervallo tra i messaggi

    # Simula l'inizio di un'osservazione
    send_nina_message(MessageType.OBSERVATION_STARTED, "Observation started.")
    time.sleep(5)

    # Simula la fine di un'osservazione
    send_nina_message(MessageType.OBSERVATION_ENDED, "Observation ended.")
    time.sleep(5)

    # Simula un errore
    send_nina_message(MessageType.ERROR, "An error occurred in the observation process.")
    time.sleep(5)

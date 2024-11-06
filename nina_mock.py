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
client = mqtt.Client(client_id="NINA_Mock", callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.connect(broker_address, 1883, 60)

# Funzione per inviare messaggi di N.I.N.A.
def send_nina_message(message: str, msg_type: MessageType = None):
    print(f"Invio del messaggio...")
    payload = {
        "message": message
    }
    if msg_type is not None:
        payload["type"] = msg_type.value
    client.publish(topic, json.dumps(payload))
    print(f"Messaggio inviato: {payload}")

# Simulazione di invio messaggi
while True:
    # Messaggio con tipo di stato di calibrazione
    send_nina_message("Calibration successful.", MessageType.CALIBRATION_STATUS)
    time.sleep(5)

    # Messaggio di inizio osservazione
    send_nina_message("Observation started.", MessageType.OBSERVATION_STARTED)
    time.sleep(5)

    # Messaggio di fine osservazione
    send_nina_message("Observation ended.", MessageType.OBSERVATION_ENDED)
    time.sleep(5)

    # Messaggio di errore
    send_nina_message("An error occurred in the observation process.", MessageType.ERROR)
    time.sleep(5)

    # Messaggio senza tipo
    send_nina_message("This is a message without a specific type.")
    time.sleep(5)
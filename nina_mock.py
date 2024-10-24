import paho.mqtt.client as mqtt
import time
import json

# Leggi il file di configurazione
with open("config.json", "r") as config_file:
    config = json.load(config_file)

broker_address = config["broker_address"]
topic = config["topic"]

# Configurazione del client MQTT con l'API Callback v1
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="NINA_Mock")
client.connect(broker_address, 1883, 60)

# Simulazione di invio messaggi
def send_status():
    print("Invio del messaggio di stato di calibrazione...")
    message = "Calibrazione riuscita!"
    client.publish(topic, message)
    print(f"Messaggio inviato: {message}")

while True:
    send_status()
    time.sleep(5)  # Simula un intervallo tra i messaggi
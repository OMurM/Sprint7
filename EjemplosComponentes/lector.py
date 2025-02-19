import time
from mqtt_client import MQTTClient

THINGSBOARD_HOST = "192.168.192.116"  # Dirección del servidor ThingsBoard
SENSOR_TOKEN = "DHT11_DEMO_TOKEN"  # Token compartido para el sensor y lector


class TemperatureReader:
    def __init__(self, mqtt_client):
        """
        Inicializa el lector de temperaturas.
        :param mqtt_client: Instancia del cliente MQTT.
        """
        self.mqtt_client = mqtt_client

    def message_callback(self, client, userdata, msg):
        """
        Callback que se ejecuta cuando se recibe un mensaje del tópico.
        :param client: Instancia del cliente MQTT.
        :param userdata: Datos adicionales del usuario.
        :param msg: Mensaje recibido con el tópico y payload.
        """
        print(f"Mensaje recibido en '{msg.topic}': {msg.payload.decode()}")

    def read_telemetry(self):
        """
        Se suscribe a los atributos del sensor para leer las temperaturas.
        """
        print("Esperando datos del sensor...")
        # El lector se suscribe a telemetría
        topic = "v1/devices/me/telemetry"
        self.mqtt_client.subscribe(topic, self.message_callback)

        try:
            while True:
                time.sleep(1)  # Mantén el programa activo y esperando mensajes
        except KeyboardInterrupt:
            print("Lectura de telemetría detenida.")


if __name__ == "__main__":
    # Inicializa el cliente MQTT y lo conecta al servidor
    mqtt_client = MQTTClient(THINGSBOARD_HOST, SENSOR_TOKEN)
    mqtt_client.connect()

    # Inicializa y ejecuta el lector de temperatura
    reader = TemperatureReader(mqtt_client)
    reader.read_telemetry()

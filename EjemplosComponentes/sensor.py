import time
import random
from mqtt_client import MQTTClient

THINGSBOARD_HOST = "192.168.192.116"
SENSOR_TOKEN = "DHT11_DEMO_TOKEN"

class TemperatureSensor:
    def __init__(self, mqtt_client, high_temp_duration=5, low_temp_duration=15):
        """
        Inicializa el sensor de temperatura.
        :param mqtt_client: Instancia del cliente MQTT.
        :param high_temp_duration: Duración en segundos de temperaturas altas.
        :param low_temp_duration: Duración en segundos de temperaturas bajas.
        """
        self.mqtt_client = mqtt_client
        self.high_temp_duration = high_temp_duration
        self.low_temp_duration = low_temp_duration

    def generate_temperature(self, high):
        """Genera temperaturas altas o bajas."""
        if high:
            return round(random.uniform(30.1, 35.0), 2)
        return round(random.uniform(20.0, 29.9), 2)

    def simulate(self):
        """Simula el envío de telemetría alternando temperaturas altas y bajas."""
        try:
            while True:
                for _ in range(self.high_temp_duration):
                    temp = self.generate_temperature(high=True)
                    # Cambia el tópico a telemetría
                    self.mqtt_client.publish("v1/devices/me/telemetry", {"temperature": temp})
                    print(f"Temperatura enviada: {temp}°C (Alta)")
                    time.sleep(1)

                for _ in range(self.low_temp_duration):
                    temp = self.generate_temperature(high=False)
                    self.mqtt_client.publish("v1/devices/me/attributes", {"temperature": temp})
                    print(f"Temperatura enviada: {temp}°C (Baja)")
                    time.sleep(1)
        except KeyboardInterrupt:
            print("Simulación de sensor detenida.")


if __name__ == "__main__":
    mqtt_client = MQTTClient(THINGSBOARD_HOST, SENSOR_TOKEN)
    mqtt_client.connect()

    sensor = TemperatureSensor(mqtt_client)
    sensor.simulate()

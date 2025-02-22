import asyncio
import json
import logging
from websocket_server import main as websocket_main
from actuator_subscription import actuator_subscription
from components.sensor import TemperatureSensor, HumiditySensor, SoilMoistureSensor
from influxdb_client import InfluxDBClient, Point, WriteOptions

logging.basicConfig(level=logging.CRITICAL)

class InfluxDBConnection:
    def __init__(self, url, token, org, bucket):
        self.url = url
        self.token = token
        self.org = org
        self.bucket = bucket

    def get_client(self):
        logging.info(f"Connecting to InfluxDB at {self.url} with token {self.token}")
        return InfluxDBClient(url=self.url, token=self.token, org=self.org)

    def get_write_api(self, client):
        return client.write_api(write_options=WriteOptions(batch_size=1))

# Initialize sensors
temperature_sensor = TemperatureSensor()
humidity_sensor = HumiditySensor()
soil_moisture_sensor = SoilMoistureSensor()

# Initialize InfluxDB connection
influxdb_connection = InfluxDBConnection(
    url="http://localhost:8086",
    token="W6ibgZq6dNxOyTn7FrIqKaQfXDQacwPOKU8KjOcgugkw2ybi40PITM49fFKjWQAUKmMfKoOmhdjGxcPHjDZU5A==",
    org="Sprint7",
    bucket="iot"
)

client = influxdb_connection.get_client()
write_api = influxdb_connection.get_write_api(client)

async def read_sensor_data():
    """Read data from sensors, print it to the terminal, and save it to InfluxDB."""
    while True:
        temperature = temperature_sensor.read_data()
        humidity = humidity_sensor.read_data()
        soil_moisture = soil_moisture_sensor.read_data()

        sensor_data = {
            "temperature": temperature,
            "humidity": humidity,
            "soil_moisture": soil_moisture
        }

        logging.info(f"Sensor Data: {json.dumps(sensor_data, indent=2)}")

        # Save data to InfluxDB
        point = Point("sensor_data") \
            .field("temperature", float(temperature)) \
            .field("humidity", humidity) \
            .field("soil_moisture", soil_moisture)
        try:
            logging.info(f"Writing data to InfluxDB: {point.to_line_protocol()}")
            write_api.write(bucket=influxdb_connection.bucket, org=influxdb_connection.org, record=point)
            logging.info("Data written to InfluxDB successfully.")
        except Exception as e:
            logging.error(f"Failed to write data to InfluxDB: {e}")

        await asyncio.sleep(5)

async def run_all():
    asyncio.create_task(actuator_subscription())
    asyncio.create_task(read_sensor_data())
    await asyncio.Future()  # Keep the process alive

if __name__ == "__main__":
    asyncio.run(run_all())
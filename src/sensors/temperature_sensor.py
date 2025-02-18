import random
import time
import config  # Import config
from influxdb_client import Point
from influxdb_client import InfluxDBClient, WritePrecision

# InfluxDB Client
client = InfluxDBClient(url=config.INFLUX_URL, token=config.TOKEN, org=config.ORG)
write_api = client.write_api(write_options=WritePrecision.NS)

def generate_temperature():
    while True:
        temp = random.uniform(18, 30)
        print(f"Temperature: {temp:.2f}°C")
        point = Point("temperature").field("value", temp)
        write_api.write(bucket=config.BUCKET, org=config.ORG, record=point)
        time.sleep(5)

if __name__ == "__main__":
    generate_temperature()

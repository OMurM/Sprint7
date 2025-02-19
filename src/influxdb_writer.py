# src/influxdb_writer.py

from influxdb_client import InfluxDBClient, Point, WriteOptions
from config.config import INFLUXDB_CONFIG

class InfluxDBWriter:
    def __init__(self):
        self.client = InfluxDBClient(
            url=INFLUXDB_CONFIG['url'],
            token=INFLUXDB_CONFIG['token'],
            org=INFLUXDB_CONFIG['org']
        )
        self.write_api = self.client.write_api(write_options=WriteOptions(batch_size=1))

    def write_data(self, temperature, humidity, soil_moisture):
        point = Point("sensor_data") \
            .field("temperature", temperature) \
            .field("humidity", humidity) \
            .field("soil_moisture", soil_moisture)

        self.write_api.write(bucket=INFLUXDB_CONFIG['bucket'], org=INFLUXDB_CONFIG['org'], record=point)

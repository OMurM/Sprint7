from influxdb_client import InfluxDBClient, Point, WritePrecision
import config  # Import configuration

# InfluxDB Client
client = InfluxDBClient(url=config.INFLUX_URL, token=config.TOKEN, org=config.ORG)
write_api = client.write_api(write_options=WritePrecision.NS)

def write_sensor_data(sensor, value):
    point = Point(sensor).field("value", value)
    write_api.write(bucket=config.BUCKET, org=config.ORG, record=point)

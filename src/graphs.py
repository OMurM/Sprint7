import matplotlib.pyplot as plt
import pandas as pd
import time
from influxdb_client import InfluxDBClient

INFLUXDB_URL = "http://localhost:8086"
INFLUXDB_TOKEN = "xq40o5kHGrd2_YDQ53r5j5EJP9eiGvZQ1mU523G16OonMCQ97fjMqTXFaqtdMeI3rZ1ld5h_-PmRdjahARXdzQ=="
ORG = "Sprint7"
BUCKET = "iot"

client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=ORG)
query_api = client.query_api()

fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
fig.suptitle("Real-Time Sensor Dashboard")

plt.ion()

while True:
    query = f'''
    from(bucket: "{BUCKET}")
      |> range(start: -10m)
      |> filter(fn: (r) => r._measurement == "sensor_data")
      |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
      |> sort(columns: ["_time"])
    '''

    result = query_api.query_data_frame(query)
    if isinstance(result, list):
        df = result[0]
    else:
        df = result

    if df.empty:
        print("No data found!")
    else:
        df['_time'] = pd.to_datetime(df['_time'])

        window = 5
        df['temperature_smoothed'] = df['temperature'].rolling(window=window).mean()
        df['humidity_smoothed'] = df['humidity'].rolling(window=window).mean()
        df['soil_moisture_smoothed'] = df['soil_moisture'].rolling(window=window).mean()

        for ax in axes:
            ax.clear()

        axes[0].plot(df['_time'], df['temperature'], label='Raw', alpha=0.3)
        axes[0].plot(df['_time'], df['temperature_smoothed'], label='Smoothed', marker='o')
        axes[0].set_ylabel("Temperature (°C)")
        axes[0].legend()
        axes[0].grid()

        axes[1].plot(df['_time'], df['humidity'], label='Raw', alpha=0.3)
        axes[1].plot(df['_time'], df['humidity_smoothed'], label='Smoothed', marker='o')
        axes[1].set_ylabel("Humidity (%)")
        axes[1].legend()
        axes[1].grid()

        axes[2].plot(df['_time'], df['soil_moisture'], label='Raw', alpha=0.3)
        axes[2].plot(df['_time'], df['soil_moisture_smoothed'], label='Smoothed', marker='o')
        axes[2].set_ylabel("Soil Moisture")
        axes[2].set_xlabel("Time")
        axes[2].legend()
        axes[2].grid()

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.draw()
        plt.pause(5)

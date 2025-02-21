import matplotlib.pyplot as plt
import pandas as pd
from influxdb_client import InfluxDBClient

# InfluxDB connection settings
INFLUXDB_URL = "http://localhost:8086"
INFLUXDB_TOKEN = "xq40o5kHGrd2_YDQ53r5j5EJP9eiGvZQ1mU523G16OonMCQ97fjMqTXFaqtdMeI3rZ1ld5h_-PmRdjahARXdzQ=="
ORG = "Sprint7"
BUCKET = "iot"

# Create an InfluxDB client and query API
client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=ORG)
query_api = client.query_api()

# Define a Flux query to retrieve sensor data from the last hour
query = f'''
from(bucket: "{BUCKET}")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "sensor_data")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"])
'''

# Execute the query and convert the result to a DataFrame
result = query_api.query_data_frame(query)
if isinstance(result, list):
    df = result[0]
else:
    df = result

if df.empty:
    print("No data found!")
else:
    # Convert the '_time' column to datetime
    df['_time'] = pd.to_datetime(df['_time'])

    # Apply a rolling average with a window of 5 readings to smooth the data
    window = 5
    df['temperature_smoothed'] = df['temperature'].rolling(window=window).mean()
    df['humidity_smoothed'] = df['humidity'].rolling(window=window).mean()
    df['soil_moisture_smoothed'] = df['soil_moisture'].rolling(window=window).mean()

    # Plot the raw and smoothed sensor data
    plt.figure(figsize=(12, 7))
    
    # Temperature
    plt.plot(df['_time'], df['temperature'], label='Temperature (Raw)', alpha=0.3)
    plt.plot(df['_time'], df['temperature_smoothed'], label='Temperature (Smoothed)', marker='o')
    
    # Humidity
    plt.plot(df['_time'], df['humidity'], label='Humidity (Raw)', alpha=0.3)
    plt.plot(df['_time'], df['humidity_smoothed'], label='Humidity (Smoothed)', marker='o')
    
    # Soil Moisture
    plt.plot(df['_time'], df['soil_moisture'], label='Soil Moisture (Raw)', alpha=0.3)
    plt.plot(df['_time'], df['soil_moisture_smoothed'], label='Soil Moisture (Smoothed)', marker='o')
    
    plt.xlabel('Time')
    plt.ylabel('Sensor Value')
    plt.title('Sensor Data Over Time (Raw vs. Smoothed)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

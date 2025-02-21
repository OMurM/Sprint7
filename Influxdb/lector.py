from influxdb_client.rest import ApiException
from connection_component import InfluxDBConnection

def read_last_temperature():
    """Lee el último valor de temperatura desde InfluxDB."""
    connection = InfluxDBConnection(
        url="http://localhost:8086",
        token = "xq40o5kHGrd2_YDQ53r5j5EJP9eiGvZQ1mU523G16OonMCQ97fjMqTXFaqtdMeI3rZ1ld5h_-PmRdjahARXdzQ==",
        org="Sprint7",
        bucket="iot"
    )
    
    client = connection.get_client()
    query_api = connection.get_query_api(client)
    
    query = f'''
    from(bucket: "{connection.bucket}")
        |> range(start: -10m)
        |> filter(fn: (r) => r._measurement == "thermometer" and r._field == "temperature")
        |> last()
    '''

    try:
        tables = query_api.query(query)
        for table in tables:
            for record in table.records:
                print(f"Última temperatura registrada: {record.get_value()}°C")
    except ApiException as e:
        print(f"Error al consultar InfluxDB: {e}")

if __name__ == "__main__":
    read_last_temperature()

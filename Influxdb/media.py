from influxdb_client.rest import ApiException
from connection_component import InfluxDBConnection

def calculate_average_temperature():
    """Calcula la media de la temperatura de los últimos 2 minutos."""
    connection = InfluxDBConnection(
        url="http://localhost:8086",
        token="W6ibgZq6dNxOyTn7FrIqKaQfXDQacwPOKU8KjOcgugkw2ybi40PITM49fFKjWQAUKmMfKoOmhdjGxcPHjDZU5A==",
        org="Sprint7",
        bucket="iot"
    )
    
    client = connection.get_client()
    query_api = connection.get_query_api(client)
    
    query = f'''
    from(bucket: "{connection.bucket}")
        |> range(start: -2m)
        |> filter(fn: (r) => r._measurement == "thermometer" and r._field == "temperature")
        |> mean()
    '''

    try:
        tables = query_api.query(query)
        for table in tables:
            for record in table.records:
                print(f"Media de temperatura (últimos 2 minutos): {record.get_value()}°C")
    except ApiException as e:
        print(f"Error al consultar InfluxDB: {e}")

if __name__ == "__main__":
    calculate_average_temperature()

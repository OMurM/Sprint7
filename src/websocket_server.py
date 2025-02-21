import asyncio
import websockets
import json
import logging
from components.sensor import TemperatureSensor, HumiditySensor, SoilMoistureSensor

logging.basicConfig(level=logging.INFO)

clients = set()

temperature_sensor = TemperatureSensor()
humidity_sensor = HumiditySensor()
soil_moisture_sensor = SoilMoistureSensor()

ALERT_THRESHOLD_TEMPERATURE = 30.0
ALERT_THRESHOLD_HUMIDITY = 65.0
ALERT_THRESHOLD_SOIL_MOISTURE = 20.0

async def send_sensor_data(websocket):
    clients.add(websocket)
    try:
        while True:
            temperature = temperature_sensor.read_data()
            humidity = humidity_sensor.read_data()
            soil_moisture = soil_moisture_sensor.read_data()

            message = {
                "temperature": temperature,
                "humidity": humidity,
                "soil_moisture": soil_moisture,
                "alert": None
            }

            if temperature > ALERT_THRESHOLD_TEMPERATURE:
                message["alert"] = "Temperature is too high!"
            elif humidity > ALERT_THRESHOLD_HUMIDITY:
                message["alert"] = "Humidity is too high!"
            elif soil_moisture < ALERT_THRESHOLD_SOIL_MOISTURE:
                message["alert"] = "Soil moisture is too low!"

            logging.info(f"Sending data to clients: {json.dumps(message, indent=2)}")

            for client in clients:
                await client.send(json.dumps(message))
                
            await asyncio.sleep(3)  # Adjust update interval as needed
    except websockets.exceptions.ConnectionClosed:
        logging.info("Client disconnected")
    finally:
        clients.remove(websocket)

async def main():
    logging.info("✅ WebSocket server running on ws://localhost:8765")
    async with websockets.serve(send_sensor_data, "localhost", 8765):
        await asyncio.Future()  # Keep the server running

if __name__ == "__main__":
    asyncio.run(main())

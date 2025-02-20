import asyncio
import websockets
import json
import logging
from components.sensor import TemperatureSensor, HumiditySensor, SoilMoistureSensor

# Configure logging
logging.basicConfig(level=logging.INFO)

clients = set()

temperature_sensor = TemperatureSensor()
humidity_sensor = HumiditySensor()
soil_moisture_sensor = SoilMoistureSensor()

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
                "soil_moisture": soil_moisture
            }

            logging.info(f"Sending data to clients: {json.dumps(message, indent=2)}")

            for client in clients:
                await client.send(json.dumps(message))

            await asyncio.sleep(3)
    except websockets.exceptions.ConnectionClosed:
        logging.info("Client disconnected")
    finally:
        clients.remove(websocket)

async def main():
    logging.info("✅ WebSocket server running on ws://localhost:8765")
    async with websockets.serve(send_sensor_data, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
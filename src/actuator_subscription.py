# src/actuator_subscription.py

import asyncio
import websockets
import json
from components.actuator import WaterPump, Fan

# Instantiate actuators
water_pump = WaterPump()
fan = Fan()

async def actuator_subscription():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            print(f"Received Data: {data}")

            # Control actuators based on sensor data
            if data["soil_moisture"] < 20:
                water_pump.activate()
            else:
                water_pump.deactivate()

            if data["temperature"] > 30:
                fan.activate()
            else:
                fan.deactivate()

asyncio.run(actuator_subscription())

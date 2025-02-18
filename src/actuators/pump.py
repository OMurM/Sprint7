import asyncio
import websockets
import config  # Import config

async def pump_control():
    async with websockets.connect(config.WEBSOCKET_URL) as websocket:
        while True:
            message = await websocket.recv()
            print(f"Pump received: {message}")
            if "moisture" in message and float(message.split(":")[1]) < 40:
                print("🚰 Activating water pump!")

asyncio.run(pump_control())

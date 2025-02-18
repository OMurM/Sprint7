import asyncio
import websockets
import random
import config  # Import configuration

clients = set()

async def send_sensor_data(websocket, path):
    clients.add(websocket)
    try:
        while True:
            temp = random.uniform(18, 30)
            humidity = random.uniform(40, 60)
            moisture = random.uniform(20, 50)

            message = f"temperature:{temp:.2f}, humidity:{humidity:.2f}, moisture:{moisture:.2f}"
            print(f"Sending: {message}")

            for client in clients:
                await client.send(message)

            await asyncio.sleep(5)
    finally:
        clients.remove(websocket)

start_server = websockets.serve(send_sensor_data, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

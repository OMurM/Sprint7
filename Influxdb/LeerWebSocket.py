import asyncio
import websockets

async def receive_data():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        print("Conectado al servidor WebSocket")
        try:
            while True:
                message = await websocket.recv()
                print(f"Datos recibidos: {message}")
        except websockets.exceptions.ConnectionClosed:
            print("Conexión cerrada por el servidor.")

if __name__ == "__main__":
    asyncio.run(receive_data())

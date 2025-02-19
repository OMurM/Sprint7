# src/main.py

import asyncio
import subprocess
from websocket_server import main as websocket_main
from actuator_subscription import actuator_subscription

async def run_all():
    # Run the WebSocket server
    asyncio.create_task(websocket_main())

    # Run actuator subscription
    asyncio.create_task(actuator_subscription())

    await asyncio.Future()  # Keep the process alive

if __name__ == "__main__":
    asyncio.run(run_all())

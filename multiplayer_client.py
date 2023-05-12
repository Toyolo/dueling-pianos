import asyncio
import websockets

async def send_message(message):
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(message)

# Example of sending a message
asyncio.get_event_loop().run_until_complete(send_message('Hello, world!'))

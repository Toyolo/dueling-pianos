import asyncio
import websockets

connected_players = set()

async def handler(websocket, path):
    # Register player.
    connected_players.add(websocket)
    try:
        async for message in websocket:
            # Broadcast incoming messages to all connected players.
            await asyncio.wait([player.send(message) for player in connected_players])
    finally:
        # Unregister player.
        connected_players.remove(websocket)

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


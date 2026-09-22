import asyncio
import websockets

CLIENT_ID = "client1"

async def receive_messages(websocket):
    while True:
        response = await websocket.recv()
        print(f"\n{response}")
        print(f"{CLIENT_ID}: ", end="", flush=True)

async def send_messages(websocket):
    loop = asyncio.get_event_loop()
    print("Format: target_id:message   (उदा. client2:Hello)")
    while True:
        message = await loop.run_in_executor(None, input, f"{CLIENT_ID}: ")
        await websocket.send(message)

async def main():
    uri = f"ws://127.0.0.1:8000/ws/{CLIENT_ID}"
    async with websockets.connect(uri) as websocket:
        print(f"{CLIENT_ID} connected")
        await asyncio.gather(
            receive_messages(websocket),
            send_messages(websocket)
        )

asyncio.run(main())
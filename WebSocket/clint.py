import asyncio
import websockets


async def main():

    async with websockets.connect(
        "ws://127.0.0.1:8000/ws"
    ) as websocket:

        print("Connected to server")
        print("Type 'exit' to close connection")

        while True:

            message = input("You: ")

            if message == "exit":
                break

            await websocket.send(message)

            response = await websocket.recv()

            print("Server:", response)


asyncio.run(main())
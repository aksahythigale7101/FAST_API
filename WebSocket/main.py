from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    print("WebSocket Connected")

    try:
        while True:

            message = await websocket.receive_text()

            print("Client sent:", message)

            await websocket.send_text(
                f"Server received: {message}"
            )

    except WebSocketDisconnect:

        print("Client Disconnected")
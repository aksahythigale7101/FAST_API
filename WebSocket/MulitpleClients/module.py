from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        # client_id -> websocket असा dictionary
        self.active_connections: dict[str, WebSocket] = {}

    async def connect(self, client_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        print(f"{client_id} connected. Total: {len(self.active_connections)}")

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
        print(f"{client_id} disconnected. Total: {len(self.active_connections)}")

    async def send_to_client(self, target_id: str, message: str, sender_id: str):
        if target_id in self.active_connections:
            await self.active_connections[target_id].send_text(f"[{sender_id}]: {message}")
        else:
            # सेंडरला कळवायचं की target उपलब्ध नाही
            if sender_id in self.active_connections:
                await self.active_connections[sender_id].send_text(
                    f"[Server]: {target_id} is not connected."
                )

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(client_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # फॉरमॅट: "target_id:message"  उदा. "client2:Hello"
            if ":" in data:
                target_id, message = data.split(":", 1)
                target_id = target_id.strip()
                message = message.strip()
                await manager.send_to_client(target_id, message, client_id)
            else:
                await websocket.send_text("[Server]: Format is target_id:message (e.g. client2:Hello)")
    except WebSocketDisconnect:
        manager.disconnect(client_id)
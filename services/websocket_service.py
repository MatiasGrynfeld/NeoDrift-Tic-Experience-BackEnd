from models.connection_manager import ConnectionManager

class WebSocketService:
    def __init__(self):
        self.manager = ConnectionManager()

    async def connect(self, websocket: WebSocket):
        await self.manager.connect(websocket)

    def disconnect(self, websocket: WebSocket):
        self.manager.disconnect(websocket)

    async def handle_message(self, message: str, websocket: WebSocket):
        await self.manager.send_personal_message(f"Mensaje recibido: {message}", websocket)
        await self.manager.broadcast(f"Cliente dice: {message}")
from fastapi import WebSocket, WebSocketDisconnect
from services.websocket_service import WebSocketService

websocket_service = WebSocketService()

async def websocket_endpoint(websocket: WebSocket):
    await websocket_service.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await websocket_service.handle_message(data, websocket)
    except WebSocketDisconnect:
        websocket_service.disconnect(websocket)

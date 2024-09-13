from fastapi import APIRouter, WebSocket
from controllers.websocket_controller import websocket_endpoint

websocket_router = APIRouter()

@websocket_router.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)

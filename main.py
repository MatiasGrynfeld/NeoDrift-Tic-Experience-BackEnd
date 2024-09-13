from fastapi import FastAPI
from routes.websocket_routes import websocket_router

app = FastAPI()

app.include_router(websocket_router)

# uvicorn main:app --reload -> to run the server
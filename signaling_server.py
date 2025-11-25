from fastapi import FastAPI, WebSocket
from aiortc import RTCPeerConnection
import json

app = FastAPI()

pcs = set()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    pc = RTCPeerConnection()
    pcs.add(pc)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            # Handle SDP offer/answer here
            print("Received:", message)
    except Exception as e:
        print("Connection closed:", e)
    finally:
        pcs.discard(pc)
        await pc.close()

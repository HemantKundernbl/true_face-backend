from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deepface import DeepFace
import base64
import cv2
import numpy as np

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageData(BaseModel):
    selfie: str
    frame: str

@app.post("/verify")
async def verify(request: Request):
    data = await request.json()
    selfie_data = data['selfie']
    frame_data = data['frame']

    # Decode base64 images
    selfie = cv2.imdecode(np.frombuffer(base64.b64decode(selfie_data), np.uint8), cv2.IMREAD_COLOR)
    frame = cv2.imdecode(np.frombuffer(base64.b64decode(frame_data), np.uint8), cv2.IMREAD_COLOR)

    # Perform verification
    result = DeepFace.verify(selfie, frame)
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

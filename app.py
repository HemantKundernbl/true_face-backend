from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deepface import DeepFace
import cv2
import numpy as np
import os

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_image(file: UploadFile):
    try:
        # Read image file
        image = np.frombuffer(file.file.read(), np.uint8)
        # Decode numpy array to image
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if image is None:
            raise ValueError("Image decoding failed")
        return image
    except Exception as e:
        raise ValueError(f"Failed to read image: {str(e)}")

@app.post("/verify")
async def verify(selfie: UploadFile = File(...), frame: UploadFile = File(...), model: str = Form("ArcFace")):
    # Read uploaded images
    try:
        selfie_image = read_image(selfie)
        frame_image = read_image(frame)
    except ValueError as e:
        return {"error": str(e)}

    # Perform verification
    try:
        result = DeepFace.verify(selfie_image, frame_image, model_name=model)
        return result
    except Exception as e:
        return {"error": f"Verification failed: {str(e)}"}

@app.post("/analyze")
async def analyze(image: UploadFile = File(...)):
    # Read uploaded image
    try:
        image = read_image(image)
    except ValueError as e:
        return {"error": str(e)}

    # Perform analysis
    try:
        result = DeepFace.analyze(image)
        return result
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

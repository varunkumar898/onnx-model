from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# NOTE: onnxruntime is not available on Windows/ARM64 via pip in many cases.
# For development on an ARM64 Python we provide a temporary stubbed inference
# implementation below so the API can run without the onnxruntime dependency.
from PIL import Image
import numpy as np
import io
import random

app = FastAPI(title="Image Recognition API")

# Allow frontend (HTML) to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Class labels (simplified for demo)
labels = ["cat", "dog", "car", "person", "chair", "bird", "flower"]


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Temporary stubbed predict endpoint for development.

    This returns a random label and confidence so the frontend and API
    can be developed without requiring the onnxruntime wheel on Windows/ARM64.
    Replace this with real ONNX inference when running on a compatible
    Python (x86_64) or in WSL/conda where onnxruntime is available.
    """
    try:
        # consume the uploaded file (we don't run a model here)
        _ = await file.read()

        label = random.choice(labels)
        confidence = round(random.random(), 3)

        return JSONResponse({
            "label": label,
            "confidence": confidence,
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

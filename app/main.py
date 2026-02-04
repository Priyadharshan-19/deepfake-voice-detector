from fastapi import FastAPI, UploadFile, File, Header, HTTPException, Depends
from app.engine import VoiceEngine
from app.config import Config
import shutil
import os

app = FastAPI(title="India AI Impact Buildathon - AI Voice Detector")

# Initialize engine globally
try:
    engine = VoiceEngine()
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    engine = None

async def verify_api_key(x_api_key: str = Header(None, alias="X-API-Key")):
    if x_api_key != Config.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

@app.post("/predict")
async def predict_voice(file: UploadFile = File(...), api_key: str = Depends(verify_api_key)):
    if engine is None:
        raise HTTPException(status_code=500, detail="Model not loaded. Check server logs.")
    
    os.makedirs("temp", exist_ok=True)
    temp_path = os.path.join("temp", file.filename)
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        label, confidence = engine.predict(temp_path)
        return {
            "status": "success",
            "prediction": label,
            "confidence_score": round(confidence, 4),
            "is_deepfake": True if label == "AI-Generated" else False
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.get("/health")
def health():
    return {"status": "ready" if engine else "error"}
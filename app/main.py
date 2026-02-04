from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from app.engine import predict_voice
from app.config import Config
import time

app = FastAPI(title="India AI Voice Detection API")

@app.post("/detect-voice")
async def detect(file: UploadFile = File(...), api_key: str = Header(None)):
    # 1. Authentication (Buildathon Requirement)
    if api_key != Config.API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid API Key")
    
    start_time = time.time()
    try:
        content = await file.read()
        label, confidence = predict_voice(content)
        latency = (time.time() - start_time) * 1000 
        
        # 2. Correct JSON Format for Submission
        return {
            "status": "success",
            "filename": file.filename,
            "classification": label,
            "confidence_score": round(confidence, 4),
            "latency_ms": round(latency, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
                            












                            
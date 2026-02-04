import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Match the variable name in your .env
    API_KEY = os.getenv("API_KEY", "IndiaAI_Impact_Secret_2026")
    MODEL_PATH = os.getenv("MODEL_PATH", "models/voice_classifier.pkl")
    DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "t")
import librosa
import numpy as np
import joblib
import io
from app.config import Config

# Global variable to hold the model in memory
model = None

def load_model():
    global model
    try:
        model = joblib.load(Config.MODEL_PATH)
    except Exception as e:
        print(f"⚠️ Model not found at {Config.MODEL_PATH}. Run train_dummy.py first.")

def extract_features(audio_bytes):
    # Load audio at 16kHz sample rate (standard for ASVspoof)
    y, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
    # Extract 40 MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    # Return the mean of each feature over time
    return np.mean(mfccs.T, axis=0).reshape(1, -1)

def predict_voice(audio_bytes):
    if model is None: load_model()
    if model is None: return "Error", 0.0
    
    features = extract_features(audio_bytes)
    prediction = model.predict(features)[0]
    # Get probability for the "AI-Generated" class
    prob = np.max(model.predict_proba(features)[0])
    
    label = "AI-Generated" if prediction == 1 else "Human"
    return label, float(prob)
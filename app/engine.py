import librosa
import numpy as np
import pickle
import os
from app.config import Config

class VoiceEngine:
    def __init__(self):
        # Prevent EOFError by checking file size first
        if not os.path.exists(Config.MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at: {Config.MODEL_PATH}")
        
        if os.path.getsize(Config.MODEL_PATH) == 0:
            raise EOFError(f"The model file at {Config.MODEL_PATH} is empty (0 bytes). Please re-train and save the model.")

        with open(Config.MODEL_PATH, 'rb') as f:
            self.model = pickle.load(f)

    def extract_features(self, audio_path):
        # Load audio and extract MFCCs
        y, sr = librosa.load(audio_path, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        return np.mean(mfccs.T, axis=0)

    def predict(self, audio_path):
        features = self.extract_features(audio_path)
        prediction = self.model.predict([features])[0]
        probabilities = self.model.predict_proba([features])[0]
        confidence = np.max(probabilities)
        
        # 0 = Real, 1 = AI-Generated (Standard deepfake mapping)
        label = "AI-Generated" if prediction == 1 else "Real"
        return label, float(confidence)
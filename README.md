AI-Generated Voice Detection System 🎙️🤖
Project Title: India AI Impact Buildathon - Deepfake Voice Detector

Problem Statement: Problem 1 - AI-Generated Voice Detection

Deployed URL: https://deepfake-voice-detector-1.onrender.com/predict

API Key: IndiaAI_Impact_Secret_2026 (Use this in the X-API-Key header)

📜 Project Overview
This project provides a robust, scalable, and secure API for detecting AI-generated (deepfake) voices. Built for the India AI Impact Buildathon, it utilizes advanced signal processing and machine learning to distinguish between genuine human speech and synthetic audio.

Key Features
Real-time Detection: Low-latency inference for immediate results.

Intelligent Logic: Uses Mel-frequency cepstral coefficients (MFCCs) for high-fidelity feature extraction.

Secure API: Implements X-API-Key header authentication to protect against unauthorized access.

Standardized JSON: Returns evaluation-ready results in a clear format.

🧠 Intelligent Logic & Methodology
Unlike simple file-type checks, this system analyzes the acoustic fingerprint of the audio.

1. Feature Extraction (MFCC)
AI-generated voices often leave subtle artifacts in their frequency distributions. Our system extracts 40 Mel-frequency cepstral coefficients (MFCCs), which capture the physical characteristics of the "vocal tract" represented in the audio signal.

2. Machine Learning Pipeline
Preprocessing: Audio is standardized using librosa to ensure consistent sampling rates.

Classification: A pre-trained Random Forest Classifier analyzes the mean MFCC features to provide a binary classification: Real or AI-Generated.

Confidence Scoring: The model doesn't just guess; it provides a confidence score based on probability distributions, ensuring transparency in high-stakes fraud detection.

🚀 API Usage
Endpoint: POST /predict
Submit an audio file to determine its authenticity.

Headers:

JSON
{
  "X-API-Key": "IndiaAI_Impact_Secret_2026",
  "Content-Type": "multipart/form-data"
}
Request Body:

file: An audio file (.wav, .mp3, or .m4a).

Response Format:

JSON
{
  "status": "success",
  "prediction": "AI-Generated",
  "confidence_score": 0.9842,
  "is_deepfake": true,
  "message": "Analysis completed successfully"
}
🛠️ Project Structure
Plaintext
deepfake-voice-detector/
├── app/
│   ├── main.py          # FastAPI routes & API Key security
│   ├── engine.py        # Logic for MFCC extraction & ML inference
│   └── config.py        # Environment & Key management
├── models/
│   └── voice_classifier.pkl # Trained Random Forest Model
├── .env.example         # Template for security keys
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
👨‍💻 Author
Priyadharshan M. Second-year B.E. (CSE) student at SNS College of Technology Internshala Student Partner (ISP)

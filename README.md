🎙️ AI-Generated Voice Detection System
India AI Impact Buildathon – Deepfake Voice Detector
📌 Problem Statement

Problem 1: AI-Generated Voice Detection

With the rapid rise of voice-cloning and synthetic speech technologies, distinguishing between real and AI-generated voices has become critical—especially in fraud prevention, authentication systems, and secure communications.

🌐 Deployment Details

Live API URL:
👉 https://deepfake-voice-detector-1.onrender.com/predict

Authentication:
API Key (use in request header):

X-API-Key: IndiaAI_Impact_Secret_2026

📜 Project Overview

This project delivers a robust, scalable, and secure REST API that accurately detects AI-generated (deepfake) voices from audio inputs. Developed for the India AI Impact Buildathon, the system leverages signal processing techniques and machine learning to analyze acoustic patterns and classify audio as either real human speech or synthetic voice.

✨ Key Features

Real-time Detection
Low-latency inference enables instant classification of audio inputs.

Intelligent Audio Analysis
Uses MFCC-based feature extraction to capture subtle acoustic artifacts.

Secure API Access
Implements X-API-Key authentication to prevent unauthorized usage.

Standardized JSON Responses
Evaluation-ready output with prediction, confidence score, and flags.

🧠 Intelligent Logic & Methodology

Unlike superficial file or metadata checks, this system performs deep acoustic analysis of the audio signal.

1️⃣ Feature Extraction – MFCC

Extracts 40 Mel-Frequency Cepstral Coefficients (MFCCs)

Captures frequency-domain characteristics that reflect vocal tract behavior

Helps identify artifacts commonly present in AI-generated speech

2️⃣ Machine Learning Pipeline

Preprocessing:
Audio is standardized using librosa for consistent sampling rates and signal normalization.

Classification:
A pre-trained Random Forest Classifier analyzes the mean MFCC features to classify audio as:

Real

AI-Generated

Confidence Scoring:
Outputs probability-based confidence scores to ensure transparency and reliability in fraud-sensitive applications.

🚀 API Usage
Endpoint
POST /predict

Request Headers
{
  "X-API-Key": "IndiaAI_Impact_Secret_2026",
  "Content-Type": "multipart/form-data"
}

Request Body

file: Audio file (.wav, .mp3, or .m4a)

Response Format
{
  "status": "success",
  "prediction": "AI-Generated",
  "confidence_score": 0.9842,
  "is_deepfake": true,
  "message": "Analysis completed successfully"
}

🛠️ Project Structure
deepfake-voice-detector/
├── app/
│   ├── main.py          # FastAPI routes & API key authentication
│   ├── engine.py        # MFCC extraction & ML inference logic
│   └── config.py        # Environment variables & configuration
├── models/
│   └── voice_classifier.pkl   # Trained Random Forest model
├── .env.example         # API key & environment template
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

👨‍💻 Author

Priyadharshan M.
Second-Year B.E. (Computer Science & Engineering)
SNS College of Technology
Internshala Student Partner (ISP)

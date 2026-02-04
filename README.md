# 🎙️ AI-Generated Voice Detection System 🤖

### *India AI Impact Buildathon – Deepfake Voice Detector*

---

## 📜 Project Overview

This project delivers a **secure, scalable, and production-ready API** for detecting AI-generated (deepfake) voices. Built for the **India AI Impact Buildathon**, it leverages **advanced signal processing and machine learning** techniques to analyze acoustic fingerprints and accurately classify audio as **Real** or **AI-Generated**.

---

## 🛠️ Project Structure

```
deepfake-voice-detector/
├── app/
│   ├── main.py              # FastAPI routes & API key security
│   ├── engine.py            # MFCC extraction & ML inference
│   └── config.py            # Environment & key management
├── models/
│   └── voice_classifier.pkl # Trained Random Forest model
├── .env.example             # Environment variable template
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚨 Problem Statement

**Problem 1: AI-Generated Voice Detection**

With the rapid growth of voice cloning and deepfake audio technologies, identifying synthetic speech has become essential for preventing fraud, impersonation, and misinformation.

---

## 🌐 Live Deployment

### 🔹 API Endpoint

👉 [https://deepfake-voice-detector-1.onrender.com/predict](https://deepfake-voice-detector-1.onrender.com/predict)

### 🔹 Interactive API Documentation (Upload & Test Audio)

👉 [https://deepfake-voice-detector-1.onrender.com/docs](https://deepfake-voice-detector-1.onrender.com/docs)

Use this Swagger UI to:

* Upload an audio file (`.wav`, `.mp3`, `.m4a`)
* Provide the required `X-API-Key`
* Execute the `/predict` endpoint
* Instantly view prediction results and confidence score

> **Tip:** Open `/docs`, select the `/predict` endpoint, click **Try it out**, upload your audio file, add the API key, and execute.

---

## 🔐 API Authentication

**API Key:**

```
IndiaAI_Impact_Secret_2026
```

**Header Usage:**

```
X-API-Key: IndiaAI_Impact_Secret_2026
```

---

## ✨ Key Features

* ⚡ **Real-Time Detection** – Low-latency inference for immediate results
* 🧠 **Intelligent Audio Analysis** – MFCC-based feature extraction
* 🔐 **Secure API Access** – X-API-Key header authentication
* 📊 **Confidence Scoring** – Probability-driven prediction transparency
* 🔁 **Standardized JSON Responses** – Easy integration with applications

---

## 🧠 Intelligent Logic & Methodology

### 1️⃣ Feature Extraction (MFCC)

The system extracts **40 Mel-Frequency Cepstral Coefficients (MFCCs)** to capture subtle acoustic artifacts commonly introduced by AI-generated voices.

### 2️⃣ Machine Learning Pipeline

* **Preprocessing:** Audio normalization and resampling using `librosa`
* **Classification:** Pre-trained **Random Forest Classifier**
* **Confidence Scoring:** Probability-based decision confidence for transparency

---

## 🚀 API Usage

### 🔹 Endpoint

```
POST /predict
```

### 🔹 Headers

```json
{
  "X-API-Key": "IndiaAI_Impact_Secret_2026",
  "Content-Type": "multipart/form-data"
}
```

### 🔹 Request Body

* **file**: Audio file (`.wav`, `.mp3`, `.m4a`)

### 🔹 Sample Response

```json
{
  "status": "success",
  "prediction": "AI-Generated",
  "confidence_score": 0.9842,
  "is_deepfake": true,
  "message": "Analysis completed successfully"
}
```

---

## 🧪 Tech Stack

* **Backend:** FastAPI
* **Machine Learning:** Random Forest Classifier
* **Audio Processing:** Librosa
* **Deployment:** Render
* **Language:** Python

---

## 👨‍💻 Author

**Priyadharshan M.**
🎓 Second-Year B.E. (CSE)
🏫 SNS College of Technology

> *“Building trust in the age of artificial intelligence starts with the ability to detect what isn’t real.”*

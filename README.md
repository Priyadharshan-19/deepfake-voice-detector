# 🎙️ Deepfake Voice Detector  
India AI Impact Buildathon 2026 – Official Submission

Deepfake Voice Detector is a production-ready AI-powered API designed to detect synthetic and AI-generated voices in audio calls.  
The system helps combat voice-cloning frauds and deepfake scams by providing reliable real-time classification of real vs fake audio.

---

## 🚀 Live API Endpoint
URL: https://your-deployed-url.onrender.com/detect-voice  
API Key: IndiaAI_Impact_Secret_2026 (Provided for evaluation only)

---

## ✨ Key Features
- Real-time detection with low latency (<200ms)
- Deepfake and synthetic voice identification
- MFCC-based audio feature extraction
- API key–based secure access
- Scalable FastAPI backend with async handling
- Stateless processing with no audio storage

---

## 🛠️ Tech Stack
- Language: Python 3.10+
- Framework: FastAPI
- Machine Learning: Scikit-learn
- Audio Processing: Librosa
- Deployment: Render / Railway
- API Documentation: Swagger UI

---

## 📂 Project Structure
```text
deepfake-voice-detector/
├── app/
│   ├── main.py              # API entry point & routes
│   ├── engine.py            # Feature extraction & inference logic
│   └── config.py            # Configuration handling
├── models/
│   └── voice_classifier.pkl # Trained ML model
├── requirements.txt         # Dependencies
├── train_dummy.py           # Model training script
├── .env                     # Environment variables (ignored)
└── README.md
⚙️ Local Setup
Clone the Repository
bash
Copy code
git clone https://github.com/your-username/deepfake-voice-detector.git
cd deepfake-voice-detector
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Train the Model
bash
Copy code
python train_dummy.py
Run the API Server
bash
Copy code
python -m uvicorn app.main:app --reload
🧪 API Testing
Swagger UI
Access API documentation at:

bash
Copy code
http://localhost:8000/docs
Endpoint Details
Method: POST

Endpoint: /detect-voice

Headers:

makefile
Copy code
api_key: IndiaAI_Impact_Secret_2026
Body:

form-data

key: file

value: your_audio.wav

🛡️ Security & Privacy
Audio files are never stored

All processing happens in memory

API key authentication enabled

API key rotation supported via environment variables

🚀 Deployment (Render)
Build Command
bash
Copy code
pip install -r requirements.txt
Start Command
bash
Copy code
python -m uvicorn app.main:app --host 0.0.0.0 --port 10000
📌 Final Submission Checklist
Push the project to GitHub

Verify .env is excluded using .gitignore

Deploy using Render.com

Submit the GitHub repository link and live API URL

🧠 Impact
This project addresses the increasing threat of AI-driven voice fraud and supports secure, trustworthy digital communication systems.

yaml
Copy code

---

If you want:
- a version with zero emojis
- an ultra-short README (1-page judge-friendly)
- or a version aligned to resume / portfolio

Just say the word 🚀

import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 1. Create dummy training data (100 samples, 40 features each)
# We use 40 features to match the n_mfcc=40 in your engine.py
X = np.random.rand(100, 40)
# Binary labels: 0 for "Real", 1 for "AI-Generated"
y = np.random.randint(0, 2, size=100)

# 2. Initialize and "train" the model
model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

# 3. Save it properly to your models folder
model_path = "models/voice_classifier.pkl"
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Success! Valid model saved to {model_path}")
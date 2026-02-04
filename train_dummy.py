import sklearn.ensemble
import joblib
import numpy as np
import os

# Ensure the models folder exists
os.makedirs('models', exist_ok=True)

# Fake data for 40 MFCC features
X = np.random.rand(100, 40)
y = np.random.randint(0, 2, 100) # 0=Human, 1=AI

model = sklearn.ensemble.RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'models/voice_classifier.pkl')
print("✅ Placeholder model created successfully!")
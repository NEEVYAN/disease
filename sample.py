import pickle
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'models', 'diabetes.sav')

try:
    with open(model_path, 'rb') as f:
        diabetic_model = pickle.load(f)
    print("Model loaded successfully:", diabetic_model)
except Exception as e:
    print(f"Error loading model: {e}")
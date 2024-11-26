from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from the frontend

# Load the heart disease prediction model
script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'models', 'heart.sav')
print(f"Model Path: {model_path}")

try:
    with open(model_path, 'rb') as f:
        heart_model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    heart_model = None
    print(f"Error loading model: {e}")


@app.route('/api/heart', methods=['POST'])
def heart_prediction():
    global heart_model

    if heart_model is None:
        try:
            print("Attempting to reload the model...")
            with open(model_path, 'rb') as f:
                heart_model = pickle.load(f)
            print("Model reloaded successfully.")
        except Exception as e:
            print(f"Error reloading model: {e}")
            return jsonify({'error': 'Model is not loaded. Cannot perform prediction.'}), 500

    # Parse the input data
    data = request.get_json()
    print("Received Data:", data)

    try:
        # Extract and validate input values
        input_values = [
            data.get('Age', 0),
            data.get('Sex', 0),
            data.get('CP', 0),
            data.get('Trestbps', 0),
            data.get('Chol', 0),
            data.get('FBS', 0),
            data.get('Restecg', 0),
            data.get('Thalach', 0),
            data.get('Exang', 0),
            data.get('Oldpeak', 0),
            data.get('Slope', 0),
            data.get('CA', 0),
            data.get('Thal', 0)
        ]

        # Prepare the data for prediction
        input_array = np.array(input_values).reshape(1, -1)
        print("Input Array for Model:", input_array)

        # Make the prediction
        prediction = heart_model.predict(input_array)
        print("Model Prediction:", prediction)

        # Format the result
        result = "The person is having heart disease" if prediction[0] == 1 else "The person does not have heart disease"
        return jsonify({'diagnosis': result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': f'An error occurred: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8081) 

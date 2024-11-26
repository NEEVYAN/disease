from flask import Flask, request, jsonify
from flask_cors import CORS 
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app) 


script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'models', 'diabetes.sav')
print(f"Model Path: {model_path}")

try:
    with open(model_path, 'rb') as f:
        diabetic_model = pickle.load(f)
    print("Model loaded successfully:", diabetic_model)
except Exception as e:
    diabetic_model = None
    print(f"Error loading model: {e}")


@app.route('/api/ml', methods=['POST'])
def api_ml():
    data = request.get_json() 
    print("Received Data:", data) 
    global diabetic_model

    if diabetic_model is None:
        try:
            print("Attempting to reload the model...")
            with open(model_path, 'rb') as f:
                diabetic_model = pickle.load(f)
            print("Model reloaded successfully.")
        except Exception as e:
            print(f"Error reloading model: {e}")
            return jsonify({'error': 'Model is not loaded. Cannot perform prediction.'}), 500

    data = request.get_json()
    print("Received Data:", data)

    try:
        input_values = [
            data.get('Pregnancies', 0),
            data.get('Glucose', 0),
            data.get('BloodPressure', 0),
            data.get('SkinThickness', 0),
            data.get('Insulin', 0),
            data.get('BMI', 0),
            data.get('DiabetesPedigreeFunction', 0),
            data.get('Age', 0)
        ]
        input_array = np.array(input_values).reshape(1, -1)
        # print("Input Array for Model:", input_array)

        prediction = diabetic_model.predict(input_array)
        # print("Model Prediction:", prediction)

        result = "The person is having diabetes" if prediction[0] == 1 else "The person does not have diabetes"
        return jsonify({'diagnosis': result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': f'An error occurred: {e}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  
    app.run(debug=True, host='0.0.0.0', port=port) 

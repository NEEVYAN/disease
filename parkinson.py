from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)  

script_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(script_dir, 'models', 'parkinsons.sav')
print(f"Model Path: {model_path}")

try:
    with open(model_path, 'rb') as f:
        parkinsons_model = pickle.load(f)
    print("Model loaded successfully.")
except Exception as e:
    parkinsons_model = None
    print(f"Error loading model: {e}")

@app.route('/api/parkinsons', methods=['POST'])
def predict_parkinsons():
    global parkinsons_model

    if parkinsons_model is None:
        try:
            print("Attempting to reload the model...")
            with open(model_path, 'rb') as f:
                parkinsons_model = pickle.load(f)
            print("Model reloaded successfully.")
        except Exception as e:
            print(f"Error reloading model: {e}")
            return jsonify({'error': 'Model is not loaded. Cannot perform prediction.'}), 500

 
    data = request.get_json()
    print("Received Data:", data)

    try:
       
        input_values = [
            data.get('MDVP_FoHz', 0),
            data.get('MDVP_FhiHz', 0),
            data.get('MDVP_FloHz', 0),
            data.get('MDVP_JitterPercent', 0),
            data.get('MDVP_JitterAbs', 0),
            data.get('MDVP_RAP', 0),
            data.get('MDVP_PPQ', 0),
            data.get('Jitter_DDP', 0),
            data.get('MDVP_Shimmer', 0),
            data.get('MDVP_Shimmer_dB', 0),
            data.get('Shimmer_APQ3', 0),
            data.get('Shimmer_APQ5', 0),
            data.get('MDVP_APQ', 0),
            data.get('Shimmer_DDA', 0),
            data.get('NHR', 0),
            data.get('HNR', 0),
            data.get('RPDE', 0),
            data.get('DFA', 0),
            data.get('spread1', 0),
            data.get('spread2', 0),
            data.get('D2', 0),
            data.get('PPE', 0),
        ]

 
        input_array = np.array(input_values).reshape(1, -1)



        prediction = parkinsons_model.predict(input_array)
       

        result = "The person is likely to have Parkinson's disease." if prediction[0] == 1 else "The person is not likely to have Parkinson's disease."
        return jsonify({'diagnosis': result})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': f'An error occurred: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8082)  # Run on port 8082

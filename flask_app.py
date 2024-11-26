from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle CORS for frontend requests

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from different origins

@app.route('/api/ml', methods=['POST'])


def api_ml():
    data = request.get_json()
    result = "ML result based on: " + data.get('data')
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, port=8080)

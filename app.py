import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from detector.classify import classify_text

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    # Input validation
    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400
    if len(text) < 20:
        return jsonify({'error': 'Text is too short, must be at least 20 characters'}), 400

    try:
        result = classify_text(text)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': 'An error occurred during classification', 'details': str(e)}), 500

# ✅ Use only one block here
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

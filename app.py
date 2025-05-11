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
    if len(text) < 20:  # Example: Minimum length check
        return jsonify({'error': 'Text is too short, must be at least 20 characters'}), 400

    try:
        result = classify_text(text)
        return jsonify(result)
    except Exception as e:
        # Handle exceptions from classify_text
        return jsonify({'error': 'An error occurred during classification', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
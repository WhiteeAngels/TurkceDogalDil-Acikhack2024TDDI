from flask import Flask, request, jsonify, render_template
from data_processing import DataProcessing

app = Flask(__name__)
data_processor = DataProcessing()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({"error": "Metin gerekli"}), 400

    try:
        analysis_result = data_processor.process_text(text)
        return jsonify(analysis_result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

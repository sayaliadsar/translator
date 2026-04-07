
from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    src = data.get('src', 'mr')   # mr or en
    dest = data.get('dest', 'en')
    
    if not text.strip():
        return jsonify({'translated': ''})
    try:
        result = GoogleTranslator(source=src, target=dest).translate(text)
        return jsonify({'translated': result})
    except Exception as e:
        return jsonify({'translated': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
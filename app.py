from flask import Flask, render_template, request, jsonify
from cv_parser import parse_cv
from ai_suggestions import get_improvement_suggestions
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'cv' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    cv_file = request.files['cv']
    job_desc = request.form.get('job_description', '')
    
    if cv_file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    file_path = os.path.join(UPLOAD_FOLDER, cv_file.filename)
    cv_file.save(file_path)
    
    try:
        cv_data = parse_cv(file_path)
        suggestions = get_improvement_suggestions(cv_data, job_desc)
        return jsonify({
            'success': True,
            'cv_data': cv_data,
            'suggestions': suggestions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
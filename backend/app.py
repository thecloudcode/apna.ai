# app.py
"""
Author : Badal Prasad Singh

This app.py is the primary Flask app to parse the Resume and suggest the best job role.
"""

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from score import score_resume, extract_text_from_pdf
import os
from flask_cors import CORS
from rankings import result
from Database.users import users_bp
from Database.employers import employers_bp
from Database.jobseekers import jobseekers_bp
from Database.applications import applications_bp
from Database.current_job_openings import current_job_openings_bp
from Database.fact_table import fact_table_bp
from Database.applicants_rating_data import applicants_rating_data_bp
from Database.companies import companies_bp

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

app.register_blueprint(users_bp)
app.register_blueprint(employers_bp)
app.register_blueprint(jobseekers_bp)
app.register_blueprint(applications_bp)
app.register_blueprint(current_job_openings_bp)
app.register_blueprint(fact_table_bp)
app.register_blueprint(applicants_rating_data_bp)
app.register_blueprint(companies_bp)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        score = score_resume(file_path)
        parse = extract_text_from_pdf(file_path)
        return jsonify({"score": score, "parse":parse})
    else:
        return jsonify({"error": "Invalid file format"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get the port from the environment variable
    app.run(host='0.0.0.0', port=port, debug=True)

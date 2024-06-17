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

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

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
    app.run(debug=True)



# """
# Author : Badal Prasad Singh
#
# This app.py is the primary Flask app to parse the Resume and suggest the best job role
# """
#
#
# from flask import Flask, render_template, request, redirect, url_for
# from werkzeug.utils import secure_filename
# from score import score_resume, extract_text_from_pdf
# from rankings import result
# import os
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = './uploads'
# app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
#
# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'resume' not in request.files:
#         return redirect(request.url)
#     file = request.files['resume']
#     if file.filename == '':
#         return redirect(request.url)
#
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         score = result(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         # score = score_resume(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         return f'Score : {score}'
#     else:
#         return 'Invalid'
#
# if __name__=='__main__':
#     port = int(os.environ.get('PORT', 5000))  # Get the port from the environment variable
#     app.run(host='0.0.0.0', port=port, debug=True)
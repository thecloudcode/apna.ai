"""
Author : Akshaya & Yashwanth
Contributor : Badal Prasad Singh

This is a Flask API to add, delete, update and get data from Supabase Database of tables : Applications_Rating_Data and Current_Job_Openings
"""

from flask import Flask, request, jsonify
from supabase import create_client, Client
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

"""
Example Postman

URL : http://127.0.0.1:5000/add_data_to_applicants_rating_data
Method : POST
Body (JSON)
{
    "Id": "103",
    "Name": "Data Engineer"
}
"""
@app.route('/add_data_to_applicants_rating_data', methods=['POST'])
def add_data_to_applicants_rating_data():
    data = request.json
    try:
        response = supabase.table('Applicants_Rating_Data').insert(data).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example Postman 

URL : http://127.0.0.1:5000/delete_data_from_applicants_rating_data/103
Method : DELETE
"""
@app.route('/delete_data_from_applicants_rating_data/<int:id>', methods=['DELETE'])
def delete_data_from_applicants_rating_data(id):
    try:
        response = supabase.table('Applicants_Rating_Data').delete().eq('Id', id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example POSTMAN

URL : http://127.0.0.1:5000/update_data_from_applicants_rating_data/104
METHOD : PUT
BODY(JSON):
{
  "Name": "Jane Doe"
}
"""
@app.route('/update_data_from_applicants_rating_data/<int:id>', methods=['PUT'])
def update_data_from_applicants_rating_data(id):
    data = request.json
    try:
        response = supabase.table('Applicants_Rating_Data').update(data).eq('Id', id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example POSTMAN

URL : http://127.0.0.1:5000/get_data_from_applicants_rating_data
METHOD : GET
"""
@app.route('/get_data_from_applicants_rating_data', methods=['GET'])
def get_data_from_applicants_rating_data():
    try:
        response = supabase.table('Applicants_Rating_Data').select('*').execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example Postman

URL : http://127.0.0.1:5000/add_data_to_current_job_openings
Method : POST
Body (JSON)
{
    "Job_id": "118"
}
"""
@app.route('/add_data_to_current_job_openings', methods=['POST'])
def add_data_to_current_job_openings():
    data = request.json
    try:
        response = supabase.table('Current_Job_Openings').insert(data).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example Postman 

URL : http://127.0.0.1:5000/delete_data_from_current_job_openings/118
Method : DELETE
"""
@app.route('/delete_data_from_current_job_openings/<int:id>', methods=['DELETE'])
def delete_data_from_current_job_openings(id):
    try:
        response = supabase.table('Current_Job_Openings').delete().eq('Job_id', id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example POSTMAN

URL : http://127.0.0.1:5000/update_data_from_current_job_openings/118
METHOD : PUT
BODY(JSON):
{
    "Company": "belikebadal"
}
"""
@app.route('/update_data_from_current_job_openings/<int:id>', methods=['PUT'])
def update_data_from_current_job_openings(id):
    data = request.json
    try:
        response = supabase.table('Current_Job_Openings').update(data).eq('Job_id', id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

"""
Example POSTMAN

URL : http://127.0.0.1:5000/get_data_from_current_job_openings
METHOD : GET
"""
@app.route('/get_data_from_current_job_openings', methods=['GET'])
def get_data_from_current_job_openings():
    try:
        response = supabase.table('Current_Job_Openings').select('*').execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

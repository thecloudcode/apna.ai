from flask import Blueprint, request, jsonify
from Database import supabase

current_job_openings_bp = Blueprint('current_job_openings', __name__)

@current_job_openings_bp.route('/current_job_openings', methods=['POST'])
def add_current_job_opening():
    data = request.json
    response = supabase.table('Current_Job_Openings').insert(data).execute()
    return jsonify(response.data)

@current_job_openings_bp.route('/current_job_openings/<int:job_id>', methods=['DELETE'])
def delete_current_job_opening(job_id):
    response = supabase.table('Current_Job_Openings').delete().eq('Job_id', job_id).execute()
    return jsonify(response.data)

@current_job_openings_bp.route('/current_job_openings/<int:job_id>', methods=['PUT'])
def update_current_job_opening(job_id):
    data = request.json
    response = supabase.table('Current_Job_Openings').update(data).eq('Job_id', job_id).execute()
    return jsonify(response.data)

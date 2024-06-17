"""

"""
from flask import Blueprint, request, jsonify
from Database import supabase

jobseekers_bp = Blueprint('jobseekers', __name__)

@jobseekers_bp.route('/jobseekers', methods=['POST'])
def add_jobseeker():
    data = request.json
    response = supabase.table('Jobseekers').insert(data).execute()
    return jsonify(response.data)

@jobseekers_bp.route('/jobseekers/<int:jobseeker_id>', methods=['DELETE'])
def delete_jobseeker(jobseeker_id):
    response = supabase.table('Jobseekers').delete().eq('jobseeker_id', jobseeker_id).execute()
    return jsonify(response.data)

@jobseekers_bp.route('/jobseekers/<int:jobseeker_id>', methods=['PUT'])
def update_jobseeker(jobseeker_id):
    data = request.json
    response = supabase.table('Jobseekers').update(data).eq('jobseeker_id', jobseeker_id).execute()
    return jsonify(response.data)

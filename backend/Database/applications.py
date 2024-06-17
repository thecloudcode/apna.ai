from flask import Blueprint, request, jsonify
from Database import supabase

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/applications', methods=['POST'])
def add_application():
    data = request.json
    response = supabase.table('Applications').insert(data).execute()
    return jsonify(response.data)

@applications_bp.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    response = supabase.table('Applications').delete().eq('application_id', application_id).execute()
    return jsonify(response.data)

@applications_bp.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    data = request.json
    response = supabase.table('Applications').update(data).eq('application_id', application_id).execute()
    return jsonify(response.data)

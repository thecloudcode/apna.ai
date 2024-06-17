from flask import Blueprint, request, jsonify
from Database import supabase

applicants_rating_data_bp = Blueprint('applicants_rating_data', __name__)

@applicants_rating_data_bp.route('/applicants_rating_data', methods=['POST'])
def add_applicant_rating():
    data = request.json
    response = supabase.table('Applicants_Rating_Data').insert(data).execute()
    return jsonify(response.data)

@applicants_rating_data_bp.route('/applicants_rating_data/<int:id>', methods=['DELETE'])
def delete_applicant_rating(id):
    response = supabase.table('Applicants_Rating_Data').delete().eq('Id', id).execute()
    return jsonify(response.data)

@applicants_rating_data_bp.route('/applicants_rating_data/<int:id>', methods=['PUT'])
def update_applicant_rating(id):
    data = request.json
    response = supabase.table('Applicants_Rating_Data').update(data).eq('Id', id).execute()
    return jsonify(response.data)

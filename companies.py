from flask import Blueprint, request, jsonify
from Database import supabase

companies_bp = Blueprint('companies', __name__)

def get_companies():
    # Fetch all user data from the 'Users' table in Supabase
    response = supabase.table('Companies').select('*').execute()
    if response.data:
        return jsonify(response.data), 200  # Return the data if successful
    else:
        return jsonify({"error": "No users found"}), 404

@companies_bp.route('/getcompanies', methods=['GET'])
def get_users():
    # Fetch all user data from the 'Users' table in Supabase
    response = supabase.table('Companies').select('*').execute()
    if response.data:
        return jsonify(response.data), 200  # Return the data if successful
    else:
        return jsonify({"error": "No users found"}), 404

@companies_bp.route('/addcompany', methods=['POST'])
def add_user():
    data = request.json
    response = supabase.table('Companies').insert(data).execute()
    return jsonify(response.data)

@companies_bp.route('/detelecompany/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = supabase.table('Companies').delete().eq('company_id', user_id).execute()
    return jsonify(response.data)

@companies_bp.route('/updatecompany/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    response = supabase.table('Companies').update(data).eq('company_id', user_id).execute()
    return jsonify(response.data)

"""
CREATE TABLE Users (
    User_id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone_Number VARCHAR(15),
    User_Type VARCHAR(50) NOT NULL CHECK (User_Type IN ('Employer', 'Jobseeker'))
);
"""

from flask import Blueprint, request, jsonify
from Database import supabase

users_bp = Blueprint('users', __name__)

@users_bp.route('/getusers', methods=['GET'])
def get_users():
    # Fetch all user data from the 'Users' table in Supabase
    response = supabase.table('Users').select('*').execute()
    if response.data:
        return jsonify(response.data), 200  # Return the data if successful
    else:
        return jsonify({"error": "No users found"}), 404

@users_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    response = supabase.table('Users').insert(data).execute()
    return jsonify(response.data)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    response = supabase.table('Users').delete().eq('user_id', user_id).execute()
    return jsonify(response.data)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    response = supabase.table('Users').update(data).eq('user_id', user_id).execute()
    return jsonify(response.data)

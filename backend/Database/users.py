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

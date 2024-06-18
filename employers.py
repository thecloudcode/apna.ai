"""
CREATE TABLE Employers (
    Employer_id SERIAL PRIMARY KEY,
    User_id INT NOT NULL,
    Company_Name VARCHAR(100) NOT NULL,
    FOREIGN KEY (User_id) REFERENCES Users(User_id) ON DELETE CASCADE
);
"""
from flask import Blueprint, request, jsonify
from Database import supabase

employers_bp = Blueprint('employers', __name__)

@employers_bp.route('/employers', methods=['POST'])
def add_employer():
    data = request.json
    response = supabase.table('Employers').insert(data).execute()
    return jsonify(response.data)

@employers_bp.route('/employers/<int:employer_id>', methods=['DELETE'])
def delete_employer(employer_id):
    response = supabase.table('Employers').delete().eq('employer_id', employer_id).execute()
    return jsonify(response.data)

@employers_bp.route('/employers/<int:employer_id>', methods=['PUT'])
def update_employer(employer_id):
    data = request.json
    response = supabase.table('Employers').update(data).eq('employer_id', employer_id).execute()
    return jsonify(response.data)

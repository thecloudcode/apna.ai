from flask import Blueprint, request, jsonify
from Database import supabase

fact_table_bp = Blueprint('fact_table', __name__)

@fact_table_bp.route('/fact_table', methods=['POST'])
def add_fact():
    data = request.json
    response = supabase.table('Fact_Table').insert(data).execute()
    return jsonify(response.data)

@fact_table_bp.route('/fact_table/<int:fact_id>', methods=['DELETE'])
def delete_fact(fact_id):
    response = supabase.table('Fact_Table').delete().eq('fact_id', fact_id).execute()
    return jsonify(response.data)

@fact_table_bp.route('/fact_table/<int:fact_id>', methods=['PUT'])
def update_fact(fact_id):
    data = request.json
    response = supabase.table('Fact_Table').update(data).eq('fact_id', fact_id).execute()
    return jsonify(response.data)

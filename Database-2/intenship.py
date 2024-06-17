import logging
from flask import Flask, Blueprint, request, jsonify
from supabase import create_client, Client

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level as needed

app = Flask(__name__)

# Define Supabase configuration
SUPABASE_URL = "https://maogxyhapksyshaleqie.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1hb2d4eWhhcGtzeXNoYWxlcWllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgxMjU4ODYsImV4cCI6MjAzMzcwMTg4Nn0.yObHYXoTXGgz5WcLpacUT21LbCBRpv8q7uprLf8eE48"

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Blueprint for internships
internships_bp = Blueprint('internships', __name__)

@internships_bp.route('/internships', methods=['POST'])
def add_internship():
    try:
        data = request.json
        logging.debug(f"Received POST request data: {data}")
        response = supabase.table('internships').insert(data).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@internships_bp.route('/internships/<int:internship_id>', methods=['DELETE'])
def delete_internship(internship_id):
    try:
        logging.debug(f"Deleting internship_id: {internship_id}")
        response = supabase.table('internships').delete().eq('internship_id', internship_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@internships_bp.route('/internships/<int:internship_id>', methods=['PUT'])
def update_internship(internship_id):
    try:
        data = request.json
        logging.debug(f"Updating internship_id {internship_id} with data: {data}")
        response = supabase.table('internships').update(data).eq('internship_id', internship_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Register the blueprint
app.register_blueprint(internships_bp)

if __name__ == '__main__':
    app.run(debug=True)

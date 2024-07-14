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

# Blueprint for activity scorer
activity_scorer_bp = Blueprint('activity_scorer', __name__)

@activity_scorer_bp.route('/activity_scorer', methods=['POST'])
def add_activity_scorer():
    try:
        data = request.json
        logging.debug(f"Received POST request data: {data}")
        response = supabase.table('Activity_Scorer').insert(data).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@activity_scorer_bp.route('/activity_scorer/<int:user_id>', methods=['DELETE'])
def delete_activity_scorer(user_id):
    try:
        logging.debug(f"Deleting user_id: {user_id}")
        response = supabase.table('Activity_Scorer').delete().eq('user_id', user_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@activity_scorer_bp.route('/activity_scorer/<int:user_id>', methods=['PUT'])
def update_activity_scorer(user_id):
    try:
        data = request.json
        logging.debug(f"Updating user_id {user_id} with data: {data}")
        response = supabase.table('Activity_Scorer').update(data).eq('user_id', user_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
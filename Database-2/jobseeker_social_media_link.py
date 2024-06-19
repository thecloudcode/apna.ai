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

# Blueprint for jobseeker_social_media_links
jobseeker_social_media_links_bp = Blueprint('jobseeker_social_media_links', __name__)

@jobseeker_social_media_links_bp.route('/jobseeker_social_media_links', methods=['POST'])
def add_jobseeker_social_media_links():
    try:
        data = request.json
        logging.debug(f"Received POST request data: {data}")
        response = supabase.table('jobseeker_social_media_links').insert(data).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@jobseeker_social_media_links_bp.route('/jobseeker_social_media_links/<int:jobseeker_id>', methods=['DELETE'])
def delete_jobseeker_social_media_links(jobseeker_id):
    try:
        logging.debug(f"Deleting jobseeker_id: {jobseeker_id}")
        response = supabase.table('jobseeker_social_media_links').delete().eq('jobseeker_id', jobseeker_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@jobseeker_social_media_links_bp.route('/jobseeker_social_media_links/<int:jobseeker_id>', methods=['PUT'])
def update_jobseeker_social_media_links(jobseeker_id):
    try:
        data = request.json
        logging.debug(f"Updating jobseeker_id {jobseeker_id} with data: {data}")
        response = supabase.table('jobseeker_social_media_links').update(data).eq('jobseeker_id', jobseeker_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Register the blueprint
app.register_blueprint(jobseeker_social_media_links_bp)

if __name__ == '__main__':
    app.run(debug=True)

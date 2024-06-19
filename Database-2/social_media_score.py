import logging
from flask import Flask, Blueprint, request, jsonify
from supabase import create_client

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level as needed

app = Flask(__name__)

# Define Supabase configuration
SUPABASE_URL = "https://maogxyhapksyshaleqie.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1hb2d4eWhhcGtzeXNoYWxlcWllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgxMjU4ODYsImV4cCI6MjAzMzcwMTg4Nn0.yObHYXoTXGgz5WcLpacUT21LbCBRpv8q7uprLf8eE48"

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Blueprint for social_media_score
social_media_score_bp = Blueprint('social_media_score', __name__)

@social_media_score_bp.route('/social_media_score', methods=['POST'])
def add_social_media_score():
    try:
        data = request.json
        logging.debug(f"Received POST request data: {data}")
        response = supabase.table('social_media_score').insert(data).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@social_media_score_bp.route('/social_media_score/<int:jobseeker_id>', methods=['DELETE'])
def delete_social_media_score(jobseeker_id):
    try:
        logging.debug(f"Deleting social media score for jobseeker_id: {jobseeker_id}")
        response = supabase.table('social_media_score').delete().eq('jobseeker_id', jobseeker_id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Register the blueprint
app.register_blueprint(social_media_score_bp)

if __name__ == '__main__':
    app.run(debug=True)

import logging
from flask import Flask, Blueprint, request, jsonify
from supabase import create_client, Client

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level as needed

app = Flask(_name_)

# Define Supabase configuration
SUPABASE_URL = "https://maogxyhapksyshaleqie.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1hb2d4eWhhcGtzeXNoYWxlcWllIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTgxMjU4ODYsImV4cCI6MjAzMzcwMTg4Nn0.yObHYXoTXGgz5WcLpacUT21LbCBRpv8q7uprLf8eE48"

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Blueprint for chatbot_prompts
chatbot_prompts_bp = Blueprint('chatbot_prompts', _name_)

@chatbot_prompts_bp.route('/chatbot_prompts', methods=['POST'])
def add_chatbot_prompt():
    try:
        data = request.json
        logging.debug(f"Received POST request data: {data}")
        response = supabase.table('chatbot_prompts').insert(data).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@chatbot_prompts_bp.route('/chatbot_prompts/<int:id>', methods=['DELETE'])
def delete_chatbot_prompt(id):
    try:
        logging.debug(f"Deleting id: {id}")
        response = supabase.table('chatbot_prompts').delete().eq('id', id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@chatbot_prompts_bp.route('/chatbot_prompts/<int:id>', methods=['PUT'])
def update_chatbot_prompt(id):
    try:
        data = request.json
        logging.debug(f"Updating id {id} with data: {data}")
        response = supabase.table('chatbot_prompts').update(data).eq('id', id).execute()
        logging.debug(f"Supabase response: {response}")
        return jsonify(response.data)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

# Register the blueprint
app.register_blueprint(chatbot_prompts_bp)

if _name_ == '_main_':
    app.run(debug=True)
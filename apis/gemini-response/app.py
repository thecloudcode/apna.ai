"""
Author : Keerthi
Contributor : Badal Prasad Singh

This API takes in a prompt and returns the Gemini API response for it
"""

from flask import Flask, request, jsonify
import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

load_dotenv()

configure(api_key=os.getenv("GOOGLE_API_KEY"))
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}

app = Flask(__name__)
model = GenerativeModel("gemini-pro", generation_config=generation_config)

"""
Example POSTMAN

URL : http://localhost:5000/generate
METHOD : POST
{
    "prompt": "How are you?"
}
"""
@app.route("/generate", methods=["POST"])
def generate_response():
    prompt = request.json.get("prompt")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = model.generate_content([prompt])
    return jsonify({"response": response.text})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
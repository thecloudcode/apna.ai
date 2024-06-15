

from flask import Flask, request, jsonify
import os
import logging
from google.generativeai import configure, GenerativeModel


GOOGLE_API_KEY = "AIzaSyDxN6nbUdLn5_1nXaZa2d5LZG03L_r3PGI"


logging.basicConfig(level=logging.DEBUG)


if not GOOGLE_API_KEY:
    logging.error("GOOGLE_API_KEY is not set.")
else:
    logging.info(f"GOOGLE_API_KEY is set: {GOOGLE_API_KEY}")


configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

app = Flask(__name__)
model = GenerativeModel("gemini-pro", generation_config=generation_config)

@app.route("/generate", methods=["POST"])
def generate_response():
    try:
        prompt = request.json.get("prompt")
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        logging.debug(f"Received prompt: {prompt}")

        # Generate the response
        response = model.generate_content([prompt])
        logging.debug(f"Generated response: {response}")

        return jsonify({"response": response.text})

    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return jsonify({"error": "An error occurred while generating the response."}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logging.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)

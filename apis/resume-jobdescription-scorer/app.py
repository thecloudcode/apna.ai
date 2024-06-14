"""
Author : Bindu Vamsi
Contributor : Badal Prasad Singh

This API uses Natural Langauge Processing to check the similarity between two major strings. Inside the project, it is going to be used as Resume and Job Description Similarity Checker
"""

from flask import Flask, request, jsonify
import spacy

nlp = spacy.load("en_core_web_md")

app = Flask(__name__)

@app.route('/similarity', methods=['POST'])
def similarity():
    """
    Endpoint to compute similarity score between two strings.

    Expected JSON Format:
    {
        "string1":"First string for comparison",
        "string2":"Second string for comparison"
    }
    """
    data = request.json

    if 'string1' not in data or 'string2' not in data:
        return jsonify({'error': 'Both string1 and string2 must be provided'}), 400

    string1 = data['string1']
    string2 = data['string2']

    try:
        w1 = nlp(string1)
        w2 = nlp(string2)
    except Exception as e:
        return jsonify({"error: Error processing input strings"}), 500

    try:
        similarity_score = w1.similarity(w2)
    except Exception as e:
        return jsonify({"Error":"Error computing similarity score"}),500

    return jsonify({'similarity': similarity_score})

if __name__ == '__main__':
    app.run(debug=True)

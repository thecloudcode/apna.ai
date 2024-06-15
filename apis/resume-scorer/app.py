"""
Author : Badal Prasad Singh
Tech Stack : Python, Flask, Supabase
Deployed on : www.render.com

This API fetches all the applicants Resume scores for the all job applications, and provides you with rank of your Resume among them
"""

import os
from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

class SupabaseClient:
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.client = create_client(self.url, self.key)

    def fetch_data(self, table: str, columns: list):
        response = self.client.table(table).select(*columns).execute()
        if response.data is None:
            logging.error("Error fetching data from Supabase")
            return None, "Error fetching data"
        return response.data, None

class RankService:
    def __init__(self, supabase_client: SupabaseClient):
        self.supabase_client = supabase_client

    def fetch_and_sort_all_data(self, columns: list):
        data, error = self.supabase_client.fetch_data("Applicants_Rating_Data", columns)
        if error:
            return None, error

        sorted_scores = {column: [] for column in columns}
        for item in data:
            for column in columns:
                if column in item and item[column] is not None:
                    sorted_scores[column].append(item[column])

        for column in columns:
            sorted_scores[column].sort()

        return sorted_scores, None

    def find_rank(self, scores: list, score: float):
        for i, s in enumerate(scores):
            if score <= s:
                return len(scores) - i + 1
        return 1

    def calculate_ranks(self, score: float):
        columns = [str(i) for i in range(101, 118)]
        sorted_scores, error = self.fetch_and_sort_all_data(columns)
        if error:
            return None, error

        ranks = {}
        for column in columns:
            rank = self.find_rank(sorted_scores[column], score)
            ranks[column] = rank

        return ranks, None

app = Flask(__name__)
supabase_client = SupabaseClient()
rank_service = RankService(supabase_client)

@app.route('/rank', methods=['POST'])
def rank_resume():
    data = request.json
    score = data.get('score')

    if score is None:
        return jsonify({"error": "Score is required"}), 400

    ranks, error = rank_service.calculate_ranks(score)
    if error:
        return jsonify({"error": "Error fetching data from Supabase"}), 500

    return jsonify(ranks)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

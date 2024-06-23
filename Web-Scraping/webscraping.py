from flask import Flask, request, jsonify
import os
import logging
import requests
from bs4 import BeautifulSoup
from google.generativeai import configure, GenerativeModel

GOOGLE_API_KEY = "AIzaSyANffUWKYQ7Fk2_nPatFdLMhrXrXcQgyX0"

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

def scrape_github_profile(url):
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching GitHub profile page: {e}")
        raise Exception(f"Failed to retrieve the webpage. Error: {e}")

    try:
        soup = BeautifulSoup(page.text, 'html.parser')

        repos_element = soup.find('span', class_='Counter')
        repos = repos_element.text.strip() if repos_element else 'N/A'

        followers_element = soup.find('a', href=lambda href: href and 'followers' in href)
        followers = followers_element.find('span', class_='text-bold').text.strip() if followers_element else 'N/A'

        contributions_element = soup.find('h2', class_='f4 text-normal mb-2')
        contributions = contributions_element.text.strip().split()[0] if contributions_element else 'N/A'

        return {
            'repositories': repos,
            'followers': followers,
            'contributions': contributions
        }
    except Exception as e:
        logging.error(f"Error parsing GitHub profile data: {e}")
        raise Exception(f"Failed to parse the webpage content. Error: {e}")

def scrape_linkedin_profile(url):
    
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Error fetching LinkedIn profile page: {e}")
        raise Exception(f"Failed to retrieve the webpage. Error: {e}")

    try:
        soup = BeautifulSoup(page.text, 'html.parser')

       
        connections_element = soup.find('span', class_='t-bold')
        connections = connections_element.text.strip() if connections_element else 'N/A'

        activities_element = soup.find('span', class_='t-regular')
        activities = activities_element.text.strip() if activities_element else 'N/A'

        return {
            'connections': connections,
            'activities': activities
        }
    except Exception as e:
        logging.error(f"Error parsing LinkedIn profile data: {e}")
        raise Exception(f"Failed to parse the webpage content. Error: {e}")

def compute_score(profile_data):
    
    score = 0
    if 'repositories' in profile_data and profile_data['repositories'] != 'N/A':
        score += 1
    if 'followers' in profile_data and profile_data['followers'] != 'N/A':
        score += 1
    if 'contributions' in profile_data and profile_data['contributions'] != 'N/A':
        score += 1
    if 'connections' in profile_data and profile_data['connections'] != 'N/A':
        score += 1
    if 'activities' in profile_data and profile_data['activities'] != 'N/A':
        score += 1
    return score

@app.route("/scrap", methods=["POST"])
def generate_response():
    try:
        profile_url = request.json.get("profile_url")
        if not profile_url:
            return jsonify({"error": "No profile URL provided"}), 400

        logging.debug(f"Received profile URL: {profile_url}")

        
        if 'github.com' in profile_url:
            profile_data = scrape_github_profile(profile_url)
        elif 'linkedin.com' in profile_url:
            profile_data = scrape_linkedin_profile(profile_url)
        else:
            return jsonify({"error": "Unsupported profile URL"}), 400

        logging.debug(f"Scraped profile data: {profile_data}")

        
        profile_score = compute_score(profile_data)

        
        prompt = f"Profile analysis: {profile_data}. Profile score: {profile_score}"
        response = model.generate_content([prompt])
        logging.debug(f"Generated response: {response}")

        return jsonify({"response": response.text, "profile_score": profile_score})

    except Exception as e:
        logging.error(f"Error generating response: {e}")
        return jsonify({"error": "An error occurred while generating the response.", "details": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    logging.info(f"Starting server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)

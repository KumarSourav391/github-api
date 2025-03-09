from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the GitHub API Integration!"})

# GitHub API details
GITHUB_API_URL = "https://api.github.com"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Fetch token from .env

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Get user profile data
@app.route('/github', methods=['GET'])
def get_github_profile():
    response = requests.get(f"{GITHUB_API_URL}/user", headers=HEADERS)
    return jsonify(response.json())

# Get repo data
@app.route('/github/<repo_name>', methods=['GET'])
def get_repo(repo_name):
    response = requests.get(f"{GITHUB_API_URL}/repos/KumarSourav391/{repo_name}", headers=HEADERS)
    return jsonify(response.json())

# Create an issue
@app.route('/github/<repo_name>/issues', methods=['POST'])
def create_issue(repo_name):
    data = request.json
    issue_data = {
        "title": data.get("title"),
        "body": data.get("body")
    }
    response = requests.post(f"{GITHUB_API_URL}/repos/KumarSourav391/{repo_name}/issues",
                             headers=HEADERS, json=issue_data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)

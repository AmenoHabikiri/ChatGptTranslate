from flask import Blueprint, jsonify, current_app as app
import requests

main = Blueprint('main', __name__)

@main.route('/models', methods=['GET'])
def get_models():
    url = 'https://api.openai.com/v1/models'
    headers = {
        'Authorization': f'Bearer {app.config["OPENAI_API_KEY"]}',
        'OpenAI-Organization': app.config['OPENAI_ORG_ID'],
    }

    response = requests.get(url, headers=headers)
    return jsonify(response.json())

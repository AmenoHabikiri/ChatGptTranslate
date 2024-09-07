from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
    app.config['OPENAI_ORG_ID'] = os.getenv('OPENAI_ORG_ID')

    from .routes import main
    app.register_blueprint(main)

    return app

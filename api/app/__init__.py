from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app) # Enable CORS for all routes
    from .routes import main
    app.register_blueprint(main)

    return app
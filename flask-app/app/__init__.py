import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Read ENV_TYPE directly from OS environment variable
    app.config['ENV_TYPE'] = os.environ.get("FLASK_ENV", "development")
    
    from .routes import main
    app.register_blueprint(main)

    return app

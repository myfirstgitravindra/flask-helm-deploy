from flask import Blueprint, render_template, current_app

main = Blueprint('main', __name__)

@main.route('/')
def home():
    env_type = current_app.config['ENV_TYPE']
    return render_template('index.html', env=env_type)

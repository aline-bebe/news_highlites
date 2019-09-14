# from flask import Blueprint
# from flask_bootstrap import Bootstrap
# main = Blueprint('main', __name__)
# from . import views,

from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    
    # Initializing application
    app = Flask(__name__)

    #Setting up configuration/Creating the app configurations
    app.config.from_object(config_options[config_name])
    # app.config.from_pyfile('config.py')

    #Initializing Flask Extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)

    # from app import views

    return app
from flask import Flask
from config import config
from .ext import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .proxy import proxy as proxy_blueprint
    app.register_blueprint(proxy_blueprint)

    return app

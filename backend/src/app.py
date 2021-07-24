import os
import pathlib


from flask import Flask

from api import api

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent

# set default settings file.
os.environ.setdefault('FLASK_SETTINGS_FILE', str(PROJECT_ROOT / 'settings/development.py'))


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)

    if config_file:
        # apply settings from config file, if defined.
        app.config.from_pyfile(config_file)

    else:
        # otherwise load settings from environment variable.
        app.config.from_envvar('FLASK_SETTINGS_FILE')

    if settings_override:
        # apply settings override if necessary.
        app.config.update(settings_override)

    # Load app modules.
    api.init_app(app)

    return app

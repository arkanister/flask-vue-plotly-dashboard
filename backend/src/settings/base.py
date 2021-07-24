"""
Settings for project.

For more information on this file, see
https://flask.palletsprojects.com/en/2.0.x/config/
"""
import pathlib
import decouple


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

# Decouple Config
# https://github.com/henriquebastos/python-decouple

config = decouple.AutoConfig(BASE_DIR.parent)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('FLASK_DEBUG', True, cast=bool)


# Disable 404 Help

ERROR_404_HELP = False


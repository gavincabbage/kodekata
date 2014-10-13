# kodekata/__init__.py


__all__ = ["app", "routes", "tests"]


from flask import Flask


app = Flask(__name__)
#app.config.from_pyfile('../config/base_config.py')
#app.config.from_envvar('APP_CONFIG_FILE')


import routes


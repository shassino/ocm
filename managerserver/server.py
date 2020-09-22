from flask import Flask, jsonify
from connexion.resolver import RestyResolver

import connexion
import logging

import settings
import api_user

SWAGGER = ('swagger/', 'swagger.yaml')
swagger = connexion.App(__name__, specification_dir=SWAGGER[0], options={"swagger_ui": False})

app = swagger.app

#load api configuration
swagger.add_api(SWAGGER[1])

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    app.run()
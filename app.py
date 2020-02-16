import os
from flask import Flask, request, Response, abort, jsonify
from flask_cors import CORS # type: ignore[import]
from waitress import serve as executar

PORT = os.getenv('PORT')
HOST = '0.0.0.0'
PRODUCAO = os.getenv('PRODUCAO')
DEBUG_MODE = os.getenv('DEBUG_MODE')

app = Flask(__name__)

# Setup cors headers to allow all domains
# https://flask-cors.readthedocs.io/en/latest/
CORS(app)

if __name__ == "__main__":
    from src.rotas import *

    if PRODUCAO:
        executar(app, host=HOST, port=PORT)
    else:
        app.run(host=HOST, port=PORT)
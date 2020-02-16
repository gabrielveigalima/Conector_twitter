#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime, timezone
from src.modulos import tweet
import json
from flask import Flask, request, Response, abort, jsonify
from app import app

@app.route("/")
def apresentacao(): # pylint: disable=unused-variable
    """ apresentacao da aplicação.
    """
    return Response(json.dumps({"mensagem": 'CONECTOR TWITTER REST API', "timestamp": datetime.now(timezone.utc)}), mimetype="application/json")


@app.route("/tweets/<string:palavra>")
def tweets(palavra):  # pylint: disable=unused-variable
    """ apresentacao da aplicação.
    """



    localizacao = "-22.785275,-43.4046764,30km"

    return Response(json.dumps(tweet.Tweet().buscar_tweets(palavra, localizacao)), mimetype="application/json")


@app.route('/health')
def Health():
    return Response(json.dumps({"mensagem": 'CONECTOR TWITTER REST API', "timestamp": datetime.now(timezone.utc)}), mimetype="application/json")


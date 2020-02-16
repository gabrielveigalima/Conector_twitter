#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.conexao import conexao_twitter

class Tweet:
    def buscar_tweets(self,palavra='morrer', localizacao="-22.785275,-43.4046764,30km"):
        resultado_tweets = conexao_twitter.ConexaoTwitter().buscar_tweets(palavra,localizacao)

        if resultado_tweets is None:
            return {"resultado": 0}

        tweets = []
        for tweet in resultado_tweets:
            tweets.append({"usuario": tweet.user.screen_name, "tweet": tweet.text})

        return tweets
import tweepy
import os

class ConexaoTwitter:

    def __init__(self):
        # Adicione aqui sua Consumer Key
        self.__consumer_key = os.getenv('CONSUMER_KEY')

        # Adicione aqui sua Consumer Secret
        self.__consumer_secret = os.getenv('CONSUMER_SECRET')

        # Adicione aqui seu Access Token
        self.__access_token = os.getenv('ACCESS_TOKEN')

        # Adicione aqui seu Access Token Secret
        self.__access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    def conectar(self):

        try:
            __authentication = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
            __authentication.set_access_token(self.__access_token, self.__access_token_secret)

            return tweepy.API(__authentication)
        except tweepy.TweepError as erro:
            Exception({"erro": f"falha ao conectar com twitter{erro}"})
            return None

    def buscar_tweets(self, palavra = 'morrer', localizacao = "-22.785275,-43.4046764,30km"):
        twitter = self.conectar()
        return twitter.search(q=palavra, geocode=localizacao)
import tweepy
import os

# Adicione aqui sua Consumer Key
consumer_key = os.getenv('CONSUMER_KEY')

# Adicione aqui sua Consumer Secret
consumer_secret = os.getenv('CONSUMER_SECRET')

# Adicione aqui seu Access Token
access_token = os.getenv('ACCESS_TOKEN')

# Adicione aqui seu Access Token Secret
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(authentication)

tweets = twitter.search(q='morrer', geocode = "-22.785275,-43.4046764,30km")

for tweet in tweets:
     print(f'UsuÃ¡rio: {tweet.user.screen_name} - Tweet: {tweet.text}')
from src.modulos import tweet

tweets = tweet.Tweet().buscar_tweets('morrer', "-22.785275,-43.4046764,30km")

for tweet in tweets:
     print(f'UsuÃ¡rio: {tweet.user.screen_name} - Tweet: {tweet.text}')
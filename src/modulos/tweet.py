from src.conexao import conexao_twitter



class Tweet:
    def buscar_tweets(self,palavra, localizacao):
        twitter = conexao_twitter.ConexaoTwitter().conectar()
        return twitter.search(q=palavra, geocode=localizacao)

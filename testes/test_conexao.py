import os
import sys
import pytest

from src.conexao import conexao_twitter


MODULE_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(MODULE_DIR, '../..'))

def test_conexao_com_twitter_nao_deve_retornar_none():
    assert conexao_twitter.ConexaoTwitter().conectar() != None

def test_varivais_de_ambiente_para_conectar_ao_twitter():
    assert os.getenv('CONSUMER_KEY') != None
    assert os.getenv('CONSUMER_SECRET') != None
    assert os.getenv('ACCESS_TOKEN') != None
    assert os.getenv('ACCESS_TOKEN_SECRET') != None
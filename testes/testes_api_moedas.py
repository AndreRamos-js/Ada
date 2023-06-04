from requests import get
import json



requisicao = get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()
nome = cotacao['USD']['name']
data = cotacao['USD']['create_date']
valor = cotacao['USD']['bid']
mensagem = f'Cotação do {nome} em {data} é {valor} reais.'

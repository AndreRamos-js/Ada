import requests
from requests.structures import CaseInsensitiveDict
import json



url ='https://api.api-futebol.com.br/v1/campeonatos/10/tabela'

headers = CaseInsensitiveDict()
headers['Accept'] = 'application/json'
headers['Authorization'] = 'Bearer live_6bb50dbeb75a454dc38b14a1c1a13b'

response = requests.get(url, headers=headers)
classificacao = json.loads(response.text)

for g6 in classificacao[:5]:
    print(g6['time']['nome_popular'])

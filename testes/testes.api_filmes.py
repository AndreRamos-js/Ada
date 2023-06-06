import urllib.request, json



url = 'https://api.themoviedb.org/4/discover/movie?sort_by=popularity.desc&api_key=d0d65ac8842befae9b0115007936b366'
resposta = urllib.request.urlopen(url)
dados = resposta.read()
jsondata = json.loads(dados)
filmes = jsondata['results']

for filme in filmes[:5]:
    print(filme['title'])

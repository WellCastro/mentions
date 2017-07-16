# API:
API para consulta de Tweets.

  
# Tecnologias utilizadas

- [Python2.7](https://www.python.org)
Python foi escolhido xxx
- [Bottle](https://bottlepy.org/docs/dev/)
Por ser simples, rápido e um poderoso micro-framework Python, ótimo para atender a demanda do teste.
- [Docker] (https://www.docker.com/)
Escolhido para facilitar a implatanção, poupando instalações e documentos explicativos.


# Exemplos GET

Most Relevants:
Url: /most_mentions/<id>

curl -GET http://localhost:8001/most_mentions/42

Most Mentions:
Url: /most_relevants/<id>

** Optei por informar um ID na chamada para sempre atender a demanda sem a necessidade de correções no código, supondo que nem
sempre o user da LocaWeb seja o 42 ou que a mesma aplicação seja usada para algum outro user ou produto da empresa.


# Executando a API:
Para executar a aplicação basta seguir os seguintes comandos do Docker-Compose

```
cd mentions
```
```
docker-compose build
```
```
docker-compose up -d
```

# Tests
```
docker-compose run web python execute_tests.py
```

# API em produção:
A aplicação também está sendo executada em um ambiente de "produção".
<a href="http://198.199.65.250:8001/most_mentions/42">URL Produção</a>

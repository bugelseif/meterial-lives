"""
API Cats fornece imagens de gatinhos com informações básicas de forma aberta e completas utilizando a chave da API.
https://thecatapi.com/
"""

import json

import requests

from chaves import key

# Rota images/search
response = requests.get("https://api.thecatapi.com/v1/images/search")
# response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit=2&breed_ids=beng&api_key={key}")

# Formata a resposta JSON para visualizar melhor
formatted_response = json.dumps(response.json(), indent=4)
print(formatted_response)


"""
Parâmetros:
    limit	        1-100	Número de imagens a serem retornadas entre	1
    page	        0-n	O número da página a ser usada ao paginar pelas imagens	0
    order	        ASC/DESC/RAND	A ordem para retornar as imagens pela data de upload. RAND = aleatório	RAND
    has_breeds	    1 ou 0	Retornar apenas imagens que possuem informações de raça	0
    breed_ids	    String delimitada por vírgulas	Os IDs das raças para filtrar as imagens. e.g. ?breed_ids=beng,abys	none
    category_ids	String delimitada por vírgulas	Os IDs das categorias para filtrar as imagens. e.g. ?breed_ids=1,5,14	none
    sub_id	        String	Filtrar imagens que possuem o valor sub_id que você usou ao enviá-las	none
"""

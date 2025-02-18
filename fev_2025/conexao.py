"""
API de cotação de moeda
https://exchangeratesapi.io/
"""

import requests
from log import logger


def consulta(*moedas):
    logger.info("Consultando dados de cambio")

    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    response = requests.get(url)
    dados = response.json()
    dados_formatado = {
        'data': dados["date"],
        }

    for moeda in moedas:
        taxa = dados["rates"][moeda]
        dados_formatado[str(moeda)] = {}
        dados_formatado[str(moeda)]['taxa'] = taxa

    logger.info("Retornando dados encontrados")

    return(dados_formatado)


if '__name__' == '__main__':
    consulta()

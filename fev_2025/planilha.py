"""
Usa pandas para manipular uma planilha
"""

import pandas as pd
from conexao import consulta
from log import logger


def salva_dados():
    logger.info("Iniciando a execução do script.")

    retorno = consulta('USD', 'EUR')

    logger.info("Iniciando processo de gravar dados em planilha")


    dados = pd.read_excel('cotacao.xlsx')

    novos_dados = []
    data_referencia = retorno["data"]

    for moeda, taxa in retorno.items():
        if moeda != "data":
            novos_dados.append({"Data": data_referencia, "Moeda": moeda, "Taxa": taxa["taxa"]})

    df_novos_dados = pd.DataFrame(novos_dados)

    dados = pd.concat([dados, df_novos_dados], ignore_index=True)

    dados.to_excel('cotacao.xlsx', index=False)

    logger.info("Tarefa finalizada")



salva_dados()

if '__name__' == '__main__':
    salva_dados()

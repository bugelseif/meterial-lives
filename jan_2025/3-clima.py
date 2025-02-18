"""
API wttr.in fornece informações climaticas de diversas formas.
https://github.com/chubin/wttr.in
"""

import requests


cidade = "São Paulo"
response = requests.get(f"https://wttr.in/{cidade}")
# response = requests.get(f"https://wttr.in/{cidade}?lang=pt&format=%c+%C+%t")

print(response.text)


"""
Parâmetros:
    lang=Idioma
    format=%
    c    Condição do tempo
    C    Nome textual da condição do tempo
    x    Condição do tempo símbolo em texto simples
    h    Umidade
    t    Temperatura (Atual)
    f    Temperatura (Sensação Térmica)
    w    Vento
    l    Localização
    m    Fase da Lua 🌑🌒🌓🌔🌕🌖🌗🌘
    M    Dia da Lua
    p    Precipitação (mm/3 horas)
    P    Pressão (hPa)
    u    Índice UV (1-12)

    D    Alvorada*
    S    Nascer do Sol*
    z    Zênite*
    s    Pôr do Sol*
    d    Crepúsculo*
    T    Hora atual*
    Z    Fuso horário local
"""

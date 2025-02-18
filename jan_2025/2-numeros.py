"""
NumbersAPI fornece rotas para curiosidades sobre numeros, anos, datas, etc.
http://numbersapi.com/
"""

import requests


numero = 5

# Rota /{numero}
response = requests.get(f"http://numbersapi.com/{numero}")
# response = requests.get(f"http://numbersapi.com/random/date")
# response = requests.get(f"http://numbersapi.com/random/year")

print(response.text)

"""
random/
    trivia
    year
    date
    math
"""

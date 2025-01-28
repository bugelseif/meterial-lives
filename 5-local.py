"""
API utilizada no exemplo pode ser executada localmente através desse repositório: https://github.com/bugelseif/app-ensino/tree/main/backend
Documentação local: http://127.0.0.1:8000/docs#/
"""

import requests

dados = {
    "name": "str",
    "email": "str",
    "point": 0,
    "password": "str"
    }

response = requests.get("http://127.0.0.1:8000/users")
# response = requests.post("http://127.0.0.1:8000/users", json=dados)
# response = requests.put("http://127.0.0.1:8000/users/2/point", json=dados)
# response = requests.delete("http://127.0.0.1:8000/users/1")


print(response.text)

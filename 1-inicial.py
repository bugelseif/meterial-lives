"""
A biblioteca requests permite enviar solicitações HTTP/1.1 com métodos como GET, POST, PUT, DELETE, etc.
https://requests.readthedocs.io/en/latest/
"""

import requests

response = requests.get("rotas/ação")
response.text

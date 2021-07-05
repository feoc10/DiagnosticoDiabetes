import requests as requests

my_data = {'colesterol_ruim': 193, 'glucose': 400, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'imc': 22.5,
           'pressão_sistolica': 118, 'pressão_diastolica': 70, 'cintura': 32}
res = requests.get('http://127.0.0.1:5000/xgboost', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 77, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'imc': 22.5,
           'pressão_sistolica': 118, 'pressão_diastolica': 70, 'cintura': 32}
res = requests.get('http://127.0.0.1:5000/xgboost', json=my_data)
print(res.json())


my_data = {'colesterol_ruim': 193, 'glucose': 400, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'imc': 22.5,
           'pressão_sistolica': 118, 'pressão_diastolica': 70, 'cintura': 32}
res = requests.get('http://127.0.0.1:5000/rdf', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 77, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'imc': 22.5,
           'pressão_sistolica': 118, 'pressão_diastolica': 70, 'cintura': 32}
res = requests.get('http://127.0.0.1:5000/rdf', json=my_data)
print(res.json())

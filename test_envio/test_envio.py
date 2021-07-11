import requests as requests

my_data = {'colesterol_ruim': 193, 'glucose': 400, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'altura': 1.55,
            'pressao_arterial': '118x70', 'cintura': 81.28}
res = requests.post('http://127.0.0.1:5000/xgboost', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 77, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'altura': 1.55,
           'pressao_arterial': '118X70', 'cintura': 81.28}
res = requests.post('http://127.0.0.1:5000/xgboost', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 77}
res = requests.post('http://127.0.0.1:5000/xgboost', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 400, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'altura': 1.55,
            'pressao_arterial': '118x70', 'cintura': 81.28}
res = requests.post('http://127.0.0.1:5000/rdf', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 77, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'altura': 1.55,
            'pressao_arterial': '118x70', 'cintura': 81.28}
res = requests.post('http://127.0.0.1:5000/rdf', json=my_data)
print(res.json())

my_data = {'colesterol_ruim': 193, 'glucose': 77}
res = requests.post('http://127.0.0.1:5000/rdf', json=my_data)
print(res.json())

res = requests.get('http://127.0.0.1:5000/modelos')
print(res.json())

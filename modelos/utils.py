"""Funções de assistência para utilização dos modelos"""
from typing import Type, Union

KEYS = ['colesterol_ruim', 'glucose', 'colesterol_bom', 'idade', 'peso', 'pressao_arterial', 'cintura']

MODELOS = ['xgboost', 'rdf']


def resquest_conversors(dic: dict) -> Union[Type[Exception], dict]:
    """Realiza a conversão dos parâmetros de entrada para a mesma unidade utilizada no modelo
    >>> resquest_conversors({'colesterol_ruim': 193, 'glucose': 400, 'colesterol_bom': 49, 'idade': 19, 'peso': 119, 'altura': 1.55, 'pressao_arterial': '118x70', 'cintura': 81.28})
    {'colesterol_ruim': 193, 'glucose': 400, 'colesterol_bom': 49, 'idade': 19, 'peso': 262, 'cintura': 32.0, 'imc': 49.5, 'pressão_sistolica': 118, 'pressão_diastolica': 70}
    >>> resquest_conversors({'colesterol_ruim': 193, 'glucose': 77})
    <class 'Exception'>"""

    for key in KEYS:
        if key not in dic.keys():
            return Exception

    """Calcula IMC"""
    dic['imc'] = round(dic['peso'] / (dic['altura'] ** 2), 1)

    """Converte kilos para libras"""
    dic['peso'] = int(float(dic['peso']) * 2.20462262185)

    """Retira altura"""
    try:
        dic.pop('altura')
    except:
        return Exception

    """Converte a pressão arterial em sistólica e diastólica além de retirar o campo do dicionário original"""
    if 'X' in dic['pressao_arterial']:
        pressao_list = str(dic['pressao_arterial']).split("X")
    else:
        pressao_list = str(dic['pressao_arterial']).split("x")
    try:
        dic.pop('pressao_arterial')
        dic['pressão_sistolica'] = int(pressao_list[0])
        dic['pressão_diastolica'] = int(pressao_list[1])
    except:
        return Exception

    """Converte a cintura de centimetros para inches"""
    dic['cintura'] = round(dic['cintura'] / 2.54, 0)

    """Reorganizar o dicionário recebido para ficar igual ao DataFrame do modelo"""
    response_dict = {'colesterol_ruim': dic['colesterol_ruim'], 'glucose': dic['glucose'],
                     'colesterol_bom': dic['colesterol_bom'], 'idade': dic['idade'], 'peso': dic['peso'],
                     'cintura': dic['cintura'], 'imc': dic['imc'], 'pressão_sistolica': dic['pressão_sistolica'],
                     'pressão_diastolica': dic['pressão_diastolica']}
    return response_dict

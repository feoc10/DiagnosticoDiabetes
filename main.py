from flask import Flask, request, jsonify
import pandas as pd
from werkzeug.exceptions import abort

from modelos.modelos import XGBoost, RandomForest
from modelos.utils import resquest_conversors, MODELOS

"""Instanciando os modelos"""
xgb = XGBoost()
rdf = RandomForest()

"""Instância do Flask"""
app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def internal_error(error):
    return {"erro": "Dados invalidos"}


@app.route(f'/{MODELOS[0]}', methods=['POST'])
def xgboost():
    try:
        content = request.json
        content_convertido = resquest_conversors(dict(content))
        pred_test = str(xgb.predict(pd.DataFrame.from_dict([content_convertido]))[0])
        if pred_test == "1":
            json_resp = {"diabetes": "sim", "code": 1}
        else:
            json_resp = {"diabetes": "nao", "code": 0}
        json_resp['estimator'] = "XGBoost Classifier"
        return json_resp
    except:
        abort(500)


@app.route(f'/{MODELOS[1]}', methods=['POST'])
def random_forest_classifier():
    try:
        content = request.json
        content_convertido = resquest_conversors(dict(content))
        pred_test = str(rdf.predict(pd.DataFrame.from_dict([content_convertido]))[0])
        if pred_test == "1":
            json_resp = {"diabetes": "sim", "code": 1}
        else:
            json_resp = {"diabetes": "nao", "code": 0}
        json_resp['estimator'] = "Random Forest Classifier"
        return json_resp
    except:
        abort(500)


@app.route('/modelos', methods=['GET'])
def get_models():
    return {'modelos': MODELOS}


if __name__ == "__main__":
    app.run(host='0.0.0.0')

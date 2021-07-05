import pickle

from flask import Flask, request
import pandas as pd
import xgboost

# Carrega o modelo a ser usado
xgb = xgboost.XGBClassifier()
xgb.load_model('modelos//model_xgboost')

with open('modelos//randomforest_pickled', 'rb') as f:
  rdf = pickle.load(f)

app = Flask(__name__)


@app.route('/xgboost', methods=['GET'])
def xgboost():
    content = request.json
    pred_test = str(xgb.predict(pd.DataFrame.from_dict([dict(content)]))[0])
    if pred_test == "1":
        json_resp = {"diabetes": "sim", "code": 1}
    else:
        json_resp = {"diabetes": "nao", "code": 0}
    json_resp['estimator'] = "XGBoost Classifier"
    return json_resp


@app.route('/rdf', methods=['GET'])
def randomforestclassifier():
    content = request.json
    pred_test = str(rdf.predict(pd.DataFrame.from_dict([dict(content)]))[0])
    if pred_test == "1":
        json_resp = {"diabetes": "sim", "code": 1}
    else:
        json_resp = {"diabetes": "nao", "code": 0}

    json_resp['estimator'] = "Random Forest Classifier"
    return json_resp


if __name__ == "__main__":
    app.run(host='0.0.0.0')

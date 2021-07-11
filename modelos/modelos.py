# Carrega os modelos a serem usados
import pickle
import xgboost
from pandas import DataFrame


class XGBoost:
    """Modelo XGBoost"""

    def __init__(self):
        self.xgb = xgboost.XGBClassifier()
        self.xgb.load_model('modelos/files/model_xgboost')

    def predict(self, dt: DataFrame):
        return self.xgb.predict(dt)


class RandomForest:
    """Modelo Random Forest"""

    def __init__(self):
        with open('modelos/files/randomforest_pickled', 'rb') as f:
            self.rdf = pickle.load(f)

    def predict(self, dt: DataFrame):
        return self.rdf.predict(dt)

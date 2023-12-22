import pandas as pd
import joblib
from app.models.building import Building

class Pipeline:

    def predict(self, building: Building): 
        pipeline = joblib.load('app/iamodels/data/model_v0.pkl')

        new_predict = pd.DataFrame(building.model_dump(), index=[0])

        X_aval = pipeline['preprocessor'].transform(new_predict)
        X_aval = pipeline['imputer'].transform(X_aval)
        y_pred_aval = pipeline['regressor'].predict(X_aval)

        return y_pred_aval
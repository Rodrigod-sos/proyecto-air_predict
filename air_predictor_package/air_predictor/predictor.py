import joblib
import numpy as np
import os

class ContaminacionPredictor:
    def __init__(self, model_dir=None):
        if model_dir is None:
            model_dir = os.path.join(os.path.dirname(__file__), 'ml-model')
        
        self.model = joblib.load(os.path.join(model_dir, 'model.pkl'))
        self.sc_x = joblib.load(os.path.join(model_dir, 'scaler_x.pkl'))
        self.sc_y = joblib.load(os.path.join(model_dir, 'scaler_y.pkl'))

    def predict(self, humedad_abs, temperatura, humedad_rel, sensor_1, sensor_4, sensor_2) -> float:
        data_array = np.array([[humedad_abs, temperatura, humedad_rel, sensor_1, sensor_4, sensor_2]])
        data_array_scaled = self.sc_x.transform(data_array)
        prediction_scaled = self.model.predict(data_array_scaled)
        prediction = self.sc_y.inverse_transform(prediction_scaled.reshape(-1, 1))
        return float(round(prediction[0][0], 2))

        

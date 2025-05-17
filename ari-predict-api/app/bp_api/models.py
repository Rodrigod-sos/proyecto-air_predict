from utils.db import db
from air_predictor import ContaminacionPredictor

class MuestraAire(db.Model):
    __tablename__ = 'muestra_aire'

    id = db.Column(db.Integer, primary_key=True)
    humedad_abs = db.Column(db.Float, nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    humedad_rel = db.Column(db.Float, nullable=False)
    sensor_1 = db.Column(db.Float, nullable=False)  # estaño CO
    sensor_4 = db.Column(db.Float, nullable=False)  # NO2
    sensor_2 = db.Column(db.Float, nullable=False)  # titania NMHC
    benceno = db.Column(db.Float, nullable=True)

    def __init__(self, humedad_abs, temperatura, humedad_rel, sensor_1, sensor_4, sensor_2):
        self.humedad_abs = humedad_abs
        self.temperatura = temperatura
        self.humedad_rel = humedad_rel
        self.sensor_1 = sensor_1
        self.sensor_4 = sensor_4
        self.sensor_2 = sensor_2
        self.benceno = 0

    @staticmethod
    def get_all():
        return MuestraAire.query.all()

    @staticmethod
    def get_by_id(id):
        return MuestraAire.query.get(id)

    def save(self):
        ml_model = ContaminacionPredictor()
        self.benceno = ml_model.predict(self.humedad_abs, self.temperatura, self.humedad_rel, self.sensor_1, self.sensor_4, self.sensor_2)

        if not self.id:
            db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
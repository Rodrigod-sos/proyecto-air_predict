from flask_restful import Resource, Api, abort
from flask import request
from . import bp_api
from .models import MuestraAire
from .schemas import MuestraAireSchema

api = Api(bp_api)

class MuestraAireApiResource(Resource):

    def get(self):
        data = MuestraAire.get_all()
        schema = MuestraAireSchema(many=True)

        context = {
            'status': True,
            'message': 'Lista de muestras de aire',
            'content': schema.dump(data)
        }

        return context, 200

    def post(self):
        data = request.get_json()
        muestra = MuestraAire(
            humedad_abs=data.get('humedad_abs'),
            temperatura=data.get('temperatura'),
            humedad_rel=data.get('humedad_rel'),
            sensor_1=data.get('sensor_1'),
            sensor_4=data.get('sensor_4'),
            sensor_2=data.get('sensor_2')
        )
        muestra.save()

        schema = MuestraAireSchema()

        context = {
            'status': True,
            'message': 'Muestra creada',
            'content': schema.dump(muestra)
        }
        return context, 201

class MuestraAireApiResourceDetail(Resource):

    def get_muestra(self, id):
        muestra = MuestraAire.get_by_id(id)
        if not muestra:
            abort(404, message="Muestra no encontrada")
        return muestra

    def get(self, id):
        data = self.get_muestra(id)
        schema = MuestraAireSchema()

        context = {
            'status': True,
            'message': 'Muestra encontrada',
            'content': schema.dump(data)
        }
        return context

    def put(self, id):
        data = request.get_json()
        muestra = self.get_muestra(id)

        muestra.humedad_abs = data.get('humedad_abs')
        muestra.temperatura = data.get('temperatura')
        muestra.humedad_rel = data.get('humedad_rel')
        muestra.sensor_1 = data.get('sensor_1')
        muestra.sensor_4 = data.get('sensor_4')
        muestra.sensor_2 = data.get('sensor_2')
        muestra.save()

        schema = MuestraAireSchema()

        context = {
            'status': True,
            'message': 'Muestra actualizada',
            'content': schema.dump(muestra)
        }
        return context

    def delete(self, id):
        muestra = self.get_muestra(id)
        muestra.delete()

        return {
            'status': True,
            'message': 'Muestra eliminada'
        }, 204

api.add_resource(MuestraAireApiResource, '/')
api.add_resource(MuestraAireApiResourceDetail, '/<int:id>')
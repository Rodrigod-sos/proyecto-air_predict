from utils.db import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import MuestraAire

class MuestraAireSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MuestraAire
        load_instance = True
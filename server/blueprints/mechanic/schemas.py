from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from server.models.mechanic import Mechanic

class MechanicSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        load_instance = True
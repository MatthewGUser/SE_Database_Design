from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from server.models.service_ticket import ServiceTicket

class ServiceTicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        load_instance = True
        fields = ('VIN', 'service_date', 'service_description', 'customer_id', 'mechanic_ids')
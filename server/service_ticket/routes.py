from flask import Blueprint, request, jsonify
from server.db import db
from server.models.service_ticket import ServiceTicket
from server.models.mechanic import Mechanic
from server.service_ticket.schemas import ServiceTicketSchema

service_ticket_bp = Blueprint('service_ticket_bp', __name__)
service_ticket_schema = ServiceTicketSchema()
service_tickets_schema = ServiceTicketSchema(many=True)

@service_ticket_bp.route('/', methods=['POST'])
def create_service_ticket():
    try:
        data = request.get_json()
        mechanic_ids = data.get('mechanic_ids', [])
        
        # Validate mechanic IDs
        valid_mechanics = Mechanic.query.filter(Mechanic.id.in_(mechanic_ids)).all()
        valid_mechanic_ids = [mechanic.id for mechanic in valid_mechanics]
        
        if len(valid_mechanic_ids) != len(mechanic_ids):
            return jsonify({'error': 'One or more mechanic IDs are invalid'}), 400
        
        new_service_ticket = service_ticket_schema.load(data, session=db.session)
        db.session.add(new_service_ticket)
        db.session.commit()
        return jsonify(service_ticket_schema.dump(new_service_ticket)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@service_ticket_bp.route('/', methods=['GET'])
def get_service_tickets():
    try:
        service_tickets = ServiceTicket.query.all()
        return jsonify(service_tickets_schema.dump(service_tickets)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
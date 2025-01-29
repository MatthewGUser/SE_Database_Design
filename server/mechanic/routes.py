from flask import Blueprint, request, jsonify
from server.db import db
from server.models.mechanic import Mechanic
from server.mechanic.schemas import MechanicSchema

mechanic_bp = Blueprint('mechanic_bp', __name__)
mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)

@mechanic_bp.route('/', methods=['POST'])
def create_mechanic():
    try:
        data = request.get_json()
        new_mechanic = mechanic_schema.load(data, session=db.session)
        db.session.add(new_mechanic)
        db.session.commit()
        return jsonify(mechanic_schema.dump(new_mechanic)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    try:
        mechanics = Mechanic.query.all()
        return jsonify(mechanics_schema.dump(mechanics)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@mechanic_bp.route('/<int:id>', methods=['PUT'])
def update_mechanic(id):
    try:
        mechanic = Mechanic.query.get_or_404(id)
        data = request.get_json()
        mechanic.name = data.get('name', mechanic.name)
        mechanic.expertise = data.get('expertise', mechanic.expertise)
        db.session.commit()
        return jsonify(mechanic_schema.dump(mechanic)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@mechanic_bp.route('/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    try:
        mechanic = Mechanic.query.get_or_404(id)
        db.session.delete(mechanic)
        db.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500
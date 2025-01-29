from server.db import db
from sqlalchemy.dialects.mysql import JSON

class ServiceTicket(db.Model):
    __tablename__ = 'service_tickets'
    id = db.Column(db.Integer, primary_key=True)
    VIN = db.Column(db.String(17), nullable=False)
    service_date = db.Column(db.Date, nullable=False)
    service_description = db.Column(db.String(255), nullable=False)
    mechanic_ids = db.Column(JSON, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'VIN': self.VIN,
            'service_date': self.service_date,
            'service_description': self.service_description,
            'mechanic_ids': self.mechanic_ids
        }
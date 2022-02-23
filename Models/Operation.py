from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from Constants.models import CARD_TYPE
from Models.User import User
from app import BaseModel, engine


class Operation(BaseModel):
    __tablename__ = 'operations'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    user_create_id = Column(Integer, ForeignKey('users.id'))
    type = Column(Integer)
    sum = Column(Integer)
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    date_delete = Column(DateTime)

    user_create = relationship("User", lazy='joined')
    patient = relationship("Patient", lazy='joined')

    def from_object(self, record: dict):
        self.id = record.get('id')
        self.patient_id = record.get('patient_id')
        self.user_create_id = engine.session.query(User).where(User.uuid == record.get('user')).first().id
        self.type = record.get('type') or CARD_TYPE['AMBULANCE']
        self.sum = record.get('sum') or 0
        self.date_create = datetime.now()
        self.date_update = datetime.now()
        self.date_delete = record.get('date_delete')

        return self

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'user_create_id': self.user_create_id,
            'type': self.type,
            'sum': self.sum,
            'date_create': self.date_create,
            'date_update': self.date_update,
            'date_delete': self.date_delete,
            'user_create': self.user_create,
            'patient': self.patient
        }

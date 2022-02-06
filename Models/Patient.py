import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app import BaseModel, engine
from Platform.Helpers.Password import Password
from .Role import Role


class Patient(BaseModel):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    uuid = Column(Text, unique=True)
    name = Column(Text, nullable=False, index=True)
    surname = Column(Text, nullable=False, index=True)
    second_name = Column(Text, nullable=False, index=True)
    telephone = Column(Text, nullable=False, index=True)
    email = Column(Text, nullable=True, index=True)
    doctor_id = Column(Integer, ForeignKey('users.id'))
    ward = Column(Text)
    discription = Column(Text)
    comment = Column(Text)
    type = Column(Integer)
    num_card = Column(Integer)
    date_birthday = Column(Date)
    date_create = Column(Date)
    date_update = Column(Date)
    date_delete = Column(Date)
    date_discharge = Column(Date)
    date_receipt = Column(Date)

    doctor = relationship("User")

    def from_object(self, record: dict):
        self.id = record.get('id')
        self.uuid = record.get('uuid') or str(uuid.uuid4())
        self.name = record.get('name')
        self.surname = record.get('surname')
        self.second_name = record.get('second_name')
        self.telephone = record.get('telephone')
        self.email = record.get('email')
        self.doctor_id = record.get('doctor_id')
        self.ward = record.get('ward')
        self.discription = record.get('discription')
        self.comment = record.get('comment')
        self.type = record.get('type')
        self.num_card = record.get('num_card')
        self.date_birthday = record.get('date_birthday')
        self.date_create = record.get('date_create') or datetime.now().date()
        self.date_update = datetime.now().date()
        self.date_delete = record.get('date_delete')
        self.date_discharge = record.get('date_discharge')
        self.date_receipt = record.get('date_receipt') or datetime.now().date()

        return self

    def to_dict(self):
        return {
            'id': self.id,
            'uuid': self.uuid or '',
            'name': self.name,
            'surname': self.surname,
            'second_name': self.second_name,
            'telephone': self.telephone,
            'email': self.email,
            'doctor_id': self.doctor_id,
            'ward': self.ward,
            'discription': self.discription,
            'comment': self.comment,
            'type': self.type,
            'num_card': self.num_card,
            'date_birthday': self.date_birthday,
            'date_create': self.date_create,
            'date_update': self.date_update,
            'date_delete': self.date_delete,
            'date_discharge': self.date_discharge,
            'date_receipt': self.date_receipt,
            'full_name': '{} {}.{}'.format(self.surname or '',
                                           self.name if self.name else '',
                                           self.second_name if self.second_name else '')
        }

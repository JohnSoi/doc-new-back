from datetime import datetime

from sqlalchemy import Column, Integer, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from Models.User import User
from app import BaseModel, engine


class Service(BaseModel):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(Text, index=True)
    description = Column(Text)
    price = Column(Integer)
    bonus_work = Column(Integer)
    is_bonus_work_percent = Column(Boolean, default=False)
    bonus_add = Column(Integer)
    is_bonus_add_percent = Column(Boolean, default=False)
    user_create_id = Column(Integer, ForeignKey('users.id'))
    date_create = Column(DateTime)
    date_update = Column(DateTime)
    date_delete = Column(DateTime)

    user_create = relationship("User", lazy='joined')

    def from_object(self, record: dict):
        self.name = record.get('name')
        self.description = record.get('description')
        self.price = record.get('price')
        self.bonus_work = record.get('bonus_work')
        self.is_bonus_work_percent = record.get('is_bonus_work_percent')
        self.bonus_add = record.get('bonus_add')
        self.is_bonus_add_percent = record.get('is_bonus_add_percent')
        self.date_create = datetime.now()
        self.date_update = datetime.now()
        self.date_delete = record.get('date_delete')
        self.user_create_id = engine.session.query(User).where(User.uuid == record.get('user')).first().id

        return self

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'bonus_work': self.bonus_work or 0,
            'is_bonus_work_percent': self.is_bonus_work_percent or False,
            'bonus_add': self.bonus_add or 0,
            'is_bonus_add_percent': self.is_bonus_add_percent or False,
            'date_create': self.date_create,
            'date_update': self.date_update,
            'date_delete': self.date_delete,
            'user_create': self.user_create
        }

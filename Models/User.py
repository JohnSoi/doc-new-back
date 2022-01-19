from sqlalchemy import Column, Integer, Text, Date, Boolean
from sqlalchemy.orm import relationship

from app import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, index=True)
    surname = Column(Text, nullable=False, index=True)
    second_name = Column(Text, nullable=False, index=True)
    role_id = Column(Integer)
    photo_url = Column(Text)
    login = Column(Text, nullable=False, index=True)
    password = Column(Text, nullable=False)
    date_create = Column(Date)
    date_update = Column(Date)
    date_delete = Column(Date)
    last_active = Column(Date)
    is_active = Column(Boolean, default=True)

    role = relationship("Role")

    def from_object(self, record: dict):
        self.id = record.get('id')
        self.name = record.get('name')
        self.surname = record.get('surname')
        self.second_name = record.get('second_name')
        self.role_id = record.get('role_id')
        self.photo_url = record.get('photo_url')
        self.login = record.get('login')
        self.password = record.get('password')
        self.date_create = record.get('date_create')
        self.date_update = record.get('date_update')
        self.date_delete = record.get('date_delete')
        self.last_active = record.get('last_active')
        self.is_active = record.get('is_active')

    def to_dict(self):
        return {
             'id': self.id,
             'name': self.name,
             'surname': self.surname,
             'second_name': self.second_name,
             'role_id': self.role_id,
             'photo_url': self.photo_url,
             'login': self.login,
             'password': self.password,
             'date_create': self.date_create,
             'date_update': self.date_update,
             'date_delete': self.date_delete,
             'last_active': self.last_active,
             'is_active': self.is_active,
        }




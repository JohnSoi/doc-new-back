from sqlalchemy import Column, Integer, Text
from app import BaseModel


class Permission(BaseModel):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    name = Column(Text, index=True)

    def from_object(self, record: dict):
        self.name = record.get('name')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from models.rol_model import RolModel
import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200), unique=True)
    password = Column(Text)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    rol_id = Column(Integer, ForeignKey('roles.id'))

    rol = relationship(RolModel)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'email': self.email,
            'status': self.status,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'rol_id': self.rol_id
        }
from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

class RolModel(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    status = Column(Boolean, default=True)
from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
)
import datetime

class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    code = Column(String(50))
    client_name = Column(String(200))
    client_last_name = Column(String(200))
    client_address = Column(String(200))
    client_document_number = Column(String(20))
    total = Column(Float)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

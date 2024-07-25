from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)
import datetime


class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
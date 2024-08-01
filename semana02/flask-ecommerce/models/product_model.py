from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    Boolean,
    DateTime,
    ForeignKey
)
import datetime

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    code = Column(String(50))
    description = Column(Text)
    image = Column(Text)
    brand = Column(String(100))
    size = Column(String(10))
    price = Column(Float)
    stock = Column(Integer)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    category_id = Column(Integer, ForeignKey('categories.id'))


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'image': self.image,
            'brand': self.brand,
            'size': self.size,
            'price': self.price,
            'stock': self.stock,
            'status': self.status,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'category_id': self.category_id
        }
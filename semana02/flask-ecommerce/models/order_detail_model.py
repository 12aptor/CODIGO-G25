from db import db
from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
)


class OrderDetailModel(db.Model):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    price = Column(Float)
    subtotal = Column(Float)
    product_id = Column(Integer, ForeignKey('products.id'))
    order_id = Column(Integer, ForeignKey('orders.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'quantity': self.quantity,
            'price': self.price,
            'subtotal': self.subtotal,
            'product_id': self.product_id,
            'order_id': self.order_id
        }
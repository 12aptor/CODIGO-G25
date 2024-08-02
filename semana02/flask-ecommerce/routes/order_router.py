from flask import Blueprint, request
from controllers.order_controller import OrderController

order_router = Blueprint('order_router', __name__)
controller = OrderController()

@order_router.post('/create')
def create_order():
    json = request.json
    return controller.create(json)
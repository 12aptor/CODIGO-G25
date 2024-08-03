from flask import Blueprint, request
from controllers.order_controller import OrderController
from utils.utils import role_required

order_router = Blueprint('order_router', __name__)
controller = OrderController()

@order_router.post('/create')
def create_order():
    json = request.json
    return controller.create(json)

@order_router.get('/get_all')
@role_required()
def get_all_orders():
    return controller.get_all()

@order_router.delete('/cancel/<int:id>')
@role_required()
def cancel_order(id: int):
    return controller.cancel(id)
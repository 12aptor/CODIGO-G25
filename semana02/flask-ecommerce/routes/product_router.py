from flask import Blueprint, request
from utils.utils import role_required
from controllers.product_controller import ProductController


product_router = Blueprint('product_router', __name__)
controller = ProductController()


@product_router.post('/create')
@role_required()
def create_product():
    image = request.files.get('image')
    form = request.form
    return controller.create(form, image)

@product_router.get('/get_all')
@role_required()
def get_all_products():
    return controller.get_all()

@product_router.get('/get_all_for_clients')
def get_all_products_for_clients():
    return controller.get_all_for_clients()

@product_router.put('/update/<int:id>')
@role_required()
def update_product(id: int):
    image = request.files.get('image')
    form = request.form
    return controller.update(id, form, image)

@product_router.delete('/delete/<int:id>')
@role_required()
def delete_product(id: int):
    return controller.delete(id)

@product_router.get('/get_by_id/<int:id>')
def get_product_by_id(id: int):
    return controller.get_by_id(id)
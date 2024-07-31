from flask import Blueprint, request
from utils.utils import role_required
from controllers.category_controller import CategoryController


category_router = Blueprint('category_router', __name__)
controller = CategoryController()

@category_router.post('/create')
@role_required('ADMIN')
def create_category():
    json = request.json
    return controller.create(json)

@category_router.get('/get_all')
@role_required('ADMIN')
def get_all_categories():
    return controller.get_all()

@category_router.get('/get_all_for_clients')
def get_all_categories_for_clients():
    return controller.get_all_for_clients()

@category_router.put('/update/<int:id>')
def update_category(id):
    json = request.json
    return controller.update(id, json)
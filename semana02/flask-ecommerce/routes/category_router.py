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
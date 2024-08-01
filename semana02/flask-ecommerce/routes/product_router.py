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
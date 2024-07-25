from flask import Blueprint, request
from controllers.rol_controller import RolController

rol_router = Blueprint('rol_router', __name__)
controller = RolController()

@rol_router.post('/create')
def create_rol():
    json = request.json
    return controller.create(json)
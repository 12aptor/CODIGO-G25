from flask import Blueprint, request
from controllers.rol_controller import RolController
from utils.utils import role_required


rol_router = Blueprint('rol_router', __name__)
controller = RolController()

@rol_router.post('/create')
@role_required('ADMIN')
def create_rol():
    json = request.json
    return controller.create(json)

@rol_router.get('/get_all')
@role_required('ADMIN')
def get_all_roles():
    return controller.get_all()

@rol_router.put('/update/<int:id>')
@role_required('ADMIN')
def update_rol(id):
    json = request.json
    return controller.update(id, json)

@rol_router.delete('/delete/<int:id>')
@role_required('ADMIN')
def delete_rol(id):
    return controller.delete(id)
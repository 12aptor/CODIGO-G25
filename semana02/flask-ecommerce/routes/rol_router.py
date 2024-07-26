from flask import Blueprint, request
from controllers.rol_controller import RolController

rol_router = Blueprint('rol_router', __name__)
controller = RolController()

@rol_router.post('/create')
def create_rol():
    json = request.json
    return controller.create(json)

@rol_router.get('/get_all')
def get_all_roles():
    return controller.get_all()

@rol_router.put('/update/<int:id>')
def update_rol(id):
    json = request.json
    return controller.update(id, json)

@rol_router.delete('/delete/<int:id>')
def delete_rol(id):
    return controller.delete(id)
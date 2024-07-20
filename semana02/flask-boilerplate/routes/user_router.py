from flask import Blueprint, request
from controllers.user_controller import UserController

user_router = Blueprint('user_router', __name__)
controller = UserController()

@user_router.post('/create')
def create_user():
    json = request.json
    return controller.create(json)

@user_router.get('/get_all')
def get_all_users():
    return controller.get_all()

@user_router.get('/get_by_id/<int:id>')
def get_user_by_id(id):
    return controller.get_by_id(id)

@user_router.put('/update/<int:id>')
def update_user(id):
    json = request.json
    return controller.update(id, json)
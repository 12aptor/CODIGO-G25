from flask_jwt_extended import (
    get_jwt_identity,
    verify_jwt_in_request,
)
from functools import wraps
from models.user_model import UserModel


def role_required(role: str):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()

            identity = get_jwt_identity()
            user = UserModel.query.get(identity)

            if user is None or user.status == False:
                return {
                    'message': 'Unauthorized'
                }, 401
            
            if user.rol.name != role:
                return {
                    'message': 'Unauthorized'
                }, 401
            
            return fn(*args, **kwargs)
        return wrapper
    return decorator
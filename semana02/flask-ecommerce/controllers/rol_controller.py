from models.rol_model import RolModel
from models.user_model import UserModel
from schemas.rol_schema import RolSchema, UpdateRolSchema
from pydantic import ValidationError
from db import db
from flask_jwt_extended import get_jwt_identity


class RolController:
    def __init__(self):
        self.model = RolModel
        self.user_model = UserModel

    def create(self, json: dict):
        try:
            validated_rol = RolSchema(**json)
        
            new_rol = self.model(**validated_rol.model_dump())

            db.session.add(new_rol)
            db.session.commit()
            
            return {
                'message': 'Rol created successfully',
                'data': new_rol.to_dict(),
            }, 201
        except ValidationError as e:
            return {
                'message': 'Validation Error',
                'errors': e.errors(),
            }, 400

        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
        
    def get_all(self):
        try:
            identity = get_jwt_identity()
            user = self.user_model.query.get(identity)

            if user is None:
                return {
                    'message': 'Unauthorized',
                }, 401
            
            # if user.rol.name == 'ADMIN':

            roles = self.model.query.all()

            return {
                'message': 'Roles fetched successfully',
                'data': [rol.to_dict() for rol in roles],
            }
        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
        
    def update(self, id: int, json: dict):
        try:
            rol = self.model.query.get(id)

            if rol is None:
                return {
                    'message': 'Rol not found',
                }, 404

            validated_rol = UpdateRolSchema(**json)

            rol.name = validated_rol.name
            rol.status = validated_rol.status

            db.session.commit()

            return {
                'message': 'Rol updated successfully',
                'data': rol.to_dict()
            }, 200
        except ValidationError as e:
            return {
                'message': 'Validation Error',
                'errors': e.errors(),
            }, 400

        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500

    def delete(self, id: int):
        try:
            rol = self.model.query.get(id)

            if rol is None:
                return {
                    'message': 'Rol not found',
                }, 404

            db.session.delete(rol)
            db.session.commit()

            return {
                'message': 'Rol deleted successfully',
            }, 200
        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
from models.rol_model import RolModel
from schemas.rol_schema import RolSchema
from pydantic import ValidationError
from db import db


class RolController:
    def __init__(self):
        self.model = RolModel

    def create(self, json):
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
        roles = self.model.query.all()

        return {
            'message': 'Roles fetched successfully',
            'data': [rol.to_dict() for rol in roles],
        }
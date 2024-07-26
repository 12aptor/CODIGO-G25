from models.user_model import UserModel
from pydantic import ValidationError
from schemas.user_schema import UserSchema
import bcrypt
from db import db

class UserController:
    def __init__(self):
        self.model = UserModel

    def create(self, json: dict):
        try:
            validated_user = UserSchema(**json)

            user = self.model.query.filter_by(email=validated_user.email).first()

            if user:
                return {
                    'message': 'User already exists',
                }, 400

            validated_user.password = self.__hash_password(validated_user.password)

            new_user = self.model(**validated_user.model_dump())

            db.session.add(new_user)
            db.session.commit()

            return {
                'message': 'User created successfully',
                'data': new_user.to_dict()
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
        
    def __hash_password(self, password: str):
        pwd_bytes = password.encode('utf-8')
        pwd_hashed = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
        return pwd_hashed.decode('utf-8')
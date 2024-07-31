from models.category_model import CategoryModel
from pydantic import ValidationError
from schemas.category_schema import (
    CategorySchema,
    UpdateCategorySchema
)
from db import db


class CategoryController:
    def __init__(self):
        self.model = CategoryModel

    def create(self, json: dict):
        try:
            validated_categroy = CategorySchema(**json)

            new_category = self.model(**validated_categroy.model_dump())

            db.session.add(new_category)
            db.session.commit()

            return {
                'message': 'Category created successfully',
                'data': new_category.to_dict()
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
            categories = self.model.query.order_by(self.model.id.asc()).all()

            return {
                'message': 'Categories fetched successfully',
                'data': [category.to_dict() for category in categories]
            }, 200
        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
        
    def get_all_for_clients(self):
        try:
            categories = self.model.query.filter_by(status=True).all()

            return {
                'message': 'Categories fetched successfully',
                'data': [category.to_dict() for category in categories]
            }, 200
        except Exception as e:
            return {
                'message': 'An error occurred',
            }, 500
        
    def update(self, id: int, json: dict):
        try:
            validated_category = UpdateCategorySchema(**json)

            category = self.model.query.get(id)

            if category is None:
                return {
                    'message': 'Category not found',
                }, 404
            
            category.name = validated_category.name
            category.status = validated_category.status

            db.session.commit()

            return {
                'message': 'Category updated successfully',
                'data': category.to_dict()
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
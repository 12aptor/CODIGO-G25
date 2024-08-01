from models.product_model import ProductModel
from schemas.product_schema import ProductSchema, UpdateProductSchema
from typing import Union
from werkzeug.datastructures import FileStorage, MultiDict
from pydantic import ValidationError
import utils.cloudinary_config
import cloudinary.uploader
import uuid
from db import db


class ProductController:
    def __init__(self):
        self.model = ProductModel

    def create(self, form: MultiDict, image: Union[FileStorage, None]):
        try:
            if image is None:
                return {
                    'message': 'Image not found',
                }, 400

            validated_product = ProductSchema(**form)

            filename = image.filename.split('.')[0]
            public_id = f'{uuid.uuid4()}-{filename}'

            cloudinary.uploader.upload(image.stream, public_id=public_id)

            new_product = self.model(**validated_product.model_dump())
            new_product.image = public_id

            db.session.add(new_product)
            db.session.commit()

            return {
                'message': 'Product created successfully',
                'product': new_product.to_dict()
            }
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
            products = self.model.query.all()

            return {
                'message': 'Products fetched successfully',
                'data': [product.to_dict() for product in products]
            }, 200
        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
        
    def get_all_for_clients(self):
        try:
            products = self.model.query.filter_by(status=True).all()

            return {
                'message': 'Products fetched successfully',
                'data': [product.to_dict() for product in products]
            }, 200
        except Exception as e:
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
        
    def update(self, id: int, form: MultiDict, image: Union[FileStorage, None]):
        try:
            validated_product = UpdateProductSchema(**form)

            product = self.model.query.get(id)

            if product is None:
                return {
                    'message': 'Product not found',
                }, 404
            
            product.name = validated_product.name
            product.code = validated_product.code
            product.description = validated_product.description

            if image is not None:
                filename = image.filename.split('.')[0]
                public_id = f'{uuid.uuid4()}-{filename}'

                cloudinary.uploader.upload(image.stream, public_id=public_id)
                cloudinary.uploader.destroy(product.image)
                
                product.image = public_id

            product.brand = validated_product.brand
            product.size = validated_product.size
            product.price = validated_product.price
            product.stock = validated_product.stock
            product.status = validated_product.status
            product.category_id = validated_product.category_id

            db.session.commit()

            return {
                'message': 'Product updated successfully',
                'data': product.to_dict()
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

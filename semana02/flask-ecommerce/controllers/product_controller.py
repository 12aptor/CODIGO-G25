from models.product_model import ProductModel
from schemas.product_schema import ProductSchema
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
            upload_response = cloudinary.uploader.upload(image.stream, public_id=f'{uuid.uuid4()}-{filename}')

            new_product = self.model(**validated_product.model_dump())
            new_product.image = upload_response['secure_url']

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
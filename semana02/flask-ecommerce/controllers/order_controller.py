from pydantic import ValidationError
from models.product_model import ProductModel
from models.order_model import OrderModel
from models.order_detail_model import OrderDetailModel
from schemas.order_schema import OrderSchema
from db import db


class OrderController:
    def __init__(self) -> None:
        self.product_model = ProductModel
        self.order_model = OrderModel
        self.order_detail_model = OrderDetailModel

    def create(self, json: dict):
        try:
            # Validar la data
            validated_order = OrderSchema(**json)

            # Validar el stock
            details = validated_order.order_details
            
            new_order_details = []
            for detail in details:
                product = self.product_model.query.get(detail.product_id)

                # Validar la existencia del producto
                if product is None:
                    return {
                        'message': 'Product not found',
                    }, 404
                
                # Validar el estado del producto
                if product.status == False:
                    return {
                        'message': f'Product {product.name} is out of stock',
                    }, 400
                
                # Validar el stock del producto
                if product.stock < detail.quantity:
                    return {
                        'message': f'Product {product.name} is out of stock'
                    }, 400
                
                # Actualizar el stock del producto
                product.stock -= detail.quantity

                # Crear el detalle de la orden
                new_order_detail = self.order_detail_model(
                    quantity=detail.quantity,
                    price=detail.price,
                    subtotal=detail.subtotal,
                    product_id=detail.product_id
                )
                new_order_details.append(new_order_detail)

            # Generar el código de la orden
            last_order = self.order_model.query.order_by(self.order_model.id.desc()).first()

            new_code = ''
            if last_order is None:
                new_code = 'C01-0001'
            else:
                num_order = int(last_order.code.split('-')[1])
                num_order += 1
                new_num_order = str(num_order).zfill(4)
                new_code = f'C01-{new_num_order}'

            # Crear la orden
            new_order = self.order_model(
                code=new_code,
                client_name=validated_order.client_name,
                client_last_name=validated_order.client_last_name,
                client_address=validated_order.client_address,
                client_document_number=validated_order.client_document_number,
                total=validated_order.total,
                order_details=new_order_details
            )

            db.session.add(new_order)
            db.session.commit()

            return {
                'message': 'Order created successfully',
                'data': new_order.to_dict()
            }, 201
        except ValidationError as e:
            return {
                'message': 'Validation Error',
                'errors': e.errors(),
            }, 400

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'An error occurred',
                'error': str(e)
            }, 500
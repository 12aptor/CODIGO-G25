from pydantic import ValidationError
from models.product_model import ProductModel
from models.order_model import OrderModel
from models.order_detail_model import OrderDetailModel
from schemas.order_schema import OrderSchema


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

            # Crear la vente

            # Actualizar el stock del producto

            # Guardar los cambios en la base de datos

            return {
                'message': 'Order created successfully',
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
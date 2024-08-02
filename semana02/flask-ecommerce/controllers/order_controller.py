from models.product_model import ProductModel
from schemas.order_schema import OrderSchema


class OrderController:
    def __init__(self) -> None:
        self.model = ProductModel

    def create(self, json: dict):
        try:
            # Validar los datos


            # Validar el stock del producto

            # Crear la vente

            # Actualizar el stock del producto

            # Guardar los cambios en la base de datos

            return {

            }, 201
        except Exception as e:
            pass
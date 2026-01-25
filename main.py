import datetime
from services.product_service import ProductService
from models.product import Product

product_service = ProductService()

print(
    product_service.create(
        product=Product(
            0,
            datetime.datetime.now(),
            None,
            "Memória RAM ECC DDR4 16GB",
            "Memória para o Kit Xeon!",
            7,
            399.99,
        )
    )
)

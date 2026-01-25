import datetime
from services.product_service import ProductService
from models.product import Product

import rich

product_service = ProductService()

rich.print(product_service.getAll())

rich.print("Vamos cadastrar um produto novo:")
name = str(input("Nome: "))
description = str(input("Descrição: "))
quantity = int(input("Quantidade: "))
price = float(input("Preço: "))

product_service.create(
    product=Product(
        0,
        datetime.datetime.now(),
        None,
        name,
        description,
        quantity,
        price,
    )
)

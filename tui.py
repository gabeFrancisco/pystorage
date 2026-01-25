from services.product_service import ProductService
from models.product import Product
import datetime

import rich
from rich.prompt import Prompt

p = ProductService()


class TUI:

    @staticmethod
    def printProductsList():
        rich.print(p.getAll())

    @staticmethod
    def createProductInput():
        rich.print("Vamos cadastrar um produto novo:")

        name = Prompt.ask("Nome: ")
        description = Prompt.ask("Descrição: ")
        quantity = Prompt.ask("Quantidade: ")
        price = Prompt.ask("Preço: ")

        p.create(
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

    @staticmethod
    def getProduct():
        id = Prompt.ask("Id do produto: ")
        rich.print(p.get(id))

    @staticmethod
    def getProductsTotal():
        rich.print(p.getTotal())

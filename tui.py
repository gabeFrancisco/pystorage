from services.product_service import ProductService
from services.category_service import CategoryService

from models.product import Product
from models.category import Category

from datetime import datetime

import rich
from rich.prompt import Prompt

p = ProductService()
c = CategoryService()


class TUI:

    # Categories ------------------------------------------------------------------

    @staticmethod
    def printCategoriesList():
        rich.print(c.getAll())

    @staticmethod
    def createCategoryInput():
        rich.print("Vamos cadastrar uma categoria nova:")

        name = Prompt.ask("Nome")

        c.create(category=Category(0, datetime.now(), None, name))

    # Products -------------------------------------------------------------------

    @staticmethod
    def printProductsList():
        rich.print(p.getAll())

    @staticmethod
    def createProductInput():
        rich.print("Vamos cadastrar um produto novo:")

        name = Prompt.ask("Nome ")
        description = Prompt.ask("Descrição ")
        quantity = Prompt.ask("Quantidade ")
        price = Prompt.ask("Preço ")

        p.create(
            product=Product(
                0,
                datetime.now(),
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

    @staticmethod
    def deleteProduct():
        id = Prompt.ask("Id do produto: ")
        rich.print(p.delete(id))

from datetime import datetime
from models.base_entity import BaseEntity


class Product(BaseEntity):
    def __init__(
        self,
        id: int,
        created_at,
        updated_at,
        name: str,
        description: str,
        quantity: int,
        price: float,
    ):
        super().__init__(id, created_at, updated_at)
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

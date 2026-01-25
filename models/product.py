from datetime import datetime
from models.base_entity import BaseEntity


class Product(BaseEntity):
    def __init__(self, 
                id: int,
                created_at: datetime,
                updated_at: datetime,
                name: str, 
                description: str,
                quantity: int, 
                price: float
                ):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
    
    
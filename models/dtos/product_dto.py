class ProductDTO:
    def __init__(
        self,
        id: int,
        created_at,
        updated_at,
        name: str,
        description: str,
        quantity: int,
        price: float,
        category: str,
    ):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.category = category

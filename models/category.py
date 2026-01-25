from datetime import datetime
from models.base_entity import BaseEntity


class Category(BaseEntity):
    def __init__(self, id, created_at, updated_at, name):
        super().__init__(id, created_at, updated_at)
        self.name = name

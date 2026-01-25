from abc import ABC
from datetime import datetime


class BaseEntity(ABC):
    def __init__(self, id: str, created_at: None, updated_at: None):
        self.id = id

        if created_at is None:
            self._created_at = datetime.now()
        else:
            self._created_at = created_at

        self.updated_at = updated_at

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime):
        self._created_at = value

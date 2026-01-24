from abc import ABC, abstractmethod
from datetime import datetime

class BaseEntity(ABC):
    def __init__(self, id: str, created_at: datetime | None, updated_at: datetime | None):
        self.id = id

        if(created_at is None):
            self._created_at = datetime.now
        else:
            self._created_at = created_at

        self.updated_at = updated_at
    
    @property
    def created_at(self) -> datetime:
        return self._created_at




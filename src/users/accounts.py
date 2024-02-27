from uuid import UUID
from typing import TypeVar

from src.users.auth.credentials import Credentials

class Account:
    def __init__(self, id : UUID, credentials : Credentials = None):
        self.__id = id
        self.__credentials = credentials

    def verify(self, credentials : Credentials) -> bool:
        return self.__credentials.verify_password(credentials.password)
    
    def revoke(self):
        self.__credentials = None
        return self

    @property
    def id(self) -> UUID:
        return self.__id
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)
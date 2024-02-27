from typing import TypeVar

class Account:
    ID = TypeVar('ID')
    def __init__(self, id : ID):
        self.__id = id
    
    @property
    def id(self) -> ID:
        return self.__id
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)
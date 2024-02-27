from abc import ABC, abstractmethod
from typing import Protocol
from typing import Optional
from typing import List

from src.users.auth.credentials import Credentials
from src.users.accounts import Account
from src.users.contacts import Contact


class Accounts(ABC):

    @abstractmethod
    async def create(self, account : Account):
        ...

    @abstractmethod
    async def read(self, **kwargs) -> Optional[Account]:
        ...

    @abstractmethod
    async def update(self, account : Account):
        ...

    @abstractmethod
    async def delete(self, account : Account):
        ...


class Contacts(ABC):

    @abstractmethod
    async def add(self, account : Account, contact : Contact):
        ...

    @abstractmethod
    async def get(self, account : Account) -> List[Contact]:
        ...

    @abstractmethod
    async def remove(self, account : Account, contact : Contact):
        ...


class UnitOfWork(Protocol):
    accounts : Accounts
    contacts : Contacts


    async def __aenter__(self):
        ...
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        ...
    
    async def commit(self):
        ...
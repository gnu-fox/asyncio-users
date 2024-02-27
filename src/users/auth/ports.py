from abc import ABC, abstractmethod
from typing import Protocol
from typing import Optional
from typing import List

from users.models import Account

class Accounts(Protocol):

    async def create(self, account : Account):
        ...

    async def read(self, **kwargs) -> Optional[Account]:
        ...

    async def update(self, account : Account):
        ...

    async def delete(self, account : Account):
        ...


class UnitOfWork(Protocol):
    accounts : Accounts

    async def __aenter__(self):
        ...
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        ...
    
    async def commit(self):
        ...
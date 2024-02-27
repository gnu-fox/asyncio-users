import pytest
import uuid

from src.domain.models import Account

def test_accounts():
    identity = uuid.uuid4()
    account = Account(id=identity)
    other_account = Account(id=identity)
    assert account == other_account
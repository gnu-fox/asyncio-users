import uuid
import pytest
import asyncio
import datetime
import logging

from src.users.auth.credentials import Credentials, SecretStr
from src.users.auth.security import Security
from src.users.auth.tokens import Token, Tokenizer, Claim
from src.users import exceptions

LOGGER = logging.getLogger(__name__)

def test_security():
    LOGGER.info("Testing Security")

    security = Security
    hash = security.hash("password")
    assert isinstance(hash, SecretStr)

    assert security.verify("password", hash) == True
    assert security.verify(SecretStr("password"), hash) == True
    assert security.verify("wrong", hash) == False

    hash = security.hash(SecretStr("password"))
    assert security.verify("password", hash) == True

def test_tokenizer():
    LOGGER.info("Testing Tokenizer")

    subject = uuid.uuid4()
    claim = Claim(sub=subject, exp=datetime.timedelta(seconds=1))
    other_claim = Claim(sub=str(subject),exp=(datetime.datetime.now() + datetime.timedelta(seconds=1)))

    assert claim.sub == other_claim.sub
    assert claim.exp == other_claim.exp

    token = Tokenizer.encode(claim)
    LOGGER.info(f"Encoded {claim}")
    LOGGER.info(f"Token: {token}")

    assert isinstance(token, Token)


    decoded = Tokenizer.decode(token)
    assert decoded.sub == str(subject)

    LOGGER.info(f"Decoded {decoded}")
    
    asyncio.run(asyncio.sleep(2))

    with pytest.raises(exceptions.TokenExpired):
        Tokenizer.decode(token)

def test_credentials():
    LOGGER.info("Testing Credentials")

    credentials = Credentials(id=uuid.uuid4(), username="admin", email="admin@gmail.com", password="admin")
    assert credentials.id
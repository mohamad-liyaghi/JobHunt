import pytest
import pytest_asyncio  # noqa
import asyncio
from tests.fixtures.db import get_test_session  # noqa
from tests.fixtures.user import user  # noqa
from tests.fixtures.client import client  # noqa
from tests.utils.controllers import user_controller  # noqa


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

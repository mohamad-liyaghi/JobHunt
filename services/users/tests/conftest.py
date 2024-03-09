import pytest
import pytest_asyncio  # noqa
import asyncio
from tests.fixtures.db import get_test_session  # noqa


@pytest.fixture(scope="class")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

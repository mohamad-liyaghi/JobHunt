import pytest
import pytest_asyncio  # noqa
import asyncio


@pytest.fixture(scope="class")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

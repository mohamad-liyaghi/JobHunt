from httpx import AsyncClient
import pytest_asyncio
from main import app


@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncClient:
    """
    Create a new FastAPI AsyncClient
    """

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

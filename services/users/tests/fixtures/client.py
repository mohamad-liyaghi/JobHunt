from httpx import AsyncClient
import pytest_asyncio
from main import app
from core.handlers import JWTHandler


@pytest_asyncio.fixture(scope="session")
async def client() -> AsyncClient:
    """
    Create a new FastAPI AsyncClient
    """

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture(scope="session")
async def authorized_client(user, client) -> AsyncClient:
    """
    Create a new user and login
    """
    access_token = await JWTHandler.create_access_token(
        data={"user_uuid": str(user.uuid), "user_id": str(user.id)}
    )
    client.headers.update({"Authorization": f"Bearer {access_token}"})
    return client

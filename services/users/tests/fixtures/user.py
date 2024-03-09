import pytest_asyncio
from tests.utils.mocks import create_fake_user_credentials  # noqa
from app.models import User


@pytest_asyncio.fixture(scope="session")
async def user(user_controller) -> User:
    credentials = await create_fake_user_credentials()
    return await user_controller.create(**credentials)

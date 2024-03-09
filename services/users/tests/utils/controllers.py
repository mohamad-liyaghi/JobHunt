import pytest_asyncio
from app.controllers import UserController
from app.repositories import UserRepository


@pytest_asyncio.fixture(scope="session")
async def user_controller(get_test_session) -> UserController:
    return UserController(repository=UserRepository(database_session=get_test_session))
